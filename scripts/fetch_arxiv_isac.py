#!/usr/bin/env python3
"""Search for Integrated Sensing and Communication (ISAC) + AI papers.

Queries the arXiv API (https://info.arxiv.org/help/api/index.html) and falls
back to OpenAlex (https://docs.openalex.org/) when arXiv is unreachable, then
prints the results as markdown.

arXiv blocks some hosts outright — CI runners among them — so a single-source
script silently stops updating. OpenAlex indexes arXiv preprints with
abstracts and has no such restriction, which keeps the report current
wherever this runs.

Usage:
    python fetch_arxiv_isac.py                 # print to stdout
    python fetch_arxiv_isac.py -o report.md    # write to a file
    python fetch_arxiv_isac.py -n 20           # 20 results per category
    python fetch_arxiv_isac.py --source openalex   # skip arXiv entirely

Only the standard library is used — no packages to install.
"""

import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ARXIV_URL = "https://export.arxiv.org/api/query"
OPENALEX_URL = "https://api.openalex.org/works"
ATOM = "{http://www.w3.org/2005/Atom}"

# OpenAlex's identifier for arXiv as a source, used to keep results to preprints.
OPENALEX_ARXIV_SOURCE = "S4306400194"

# arXiv asks automated clients to identify themselves and to point at a page
# describing the client, so a maintainer can be reached about its traffic.
USER_AGENT = (
    "isac-ai-paper-collector/2.0 (+https://github.com/alipourkarimi/ISAC_LLM)"
)

# Each category carries one query per backend: arXiv uses fielded prefixes,
# OpenAlex searches title and abstract, so the syntax differs.
CATEGORIES = [
    {
        "heading": "Large Language Models (LLMs)",
        "arxiv": 'all:"integrated sensing and communication" AND '
                 '(all:"large language model" OR all:LLM)',
        "openalex": '"integrated sensing and communication" AND '
                    '("large language model" OR "LLM")',
    },
    {
        "heading": "Generative AI / Diffusion Models",
        "arxiv": 'all:"integrated sensing and communication" AND '
                 '(all:"generative AI" OR all:"diffusion model")',
        "openalex": '"integrated sensing and communication" AND '
                    '("generative AI" OR "diffusion model")',
    },
    {
        "heading": "Reinforcement Learning",
        "arxiv": 'all:"integrated sensing and communication" AND '
                 'all:"reinforcement learning"',
        "openalex": '"integrated sensing and communication" AND '
                    '"reinforcement learning"',
    },
    {
        "heading": "Deep Learning",
        "arxiv": 'all:"integrated sensing and communication" AND '
                 'all:"deep learning"',
        "openalex": '"integrated sensing and communication" AND "deep learning"',
    },
    {
        "heading": "Federated Learning",
        "arxiv": 'all:"integrated sensing and communication" AND '
                 'all:"federated learning"',
        "openalex": '"integrated sensing and communication" AND '
                    '"federated learning"',
    },
    {
        "heading": "Semantic Communication",
        "arxiv": 'all:"integrated sensing and communication" AND '
                 'all:"semantic communication"',
        "openalex": '"integrated sensing and communication" AND '
                    '"semantic communication"',
    },
    {
        "heading": "Wireless Foundation Models",
        "arxiv": 'all:"integrated sensing and communication" AND '
                 '(all:"foundation model" OR all:"multimodal sensing")',
        "openalex": '"integrated sensing and communication" AND '
                    '("foundation model" OR "multimodal sensing")',
    },
    {
        "heading": "Agentic AI",
        "arxiv": 'all:"integrated sensing and communication" AND '
                 '(all:"agentic AI" OR all:"AI agent")',
        "openalex": '"integrated sensing and communication" AND '
                    '("agentic AI" OR "AI agent")',
    },
]


def fetch(url: str, attempts: int = 4) -> bytes:
    """GET a URL, retrying transient failures with exponential backoff."""
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json,application/atom+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as error:
            # A 4xx other than 429 means the request itself is wrong; retrying
            # it would just repeat the same mistake.
            fatal = (
                isinstance(error, urllib.error.HTTPError)
                and 400 <= error.code < 500
                and error.code != 429
            )
            if fatal or attempt == attempts:
                raise
            backoff = 2**attempt
            print(f"    attempt {attempt} failed ({error}); retrying in {backoff}s")
            time.sleep(backoff)
    raise RuntimeError("unreachable")


def search_arxiv(query: str, max_results: int) -> list[dict]:
    """Query the arXiv API and return parsed entries."""
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    feed = ET.fromstring(fetch(f"{ARXIV_URL}?{params}"))

    papers = []
    for entry in feed.findall(f"{ATOM}entry"):
        link = entry.findtext(f"{ATOM}id", default="")
        papers.append(
            {
                "id": link.rsplit("/", 1)[-1],
                "title": " ".join(entry.findtext(f"{ATOM}title", default="").split()),
                "authors": [
                    author.findtext(f"{ATOM}name", default="")
                    for author in entry.findall(f"{ATOM}author")
                ],
                "published": entry.findtext(f"{ATOM}published", default="")[:10],
                "summary": " ".join(entry.findtext(f"{ATOM}summary", default="").split()),
                "link": link,
            }
        )
    return papers


def _reconstruct_abstract(inverted_index: dict | None) -> str:
    """Rebuild plain text from OpenAlex's {word: [positions]} abstract format."""
    if not inverted_index:
        return ""
    positions: list[tuple[int, str]] = []
    for word, indices in inverted_index.items():
        positions.extend((index, word) for index in indices)
    return " ".join(word for _, word in sorted(positions))


def _arxiv_id_from(work: dict) -> str:
    """Pull an arXiv identifier out of an OpenAlex work, if it has one."""
    location = work.get("primary_location") or {}
    landing = location.get("landing_page_url") or ""
    if "arxiv.org/abs/" in landing:
        return landing.rsplit("/", 1)[-1]
    doi = (work.get("ids") or {}).get("doi") or ""
    marker = "arxiv."
    if marker in doi.lower():
        return doi.lower().rsplit(marker, 1)[-1]
    return work.get("id", "").rsplit("/", 1)[-1]


def search_openalex(query: str, max_results: int) -> list[dict]:
    """Query OpenAlex for arXiv-hosted works and return parsed entries."""
    params = urllib.parse.urlencode(
        {
            "filter": (
                f"title_and_abstract.search:{query},"
                f"primary_location.source.id:{OPENALEX_ARXIV_SOURCE}"
            ),
            "sort": "publication_date:desc",
            "per-page": max_results,
        }
    )
    payload = json.loads(fetch(f"{OPENALEX_URL}?{params}"))

    papers = []
    for work in payload.get("results", []):
        authors = [
            (entry.get("author") or {}).get("display_name", "")
            for entry in work.get("authorships", [])
        ]
        location = work.get("primary_location") or {}
        papers.append(
            {
                "id": _arxiv_id_from(work),
                "title": " ".join((work.get("title") or "Untitled").split()),
                "authors": [name for name in authors if name],
                "published": work.get("publication_date", ""),
                "summary": _reconstruct_abstract(work.get("abstract_inverted_index"))
                or "_No abstract available._",
                "link": location.get("landing_page_url") or work.get("id", ""),
            }
        )
    return papers


def search(category: dict, max_results: int, source: str) -> tuple[list[dict], str]:
    """Fetch one category, returning its papers and the backend that served them."""
    if source in ("auto", "arxiv"):
        try:
            return search_arxiv(category["arxiv"], max_results), "arXiv"
        except Exception as error:  # noqa: BLE001 - fall back to the other backend
            if source == "arxiv":
                raise
            print(f"    arXiv unavailable ({error}); falling back to OpenAlex")
    return search_openalex(category["openalex"], max_results), "OpenAlex"


def format_markdown(
    results: dict[str, list[dict]], failures: dict[str, str], sources: set[str]
) -> str:
    origin = " and ".join(sorted(sources)) if sources else "no source"
    lines = [
        "# ISAC + AI papers on arXiv",
        "",
        f"Generated on {time.strftime('%Y-%m-%d')} via {origin}.",
    ]
    if failures:
        lines += [
            "",
            f"> **Warning:** {len(failures)} of {len(CATEGORIES)} searches failed on "
            "this run; those sections show the error instead of results.",
        ]
    for category in CATEGORIES:
        heading = category["heading"]
        lines += ["", f"## {heading}", ""]
        if heading in failures:
            lines.append(f"_Search failed: {failures[heading]}_")
            continue
        papers = results.get(heading, [])
        if not papers:
            lines.append("_No results returned._")
        for paper in papers:
            first_authors = ", ".join(paper["authors"][:3])
            if len(paper["authors"]) > 3:
                first_authors += " et al."
            lines += [
                f"### [{paper['title']}]({paper['link']})",
                "",
                f"- **arXiv:** {paper['id']} · {paper['published']} · {first_authors}",
                "",
                f"> {paper['summary']}",
                "",
            ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--max-results", type=int, default=10,
                        help="results per category (default: 10)")
    parser.add_argument("-o", "--output", help="write markdown to this file")
    parser.add_argument("--source", choices=("auto", "arxiv", "openalex"),
                        default="auto",
                        help="backend to query (default: arXiv, then OpenAlex)")
    args = parser.parse_args()

    results: dict[str, list[dict]] = {}
    failures: dict[str, str] = {}
    sources: set[str] = set()
    for index, category in enumerate(CATEGORIES):
        heading = category["heading"]
        print(f"Searching: {heading} ...")
        try:
            papers, source = search(category, args.max_results, args.source)
            results[heading] = papers
            sources.add(source)
            print(f"    {len(papers)} result(s) from {source}")
        except Exception as error:  # noqa: BLE001 - one bad query must not sink the run
            print(f"    FAILED: {error}")
            failures[heading] = str(error)
        # API etiquette: no more than one request every 3 seconds.
        if index < len(CATEGORIES) - 1:
            time.sleep(3)

    # Every search failing means both backends are unreachable. Publishing an
    # empty report would quietly erase a working one, so stop instead.
    if len(failures) == len(CATEGORIES):
        print("\nAll searches failed; leaving the existing report untouched.")
        return 1

    markdown = format_markdown(results, failures, sources)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(markdown)
        print(f"Wrote {args.output}")
    else:
        print()
        print(markdown)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Search arXiv for Integrated Sensing and Communication (ISAC) + AI papers.

Queries the official arXiv API (https://info.arxiv.org/help/api/index.html)
for several AI-technique categories (LLMs, generative AI, reinforcement
learning, deep learning) and prints the results as markdown.

Usage:
    python fetch_arxiv_isac.py                 # print to stdout
    python fetch_arxiv_isac.py -o report.md    # write to a file
    python fetch_arxiv_isac.py -n 20           # 20 results per category

Only the standard library is used — no packages to install.
"""

import argparse
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

API_URL = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"

# arXiv asks automated clients to identify themselves and to point at a page
# describing the client, so a maintainer can be reached about its traffic.
USER_AGENT = (
    "isac-ai-paper-collector/1.1 (+https://github.com/alipourkarimi/ISAC_LLM)"
)

# Each category: (heading, arXiv fielded search query)
CATEGORIES = [
    (
        "Large Language Models (LLMs)",
        'all:"integrated sensing and communication" AND '
        '(all:"large language model" OR all:LLM)',
    ),
    (
        "Generative AI / Diffusion Models",
        'all:"integrated sensing and communication" AND '
        '(all:"generative AI" OR all:"diffusion model")',
    ),
    (
        "Reinforcement Learning",
        'all:"integrated sensing and communication" AND '
        'all:"reinforcement learning"',
    ),
    (
        "Deep Learning",
        'all:"integrated sensing and communication" AND all:"deep learning"',
    ),
    (
        "Federated Learning",
        'all:"integrated sensing and communication" AND '
        'all:"federated learning"',
    ),
    (
        "Semantic Communication",
        'all:"integrated sensing and communication" AND '
        'all:"semantic communication"',
    ),
    (
        "Wireless Foundation Models",
        'all:"integrated sensing and communication" AND '
        '(all:"foundation model" OR all:"multimodal sensing")',
    ),
]


def search_arxiv(query: str, max_results: int, attempts: int = 4) -> list[dict]:
    """Run one query against the arXiv API and return parsed entries.

    arXiv rejects requests that do not negotiate a content type (HTTP 406) and
    throttles clients that do not identify themselves, so send an explicit
    Accept header and a User-Agent naming this project. Transient failures
    (throttling, 5xx, timeouts) are retried with exponential backoff.
    """
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    request = urllib.request.Request(
        f"{API_URL}?{params}",
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/atom+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )

    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                feed = ET.fromstring(response.read())
            break
        except (urllib.error.URLError, ET.ParseError, TimeoutError) as error:
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
            print(f"  attempt {attempt} failed ({error}); retrying in {backoff}s")
            time.sleep(backoff)

    papers = []
    for entry in feed.findall(f"{ATOM}entry"):
        authors = [
            author.findtext(f"{ATOM}name", default="")
            for author in entry.findall(f"{ATOM}author")
        ]
        papers.append(
            {
                "id": entry.findtext(f"{ATOM}id", default="").rsplit("/", 1)[-1],
                "title": " ".join(entry.findtext(f"{ATOM}title", default="").split()),
                "authors": authors,
                "published": entry.findtext(f"{ATOM}published", default="")[:10],
                "summary": " ".join(entry.findtext(f"{ATOM}summary", default="").split()),
                "link": entry.findtext(f"{ATOM}id", default=""),
            }
        )
    return papers


def format_markdown(results: dict[str, list[dict]], failures: dict[str, str]) -> str:
    lines = [
        "# ISAC + AI papers on arXiv",
        "",
        f"Generated on {time.strftime('%Y-%m-%d')} via the arXiv API.",
    ]
    if failures:
        lines += [
            "",
            f"> **Warning:** {len(failures)} of {len(CATEGORIES)} searches failed on "
            "this run; those sections show the error instead of results.",
        ]
    for heading, _ in CATEGORIES:
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
    args = parser.parse_args()

    results: dict[str, list[dict]] = {}
    failures: dict[str, str] = {}
    for index, (heading, query) in enumerate(CATEGORIES):
        print(f"Searching arXiv: {heading} ...")
        try:
            results[heading] = search_arxiv(query, args.max_results)
        except Exception as error:  # noqa: BLE001 - one bad query must not sink the run
            print(f"  FAILED: {error}")
            failures[heading] = str(error)
        # arXiv API etiquette: no more than one request every 3 seconds.
        if index < len(CATEGORIES) - 1:
            time.sleep(3)

    # Every search failing means arXiv is unreachable or the API contract moved.
    # Publishing an empty report would quietly erase a working one, so stop.
    if len(failures) == len(CATEGORIES):
        print("\nAll searches failed; leaving the existing report untouched.")
        return 1

    markdown = format_markdown(results, failures)
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

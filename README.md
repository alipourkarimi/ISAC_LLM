# AI-Empowered Integrated Sensing and Communication (ISAC) — arXiv Research Collection

A curated collection of **39 arXiv papers** at the intersection of **Integrated Sensing
and Communication (ISAC)** and **Artificial Intelligence** — covering Large Language
Models (LLMs), Generative AI / diffusion models, (Deep) Reinforcement Learning, classical
Deep Learning, Federated Learning, Semantic Communication, and Wireless Foundation Models.

ISAC is a key enabling technology for 6G in which one waveform, one spectrum, and one
hardware platform serve **both** radar-style sensing (detection, localization, tracking)
and data communication. Because the joint design space is huge and hard to optimize with
closed-form methods, AI techniques have become the dominant research direction.

> Curated briefs last updated **2026-08-14** from arXiv searches. Each brief is based on
> the paper's abstract and public metadata — always read the original paper before
> citing. For an unfiltered, always-current feed see
> [`latest-arxiv-report.md`](latest-arxiv-report.md), regenerated weekly by CI.

---

## Repository structure

| File | Contents |
|---|---|
| [`papers/01-llm-for-isac.md`](papers/01-llm-for-isac.md) | Large Language Models for ISAC |
| [`papers/02-generative-ai-for-isac.md`](papers/02-generative-ai-for-isac.md) | Generative AI & diffusion models for ISAC |
| [`papers/03-reinforcement-learning-for-isac.md`](papers/03-reinforcement-learning-for-isac.md) | (Deep) Reinforcement Learning for ISAC |
| [`papers/04-deep-learning-for-isac.md`](papers/04-deep-learning-for-isac.md) | Deep learning, surveys & tutorials for ISAC |
| [`papers/05-federated-learning-and-semantic-isac.md`](papers/05-federated-learning-and-semantic-isac.md) | Federated learning & semantic communication for ISAC |
| [`papers/06-foundation-models-for-isac.md`](papers/06-foundation-models-for-isac.md) | Multimodal wireless foundation models for ISAC (2025–2026) |
| [`scripts/fetch_arxiv_isac.py`](scripts/fetch_arxiv_isac.py) | Python script that re-runs the arXiv search so the collection can be refreshed |
| [`.github/workflows/update-papers.yml`](.github/workflows/update-papers.yml) | Weekly GitHub Action that refreshes [`latest-arxiv-report.md`](latest-arxiv-report.md) automatically |

## Paper index

| # | arXiv ID | Title (short) | AI technique |
|---|---|---|---|
| 1 | [2410.05062](https://arxiv.org/abs/2410.05062) | LLM-based multi-objective optimization for ISAC UAV networks | LLM + evolutionary optimization |
| 2 | [2502.06877](https://arxiv.org/abs/2502.06877) | WirelessGPT: generative pre-trained multi-task wireless model | Wireless foundation model |
| 3 | [2401.07764](https://arxiv.org/abs/2401.07764) | LLM agents meet 6G networks | LLM agents / edge AI |
| 4 | [2505.22320](https://arxiv.org/abs/2505.22320) | Chain-of-Thought for LLM-empowered wireless | LLM reasoning (CoT) |
| 5 | [2604.10256](https://arxiv.org/abs/2604.10256) | Graph-enhanced LLM for SWAN-ISAC | GNN + LLM (LoRA) |
| 6 | [2502.12622](https://arxiv.org/abs/2502.12622) | GenAI data augmentation for wireless sensing in ISAC | Conditional diffusion |
| 7 | [2408.11398](https://arxiv.org/abs/2408.11398) | GenAI-based secure wireless sensing (DFSS) | Diffusion models |
| 8 | [2506.06942](https://arxiv.org/abs/2506.06942) | Conditional denoising diffusion for cell-free 6G channel estimation | Diffusion + transformer |
| 9 | [2406.00408](https://arxiv.org/abs/2406.00408) | Optimizing 6G ISAC via expert networks | Mixture-of-experts + GenAI |
| 10 | [2510.25496](https://arxiv.org/abs/2510.25496) | Dynamic beamforming & power allocation via DRL | Deep RL |
| 11 | [2506.18560](https://arxiv.org/abs/2506.18560) | Digital-twin-assisted DRL beam selection (cell-free massive MIMO) | Deep RL + digital twin |
| 12 | [2508.19566](https://arxiv.org/abs/2508.19566) | Energy-efficient learning-based beamforming for ISAC V2X | Deep RL |
| 13 | [2405.20168](https://arxiv.org/abs/2405.20168) | Aerial RIS-assisted ISAC with DRL | Deep RL |
| 14 | [2412.01077](https://arxiv.org/abs/2412.01077) | Memory-based RL for ISAC | Recurrent / memory RL |
| 15 | [2509.06968](https://arxiv.org/abs/2509.06968) | DL techniques for ISAC: state of the art (survey) | Survey |
| 16 | [2504.13363](https://arxiv.org/abs/2504.13363) | AI-empowered ISAC (tutorial) | Tutorial (SL/UL/RL) |
| 17 | [2307.15074](https://arxiv.org/abs/2307.15074) | ISAC-NET: model-driven DL for passive sensing + communication | Model-driven DL |
| 18 | [2403.01480](https://arxiv.org/abs/2403.01480) | DL-based design of uplink ISAC | Deep learning |
| 19 | [2402.09439](https://arxiv.org/abs/2402.09439) | DL channel estimation for IRS-assisted ISAC | DNNs |
| 20 | [2509.21118](https://arxiv.org/abs/2509.21118) | Neural ISAC for the MIMO-OFDM downlink | Neural signal processing |
| 21 | [2509.02137](https://arxiv.org/abs/2509.02137) | High-resolution sensing in communication-centric ISAC | DL + parametric methods |
| 22 | [2508.15185](https://arxiv.org/abs/2508.15185) | ISCC for over-the-air federated edge learning | Federated learning + AirComp |
| 23 | [2306.02990](https://arxiv.org/abs/2306.02990) | ISCC for UAV-assisted federated edge learning | Federated learning |
| 24 | [2512.03374](https://arxiv.org/abs/2512.03374) | Vertical federated edge learning in edge perception networks | Vertical federated learning |
| 25 | [2603.15783](https://arxiv.org/abs/2603.15783) | Multi-objective OTA-FEEL for collaborative ISAC | Federated learning + MOO |
| 26 | [2503.08726](https://arxiv.org/abs/2503.08726) | SIMAC: semantic-driven multimodal sensing & communication | ViT + cross-attention |
| 27 | [2504.07656](https://arxiv.org/abs/2504.07656) | ISCSC with fluid antenna for metaverse | Semantic communication |
| 28 | [2506.00522](https://arxiv.org/abs/2506.00522) | ISCSC for vehicular networks | Semantic communication + transformer |
| 29 | [2409.20453](https://arxiv.org/abs/2409.20453) | E-healthcare ISCSC with physical-layer security | Semantic communication + PLS |
| 30 | [2506.05637](https://arxiv.org/abs/2506.05637) | Joint user association & beamforming for ISAC with LLMs | LLM + convex optimization |
| 31 | [2503.10432](https://arxiv.org/abs/2503.10432) | BeamLLM: vision-empowered mmWave beam prediction | LLM + vision |
| 32 | [2607.16269](https://arxiv.org/abs/2607.16269) | LLM-driven agent compilers for ISAC networks | LLM agents / intent-based |
| 33 | [2506.22507](https://arxiv.org/abs/2506.22507) | Unified cloud-edge-terminal multimodal ISAC | Distributed large models |
| 34 | [2511.12305](https://arxiv.org/abs/2511.12305) | MMSense: vision foundation model for wireless sensing | Multimodal foundation model |
| 35 | [2604.18255](https://arxiv.org/abs/2604.18255) | WiFo-MiSAC: wireless foundation model (SoM) | Self-supervised foundation model |
| 36 | [2512.23897](https://arxiv.org/abs/2512.23897) | WMFM: vision + communication foundation model for 6G ISAC | Contrastive learning |
| 37 | [2602.04016](https://arxiv.org/abs/2602.04016) | Multi-modal foundational model for communication & sensing | Physics-grounded foundation model |
| 38 | [2606.06239](https://arxiv.org/abs/2606.06239) | Foundation models for wireless: PHY intelligence → autonomy | Survey |
| 39 | [2606.20583](https://arxiv.org/abs/2606.20583) | Physical-AI: channel awareness → environmental intelligence | Vision paper |

## Key takeaways across the literature

1. **LLMs are moving from "chatbot" to "optimizer/controller"** — recent work uses LLMs
   as search operators inside evolutionary algorithms, as multimodal reasoners over CSI,
   and as network-management agents, rather than only as language interfaces.
2. **Diffusion models are the workhorse of generative ISAC** — used for channel/CSI data
   augmentation, secure sensing, and channel estimation, where their ability to model
   complex high-dimensional distributions beats GAN/VAE baselines.
3. **DRL dominates real-time resource allocation** — beamforming, power allocation, beam
   selection and RIS/trajectory control are naturally sequential decision problems;
   papers consistently report orders-of-magnitude faster inference than convex/SDR
   solvers at a modest performance gap.
4. **Digital twins and model-driven DL narrow the sim-to-real gap** — pure black-box
   learning is giving way to hybrid designs that embed known signal-processing structure
   (ISAC-NET) or train against a synchronized virtual replica of the network.
5. **ISAC is expanding into ISCC/ISCSC** — federated edge learning adds *computation* as
   a third co-designed resource, and semantic communication replaces bit pipes with
   meaning pipes; the newest papers co-optimize sensing, communication, computation, and
   security together.
6. **2026's pivot: multimodal wireless foundation models** — the field is moving from a
   network-per-task to *pre-train once, fine-tune many*, and from RF-only to RF + vision
   + LiDAR aligned in one embedding space via self-supervised or contrastive objectives
   that require no labels. Two strategies compete: adapt an existing vision foundation
   model, or pre-train natively on tokenized wireless signals.
7. **The best LLM results are hybrid, not end-to-end** — across the strongest papers the
   LLM takes the discrete, semantic, or few-shot part of the problem (user association,
   beam selection from imagery, intent parsing) while convex solvers keep the continuous
   optimization. Pure "ask the LLM to design the system" approaches do not lead.

## Refreshing this collection

```bash
python scripts/fetch_arxiv_isac.py            # print latest results to stdout
python scripts/fetch_arxiv_isac.py -o out.md  # write a fresh markdown report
```

The script queries the official [arXiv API](https://info.arxiv.org/help/api/index.html)
(`export.arxiv.org/api/query`) for each AI-technique category and formats the results as
markdown. arXiv asks automated clients to stay under 1 request / 3 seconds — the script
respects that.

# Deep Learning for ISAC — Surveys, Tutorials, and Core Designs

Beyond LLMs, GenAI, and RL, a large body of ISAC work applies "classical" deep learning:
DNN receivers that demodulate data *and* estimate targets, learned channel estimators,
and end-to-end neural transceivers. This file collects the main surveys/tutorials (start
here if you're new) and representative technical designs.

---

## Surveys & tutorials

### 1. Deep Learning-based Techniques for Integrated Sensing and Communication Systems: State-of-the-Art, Challenges, and Opportunities

- **arXiv:** [2509.06968](https://arxiv.org/abs/2509.06968) · Sep 2025 · eess.SP

**Brief.** A comprehensive survey of DL across the ISAC stack. Covers, among others:
fully connected DNN receivers that demodulate communication symbols while simultaneously
processing the received signal for sensing, and ISAC receivers whose neural networks
jointly demodulate data and estimate target **range and velocity under hardware
imperfections** (where model-based methods degrade). Ends with a challenges/opportunities
roadmap: datasets, generalization across environments, and complexity at the edge.

**Recommended as the entry-point survey for this collection.**

### 2. AI-Empowered Integrated Sensing and Communications

- **arXiv:** [2504.13363](https://arxiv.org/abs/2504.13363) · Apr 2025 · eess.SP

**Brief.** A tutorial-style treatment of AI for the two central physical-layer design
problems of ISAC: **waveform design** and **beamforming**. Systematically walks through
supervised, unsupervised, and reinforcement-learning approaches to each, comparing them
against optimization-based designs, and identifying when learning genuinely helps
(non-convexity, imperfect models, real-time constraints) versus when classical methods
remain preferable.

---

## Technical designs

### 3. ISAC-NET: Model-driven Deep Learning for Integrated Passive Sensing and Communication

- **arXiv:** [2307.15074](https://arxiv.org/abs/2307.15074) · Jul 2023 · eess.SP

**Brief.** Instead of a black-box network, ISAC-NET is **model-driven**: it unfolds the
known signal-processing pipeline into learnable blocks — a passive-sensing module, a
signal-detection module, and a channel-reconstruction module — processed block by block.
It outputs **passive sensing results and demodulated communication symbols
simultaneously**, showing better sensing accuracy than traditional passive sensing at
comparable/better demodulation performance.

**Why it matters:** the model-driven (deep-unfolding) philosophy keeps physical
interpretability and needs far less training data than end-to-end black boxes.

### 4. Deep Learning-based Design of Uplink Integrated Sensing and Communication

- **arXiv:** [2403.01480](https://arxiv.org/abs/2403.01480) · Mar 2024 · eess.SP

**Brief.** Addresses the less-studied **uplink** ISAC setting, where the base station
must decode user data while sensing from the same received signals. Proposes DL-based
receiver designs that handle the interference between the two roles, outperforming
conventional separated processing, and analyzes the achievable
communication–sensing operating points.

### 5. Deep-Learning-Based Channel Estimation for IRS-Assisted ISAC System

- **arXiv:** [2402.09439](https://arxiv.org/abs/2402.09439) · Feb 2024 · eess.SP

**Brief.** In an intelligent-reflecting-surface (IRS)-assisted ISAC system, the cascaded
channels (BS→IRS→user/target) are high-dimensional and hard to estimate. The paper
builds a **deep-learning estimation framework with two DNN architectures** tailored to
different propagation environments, estimating the sensing and communication channels
and beating least-squares/traditional baselines, especially at low SNR.

### 6. Neural Integrated Sensing and Communication for the MIMO-OFDM Downlink

- **arXiv:** [2509.21118](https://arxiv.org/abs/2509.21118) · Sep 2025 · eess.SP

**Brief.** Presents a signal-processing framework for **neural ISAC in MIMO-OFDM
downlink** systems — the waveform family used by 5G/6G. Data-driven components are
inserted into the transceiver chain so that one learned design serves both the
communication link and the sensing function over standard OFDM signals, keeping
compatibility with existing air interfaces.

### 7. High-Resolution Sensing in Communication-Centric ISAC: Deep Learning and Parametric Methods

- **arXiv:** [2509.02137](https://arxiv.org/abs/2509.02137) · Sep 2025 · eess.SP

**Brief.** Communication-centric ISAC reuses communication waveforms (like OFDM) for
sensing, which limits resolution. This work compares and combines **parametric
(model-based super-resolution) methods with deep learning** to push sensing resolution
beyond classical FFT-based processing, characterizing when learned methods beat
parametric estimators and proposing hybrid pipelines.

---

### 8. Short-Length Code Designs for ISAC: A Deep Learning Approach

- **arXiv:** [2609.33605](https://arxiv.org/abs/2609.33605) · Sep 2026 · eess.SP

**Brief.** Opens a part of the stack the rest of this collection leaves alone: **channel
coding**. In the **short blocklength** regime the communication/sensing trade-off is at
its sharpest, and the usual asymptotic intuitions do not apply. The paper derives a
modified Cramér-Rao bound for multi-target delay estimation and analyzes the
maximum-likelihood decoding rule for **noncoherent** communication under correlated
fading, using both to expose the structural connections between the two objectives. An
**autoencoder** then learns waveform representations optimizing both, with a tunable
parameter setting where on the trade-off to sit. It beats conventional schemes on
reliability *and* sensing accuracy, most clearly at short blocklength under fading.

**Why it matters:** most learned ISAC work optimizes beams and power over a fixed
waveform family; this learns the code itself, in the regime where closed-form design is
weakest.

### 9. Predictive Beamforming via Echo-Beam Modality Separation with Cross-Attention

- **arXiv:** [2610.09429](https://arxiv.org/abs/2610.09429) · Oct 2026 · eess.SP

**Brief.** In V2I networks, sensing echoes can predict where a beam should point next.
The design point worth noting is **negative evidence against naive fusion**: echoes and
historical beamformers are pushed through **separate encoders** to preserve their
modality-specific character, and only then combined via **cross-attention**, which the
authors find exploits the two representations more effectively than concatenating inputs.
GRUs capture dependence across time slots. Training uses a penalty-based unconstrained
surrogate for sum-spectral-efficiency maximization under a sensing SINR constraint.

**Why it matters:** a concrete architectural finding — *when* you fuse modalities matters
as much as *that* you fuse them, echoing the separate-encoder pattern in SIMAC and the
radio-echo work in file 06.

### 10. Robust Resource Allocation for STAR-RIS-Assisted ISAC Networks Using Deep Learning

- **arXiv:** [2610.25798](https://arxiv.org/abs/2610.25798) · Oct 2026 · eess.SP

**Brief.** A simultaneously transmitting and reflecting RIS serves users on both sides of
the surface, which makes the joint resource problem coupled and non-convex. Prior
iterative optimizers assume **accurate global channel information and ideal phase
shifts** — assumptions that break in deployment. This **model-driven** deep learning
framework jointly optimizes transmit beamforming, waveform, and the STAR-RIS
reflection/transmission coefficient matrices by minimizing a weighted sum of
**multi-user interference energy** (communication) and **CRLB** (sensing), at low
overhead and explicitly **under imperfect channel information**.

**Why it matters:** the robustness framing is the contribution — it targets the gap
between what iterative optimizers assume and what a real deployment can measure.

---

### Category takeaway

The DL-for-ISAC literature is converging on **hybrid designs**: embed the known physics
(OFDM structure, array manifolds, estimation pipelines) and let neural networks handle
what models get wrong (hardware impairments, complex clutter, non-convex couplings).
Pure end-to-end black boxes are increasingly rare outside benchmark studies.

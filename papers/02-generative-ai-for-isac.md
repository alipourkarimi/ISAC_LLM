# Generative AI & Diffusion Models for ISAC

Generative models — above all **denoising diffusion models** — are used in ISAC to
*synthesize* what is expensive to measure (labeled CSI/sensing data), to *reconstruct*
what is noisy or incomplete (channels), and to *hide* what should stay private (secure
sensing). Their strength is modeling complex, high-dimensional wireless data
distributions more stably than GANs.

---

## 1. Generative AI Enabled Robust Data Augmentation for Wireless Sensing in ISAC Networks

- **arXiv:** [2502.12622](https://arxiv.org/abs/2502.12622) · Feb 2025 · cs.LG / eess.SP

**Brief.** Wireless sensing models (e.g., human activity recognition from CSI) suffer
when training data is scarce and unevenly distributed across environments. This paper
trains a **conditioned diffusion model on limited CSI data** to generate new synthetic
samples, expanding dataset size, and uses a **second diffusion model to enhance sample
quality** — a two-stage generate-then-refine augmentation pipeline. The augmented
datasets significantly improve downstream sensing accuracy in ISAC networks with
insufficient measurements.

**Why it matters:** data scarcity is the #1 practical blocker for learned wireless
sensing; diffusion-based augmentation is emerging as the standard fix.

---

## 2. Generative AI based Secure Wireless Sensing for ISAC Networks

- **arXiv:** [2408.11398](https://arxiv.org/abs/2408.11398) · Aug 2024 · cs.CR / eess.SP

**Brief.** ISAC has a privacy dark side: anyone receiving the signals can potentially
"sense" people through walls. The proposed **DFSS** system uses two diffusion models to
make sensing *selective*: a **discrete conditional diffusion model generates graphs**
that guide the ISAC network in which wireless links/nodes to activate, so that authorized
sensing keeps working while the information leaked to eavesdroppers is scrambled.
Experiments show DFSS cuts the activity-recognition accuracy of **unauthorized** devices
by roughly **70%** while preserving legitimate sensing performance.

**Why it matters:** one of the first works to weaponize generative models *for defense* —
protecting physical privacy in sensing-capable networks.

---

## 3. Conditional Denoising Diffusion for ISAC-Enhanced Channel Estimation in Cell-Free 6G

- **arXiv:** [2506.06942](https://arxiv.org/abs/2506.06942) · Jun 2025 · eess.SP

**Brief.** In cell-free 6G (many distributed access points, no cells), channel estimation
is hard but sensing information about the environment is available "for free" from ISAC.
This paper feeds that sensing information into a **Conditional Denoising Diffusion Model
(CDDM)** combined with a **Multimodal Transformer**: the diffusion model learns to
denoise/reconstruct the channel conditioned on sensing observations, and the transformer
fuses the modalities. Result: better channel estimates than sensing-blind estimators,
i.e., a concrete demonstration of the *sensing-helps-communication* half of the ISAC
promise.

**Why it matters:** most ISAC papers optimize a trade-off; this one shows the synergy —
sensing data actively improving a core communication task.

---

## 4. Optimizing 6G Integrated Sensing and Communications (ISAC) via Expert Networks

- **arXiv:** [2406.00408](https://arxiv.org/abs/2406.00408) · Jun 2024 · eess.SP / cs.AI

**Brief.** Proposes an **expert-network (mixture-of-experts style) architecture** for 6G
ISAC optimization, in which specialized modules handle different sub-problems and signal
types. The pipeline processes downlink signals with a mix of classical tools (e.g., FFT
feature extraction) and **generative diffusion models**, routing tasks to the right
expert. It illustrates a pragmatic pattern: don't ask one monolithic model to do all of
ISAC — compose classical DSP experts with generative experts.

**Why it matters:** an early template for modular "AI-native" ISAC stacks combining
signal processing and GenAI components.

---

## 5. RadioVIL: Anomaly-Aware Diffusion Models for Radio Map Inpainting and Zero-Shot Vehicle Localization

- **arXiv:** [2608.16167](https://arxiv.org/abs/2608.16167) · Aug 2026 · eess.SP

**Brief.** Identifies a failure mode that matters for any generative approach to sensing:
treating radio-map construction as **pure image completion** produces over-smoothed
reconstructions that **erase the high-frequency scattering signatures** of the very things
you want to detect, such as hidden vehicles. The fix is to reformulate inpainting and
localization as a **prior-guided physical inverse problem**. A DDPM first learns the
environment's structural prior; at inference from sparse measurements, a Diffusion-based
Mediating Intermediate Layer Optimization (DMILO) step optimizes an L1-regularized sparse
deviation term to **isolate scattering anomalies layer by layer**, without unfolding the
whole denoising chain.

Conventional reconstruction baselines fail to detect hidden vehicles at all, and a
zero-shot diffusion baseline manages only limited detection because it forces semantic
harmonization. RadioVIL preserves authentic physical texture (best LPIPS 0.0587) and
unlocks **zero-shot localization from sparse radio maps** at 75.20% recall and 3.31 m
average error.

**Why it matters:** a concrete warning that generative priors can smooth away exactly the
anomaly the sensing task exists to find — and a method that keeps the anomaly by treating
it as a residual rather than something to reconcile.

---

### Category takeaway

Diffusion models have displaced GANs as the default generative tool in ISAC work
(2024→2026), for three jobs: data augmentation, conditional reconstruction/estimation,
and privacy protection. The recurring open issues are inference latency of iterative
denoising (a problem for real-time radio) and validating that synthetic CSI is
physically consistent, not just visually plausible.

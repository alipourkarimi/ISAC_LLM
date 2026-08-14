# Wireless Foundation Models for ISAC

The fastest-moving direction of 2026. Rather than training a network per task, these
works pre-train a **single large model on wireless data** — channel measurements, radar
returns, LiDAR, imagery — usually self-supervised, then fine-tune it for many downstream
sensing and communication tasks. This is the model-level expression of the ISAC idea:
one representation serving both functions, exactly as one waveform serves both at the
physical layer.

A recurring theme is **multimodality**: radio-only sensing is being replaced by designs
that align RF with vision and LiDAR in a shared embedding space, because cameras and
channels observe the same physical scene.

---

## 1. MMSense: Adapting Vision-based Foundation Models for Multi-task Multi-modal Wireless Sensing

- **arXiv:** [2511.12305](https://arxiv.org/abs/2511.12305) · Nov 2025 · eess.SP / cs.CV

**Brief.** Rather than pre-training from scratch, MMSense **adapts an existing
vision foundation model** to wireless sensing by converting each modality — image,
radar, LiDAR, and text — into vision-compatible representations so they align inside one
feature space. One model then covers three task families that are usually studied
separately: **channel-centric** (e.g., estimation/prediction), **environment-aware**
(mapping, localization), and **human-centered** sensing (activity, presence).

**Why it matters:** reuses the enormous investment already sunk into vision foundation
models instead of demanding wireless-scale pre-training data that does not yet exist.

---

## 2. WiFo-MiSAC: A Wireless Foundation Model for Multimodal Sensing and Communication Integration via Synesthesia of Machines

- **arXiv:** [2604.18255](https://arxiv.org/abs/2604.18255) · Apr 2026 · eess.SP

**Brief.** A **task-agnostic** foundation model that **tokenizes heterogeneous signals
into a unified token space** and pre-trains over them self-supervised — the wireless
analogue of how LLMs tokenize text. The "Synesthesia of Machines" framing treats
different sensors as different senses of one machine perceiving a single environment, so
sensing and communication tasks become downstream heads over shared tokens rather than
separate systems.

**Why it matters:** the tokenize-everything approach is what let language and vision
models scale; this is its clearest transfer to ISAC to date.

---

## 3. Wireless Multimodal Foundation Model (WMFM): Integrating Vision and Communication Modalities for 6G ISAC Systems

- **arXiv:** [2512.23897](https://arxiv.org/abs/2512.23897) · Dec 2025 · eess.SP

**Brief.** Jointly learns from **wireless channel coefficients and camera imagery** using
**contrastive learning** — the CLIP recipe applied to radio. Camera and channel
embeddings of the same scene are pulled together and mismatched pairs pushed apart, so
the model learns the correspondence **without explicit labels**. The resulting aligned
representation supports downstream 6G ISAC tasks such as vision-aided beam and blockage
prediction.

**Why it matters:** label-free training is the practical unlock — paired camera/channel
data can be collected automatically by any instrumented base station.

---

## 4. A Multi-Modal Foundational Model for Wireless Communication and Sensing

- **arXiv:** [2602.04016](https://arxiv.org/abs/2602.04016) · Feb 2026 · eess.SP

**Brief.** A task-agnostic multimodal foundation model whose distinguishing claim is that
its learned representations are **grounded in the physics of electromagnetic wave
propagation** rather than being purely statistical. Embedding propagation structure is
the proposed route to generalization across sites and deployments — the failure mode
that has dogged learned wireless models, which typically overfit the environment they
were trained in.

**Why it matters:** directly targets the generalization gap that keeps learned ISAC
models from transferring between real deployments.

---

## 5. Foundation Models for Wireless Communications: From PHY Intelligence to Network Autonomy

- **arXiv:** [2606.06239](https://arxiv.org/abs/2606.06239) · Jun 2026 · eess.SP

**Brief.** A survey/position paper tracing the arc from foundation models applied at the
**physical layer** (channel estimation, beam management, sensing) up to **autonomous
network operation**, with ISAC as a central use case. Useful as the map of this
sub-field: it organizes the rapidly multiplying "WirelessGPT / WiFo / MMSense"-style
models into a coherent taxonomy and identifies the shared open problems — data, scaling
laws for wireless, evaluation benchmarks.

**Recommended as the entry-point survey for this category.**

---

## 6. Physical-AI: From Channel Awareness to Environmental Intelligence in 6G Wireless Networks

- **arXiv:** [2606.20583](https://arxiv.org/abs/2606.20583) · Jun 2026 · eess.SP

**Brief.** Argues for a shift from networks that merely **know their channel** to networks
with **environmental intelligence** — an internal model of the physical world built from
integrated sensing, on which AI reasons and acts. ISAC is the sensory substrate for this
"Physical-AI" vision, and foundation models are the reasoning layer over it.

**Why it matters:** the clearest statement of where the field believes ISAC + AI is
ultimately heading: the network as an embodied perceiving agent.

---

### Category takeaway

Between late 2025 and mid 2026 the field pivoted from task-specific networks to
**pre-train-once, fine-tune-many** wireless foundation models, and from RF-only to
**multimodal** (RF + vision + LiDAR) designs trained with self-supervised or contrastive
objectives that need no labels. Two strategies are competing: **adapt** an existing
vision foundation model (MMSense) versus **pre-train** natively on tokenized wireless
signals (WiFo-MiSAC). The unresolved questions are whether wireless data exhibits
LLM-style scaling laws, and whether physics-grounded representations really deliver the
cross-site generalization that purely statistical ones have not.

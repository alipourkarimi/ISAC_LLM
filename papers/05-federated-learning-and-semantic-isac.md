# Federated Learning & Semantic Communication for ISAC

Two further AI directions round out the picture. **Federated edge learning (FEEL)**
treats the ISAC network itself as a distributed training system: devices sense locally,
train locally, and aggregate models over the air — turning "integrated sensing and
communication" into "integrated sensing, communication **and computation** (ISCC)".
**Semantic communication** transmits *meaning* instead of bits using learned
(transformer-based) encoders, and merges naturally with sensing into ISCSC frameworks.

---

## Federated / distributed learning

### 1. Integrated Sensing, Communication, and Computation for Over-the-Air Federated Edge Learning

- **arXiv:** [2508.15185](https://arxiv.org/abs/2508.15185) · Aug 2025 · eess.SP

**Brief.** An edge server coordinates multiple devices that **wirelessly sense objects
and collaboratively train a recognition model** via federated learning. Model updates
are aggregated with **over-the-air computation (AirComp)** — all devices transmit
simultaneously and the channel itself sums the gradients in one shot. The paper analyzes
convergence while accounting for the two ISAC-specific impairments: wireless sensing
noise in the training data and AirComp distortion in the aggregation.

**Why it matters:** the cleanest formulation of the full loop — sense over the air,
learn over the air — with a convergence guarantee.

### 2. Integrated Sensing, Computation, and Communication for UAV-assisted Federated Edge Learning

- **arXiv:** [2306.02990](https://arxiv.org/abs/2306.02990) · Jun 2023 · eess.SP

**Brief.** Uses a UAV as a mobile edge node for federated learning over ISAC: the UAV's
position affects both the quality of the sensing data collected (human-motion
recognition) and the communication links carrying model updates. The paper studies this
sensing-quality/communication trade-off and optimizes UAV deployment for training
performance.

### 3. Joint Sensing, Communication, and Computation for Vertical Federated Edge Learning in Edge Perception Networks

- **arXiv:** [2512.03374](https://arxiv.org/abs/2512.03374) · Dec 2025 · eess.SP

**Brief.** Extends the ISCC idea to **vertical** federated learning, where devices hold
different *features* of the same targets (different sensing views) rather than different
samples. Edge devices wirelessly sense objects and train a shared model under edge-server
coordination, again using AirComp for fast gradient aggregation — matching the
multi-view nature of distributed radar-like perception.

### 4. Multi-objective Optimization for Over-the-Air Federated Edge Learning-enabled Collaborative Integrated Sensing and Communications

- **arXiv:** [2603.15783](https://arxiv.org/abs/2603.15783) · Mar 2026 · eess.SP

**Brief.** (2026 paper — brief based on search-result metadata.) A multi-objective
framework for collaborative wireless sensing with over-the-air FEEL, enabling
**multi-task OTA aggregation** that handles sensing and learning objectives
simultaneously rather than optimizing one and constraining the other.

---

## Semantic communication (ISCSC)

### 5. SIMAC: A Semantic-Driven Integrated Multimodal Sensing And Communication Framework

- **arXiv:** [2503.08726](https://arxiv.org/abs/2503.08726) · Mar 2025 · eess.SP / cs.CV

**Brief.** Fuses multiple sensing modalities at the *semantic* level: a **vision
transformer (ViT)** extracts semantics from images while **complex-valued CNNs** extract
semantics from radio signals, and a **cross-attention** module fuses them into one
representation that serves both sensing and communication. Instead of shipping raw
samples, the network exchanges fused semantics — less bandwidth, more task accuracy.

### 6. Integrated Sensing, Computing, and Semantic Communication with Fluid Antenna for Metaverse

- **arXiv:** [2504.07656](https://arxiv.org/abs/2504.07656) · Apr 2025 · eess.SP

**Brief.** Targets metaverse applications, where huge sensory streams must reach
rendering servers with low latency. The proposed **ISCSC** framework transmits only
contextual/semantic information (drastically cutting data volume) and adds a **fluid
antenna** — a position-reconfigurable antenna — to give the physical layer extra degrees
of freedom for balancing sensing and semantic transmission.

### 7. Integrated Sensing, Computing and Semantic Communication for Vehicular Networks

- **arXiv:** [2506.00522](https://arxiv.org/abs/2506.00522) · Jun 2025 · eess.SP

**Brief.** Brings ISCSC to V2X: roadside units sense vehicles, extract semantic
descriptions of the traffic scene, and communicate those semantics under the roadside
unit's limited computing budget. Includes a **transformer-based estimator for the joint
semantic-communication-and-sensing channel** that cuts pilot overhead — the learned
encoder does double duty for channel knowledge and meaning extraction.

### 8. E-Healthcare Systems: Integrated Sensing, Computing, and Semantic Communication with Physical Layer Security

- **arXiv:** [2409.20453](https://arxiv.org/abs/2409.20453) · Sep 2024 · eess.SP

**Brief.** Applies ISCSC to e-healthcare, where the sensed data (patient monitoring) is
maximally privacy-sensitive. Combines semantic transmission of health features with
**physical-layer security** so that eavesdroppers can recover neither the raw sensing
data nor its semantic content, and analyzes the resulting security/efficiency trade-off.

---

### Category takeaway

These works push ISAC beyond a two-way trade-off into three- and four-way co-design:
sensing + communication + computation (+ security). The shared toolbox is AirComp for
aggregation, transformers for semantic extraction, and multi-objective optimization for
the enlarged design space. Expect "ISCC/ISCSC" to appear increasingly often as the
successor acronym to ISAC in 2026+ literature.

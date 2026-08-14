# Large Language Models (LLMs) for ISAC

LLMs enter ISAC research in three roles: as **optimizers** (steering search/evolutionary
algorithms with in-context reasoning), as **multimodal perceivers** (fusing CSI, radar
returns, and vision for beam prediction or target recognition), and as **network agents**
(autonomous management of 6G resources). Foundation models trained directly on wireless
channel data ("wireless GPTs") are an emerging fourth direction.

---

## 1. Large Language Model Based Multi-Objective Optimization for Integrated Sensing and Communications in UAV Networks

- **arXiv:** [2410.05062](https://arxiv.org/abs/2410.05062) · Oct 2024 · eess.SY / cs.AI

**Brief.** Considers a UAV that simultaneously communicates with ground users and senses
targets (UAV-enabled ISAC). The joint design of UAV trajectory/deployment and transmit
beamforming is a multi-objective problem — communication rate vs. sensing performance
trade-off. The authors propose **LEDMA**, an LLM-enabled decomposition-based
multi-objective evolutionary algorithm: the problem is decomposed into scalar
sub-problems (MOEA/D style) and *LLMs act as the search operators*, driven by carefully
engineered prompts that inject the optimization context in-context. Results show LEDMA
outperforms standard multi-objective baselines and finds better Pareto fronts.

**Why it matters:** one of the first concrete demonstrations that off-the-shelf LLMs can
replace hand-designed crossover/mutation operators in ISAC network optimization.

---

## 2. WirelessGPT: A Generative Pre-trained Multi-task Learning Framework for Wireless Communication

- **arXiv:** [2502.06877](https://arxiv.org/abs/2502.06877) · Feb 2025 · eess.SP

**Brief.** Proposes a **wireless foundation model** pre-trained on large-scale wireless
channel data to learn a universal channel representation, then fine-tuned for multiple
downstream tasks — channel estimation, channel prediction, and **sensing tasks (e.g.,
human activity recognition)** within one model. This is one of the early attempts to
unify communication and sensing tasks inside a single generative pre-trained model,
which is exactly the ISAC vision at the model level: one representation serving both
functions. Reported gains over task-specific baselines grow with model size, suggesting
scaling laws carry over to wireless data.

**Why it matters:** points toward "one foundation model per network" instead of dozens of
task-specific neural networks — a natural AI counterpart to ISAC's hardware unification.

---

## 3. When Large Language Model Agents Meet 6G Networks: Perception, Grounding, and Alignment

- **arXiv:** [2401.07764](https://arxiv.org/abs/2401.07764) · Jan 2024 · cs.NI

**Brief.** A vision/framework paper on running **LLM agents split between mobile devices
and 6G edge servers** (small local model + large edge model). It maps the classic agent
loop — perception, grounding, alignment — onto 6G capabilities and argues that **ISAC is
the perception layer of LLM agents**: integrated sensing supplies the environmental
information (location, motion, surroundings) that agents need to ground their reasoning
in the physical world, while the communication half moves model context between device
and edge efficiently.

**Why it matters:** frames ISAC not just as a radio technique but as the "eyes and ears"
of future network-native AI agents.

---

## 4. Chain-of-Thought for Large Language Model-empowered Wireless Communications

- **arXiv:** [2505.22320](https://arxiv.org/abs/2505.22320) · May 2025 · eess.SP

**Brief.** Studies how **chain-of-thought (CoT) prompting** improves LLM performance on
wireless-domain problems, where naive prompting often fails because the tasks require
multi-step numerical and physical reasoning. The paper walks through wireless use cases
(including sensing/ISAC-flavored tasks) and shows that structured intermediate reasoning
steps substantially improve solution quality, positioning CoT as a cheap alternative to
fine-tuning for wireless problem solving.

**Why it matters:** practical guidance on *how* to prompt general-purpose LLMs for
ISAC/wireless engineering tasks rather than training new models.

---

## 5. Graph-Enhanced LLM for SWAN-ISAC

- **arXiv:** [2604.10256](https://arxiv.org/abs/2604.10256) · Apr 2026 · eess.SP

**Brief.** (2026 paper — brief based on search-result metadata.) Combines a **CSI-induced
self-graph neural network** with an **LLM backbone fine-tuned via LoRA** (low-rank
adaptation) to capture the interactions among communication users and sensing targets in
a space-water-air-network (SWAN) ISAC setting. The graph structure encodes who interferes
with / senses whom, and the LLM provides the sequence-modeling capacity, with LoRA keeping
the fine-tuning cost low.

**Why it matters:** shows the current frontier — hybrid GNN + LLM architectures applied
to multi-domain (space/air/water) ISAC networks.

---

## 6. Joint User Association and Beamforming Design for ISAC Networks with Large Language Models

- **arXiv:** [2506.05637](https://arxiv.org/abs/2506.05637) · Jun 2025 · eess.SP

**Brief.** Considers a **multi-base-station ISAC network** serving several ground users
while detecting several targets, and formulates joint user association + multi-BS
transmit beamforming to maximize sum rate subject to target detection and estimation
requirements. The key idea is a **division of labor**: the discrete, combinatorial user
association is handed to an LLM steered by **few-shot prompting, chain-of-thought, and
self-reflection**, while the continuous beamforming sub-problem stays with a classical
convex solver, the two alternating to convergence. With GPT-o1 driving the association
step, the algorithm converges quickly and lands near the performance upper bound.

**Why it matters:** a clean recipe for where LLMs actually add value in ISAC
optimization — discrete/combinatorial decisions that convex solvers handle badly — while
leaving the continuous math to tools that are already optimal at it.

---

## 7. BeamLLM: Vision-Empowered mmWave Beam Prediction with Large Language Models

- **arXiv:** [2503.10432](https://arxiv.org/abs/2503.10432) · Mar 2025 · eess.SP

**Brief.** mmWave links need the right narrow beam at the right instant, and scanning for
it burns overhead. BeamLLM predicts the beam from **camera imagery plus radio context**,
adapting an LLM as the cross-modal reasoning backbone over visual scene features. It
reports substantial accuracy and robustness gains over conventional deep-learning
predictors, and — the notable part — holds up in **few-shot** settings where task-specific
networks collapse for lack of training data.

**Why it matters:** the strongest evidence so far that an LLM's pretrained contextual
reasoning transfers to a physical-layer task, especially when labeled data is scarce.

---

## 8. From Intent to Infrastructure: LLM-Driven Agent Compilers for ISAC Networks

- **arXiv:** [2607.16269](https://arxiv.org/abs/2607.16269) · Jul 2026 · eess.SP / cs.NI

**Brief.** (Newest LLM entry in this collection.) Observes that AI-for-ISAC work almost
always optimizes one isolated subtask, leaving a gap between a human's **high-level
intent** ("track vehicles on this corridor while keeping user throughput above X") and a
**complete system configuration**. The paper proposes LLMs as **agent compilers**: the
model parses intent and compiles it down into a coordinated pipeline of ISAC agents and
concrete network parameters — effectively treating network configuration as a code
generation problem.

**Why it matters:** points at intent-based networking for ISAC, where the LLM is the
orchestration layer over many specialized components rather than a single-task solver.

---

## 9. A Unified Cloud-Edge-Terminal Framework for Multimodal Integrated Sensing and Communication

- **arXiv:** [2506.22507](https://arxiv.org/abs/2506.22507) · Jun 2025 · eess.SP

**Brief.** Addresses *where* large models should run in a multimodal ISAC system by
splitting work across the **cloud, edge, and terminal** tiers: lightweight processing of
sensing streams happens near the device, heavier multimodal reasoning is offloaded
upward, and the framework coordinates the hand-offs. It targets the practical blocker
named in nearly every LLM-ISAC paper — large-model latency at the network edge.

**Why it matters:** moves the conversation from "can an LLM do this?" to "where in the
network does it physically run?", which is what deployment actually turns on.

---

### Category takeaway

LLM-for-ISAC work is young but moving fast: 2024 papers used LLMs *around* the problem
(as optimizers or agents); 2025–2026 papers increasingly put wireless data *inside* the
model (foundation models, LoRA fine-tuning on CSI), and the newest work (2026) promotes
the LLM to an **orchestration layer** that compiles human intent into full network
configurations. A consistent pattern across the strongest results is *hybrid* design:
give the LLM the discrete, semantic, or few-shot part of the problem and leave the
continuous optimization to convex solvers. The open challenges repeatedly named are
hallucination in numeric tasks, latency of large models at the network edge (now being
answered by cloud-edge-terminal splits), and the lack of large public ISAC datasets for
pre-training.

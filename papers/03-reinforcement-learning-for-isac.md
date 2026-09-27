# (Deep) Reinforcement Learning for ISAC

Resource allocation in ISAC — beamforming, power splitting between sensing and
communication, beam/user selection, RIS phase control, UAV trajectories — is a
*sequential decision problem under uncertainty*, which is exactly what RL solves. The
consistent story across these papers: DRL reaches 80–95% of the optimum found by heavy
convex/SDR solvers while deciding in **milliseconds instead of seconds**, which is what
real-time radios actually need.

---

## 1. Dynamic Beamforming and Power Allocation in ISAC via Deep Reinforcement Learning

- **arXiv:** [2510.25496](https://arxiv.org/abs/2510.25496) · Oct 2025 · eess.SP

**Brief.** Jointly adapts transmit beamforming and power allocation in a dynamic ISAC
system using DRL, replacing the conventional semidefinite-relaxation (SDR) optimizer.
The trained agent converges within ~2,000 episodes and achieves up to **80% of the
spectral efficiency of the SDR benchmark**, but makes decisions in about **20 ms versus
~4,500 ms** for SDR — a >200× speedup that turns an offline optimization into something
deployable at frame timescales.

**Why it matters:** the clearest published quantification of the DRL trade: give up
~20% optimality, gain real-time operation.

---

## 2. Efficient Beam Selection for ISAC in Cell-Free Massive MIMO via Digital Twin-Assisted Deep Reinforcement Learning

- **arXiv:** [2506.18560](https://arxiv.org/abs/2506.18560) · Jun 2025 · eess.SP

**Brief.** In cell-free massive MIMO ISAC, many distributed access points must pick
beams that jointly serve users and illuminate sensing targets — a combinatorial search.
The paper formulates beam selection as a **Markov decision process** and trains a DRL
agent **inside a digital twin** of the network: the twin (a synchronized virtual replica
built from ray-tracing/site data) generates cheap training experience, so the agent
learns without degrading the live network, then transfers to the real system.

**Why it matters:** digital-twin-in-the-loop training is the leading answer to DRL's
"you can't let an untrained agent explore on a production network" problem.

---

## 3. Energy-Efficient Learning-Based Beamforming for ISAC-Enabled V2X Networks

- **arXiv:** [2508.19566](https://arxiv.org/abs/2508.19566) · Aug 2025 · eess.SP

**Brief.** Targets vehicle-to-everything (V2X) scenarios where roadside ISAC units track
vehicles (sensing) while serving them data (communication) under an **energy-efficiency**
objective rather than raw rate. A DRL algorithm jointly optimizes beamforming and power
allocation, adapting to fast vehicular channel dynamics; results show substantial energy
savings versus optimization baselines at comparable sensing/communication quality.

**Why it matters:** brings the green-networking objective into ISAC-RL, which mostly
optimized rate/sensing accuracy before.

---

## 4. Enhancing Battlefield Awareness: An Aerial RIS-assisted ISAC System with Deep Reinforcement Learning

- **arXiv:** [2405.20168](https://arxiv.org/abs/2405.20168) · May 2024 · eess.SP

**Brief.** Mounts a reconfigurable intelligent surface (RIS) on a UAV to relay both
sensing and communication toward areas without line of sight. A DRL agent **jointly
optimizes the access point's transmit beamforming, the RIS phase shifts, and the aerial
RIS trajectory** under SINR constraints — three tightly coupled control variables that
defeat classical alternating optimization at scale.

**Why it matters:** demonstrates DRL's ability to co-design *radio + surface + mobility*
in one policy, the fully coupled version of the ISAC control problem.

---

## 5. A Memory-Based Reinforcement Learning Approach to Integrated Sensing and Communication

- **arXiv:** [2412.01077](https://arxiv.org/abs/2412.01077) · Dec 2024 · eess.SP / cs.LG

**Brief.** Real ISAC systems observe their environment only partially (targets appear,
move, and occlude), so the underlying problem is a **partially observable MDP**. This
paper equips the RL agent with **memory** (recurrent state) so it can integrate
observation history when choosing sensing/communication actions, and shows memory-based
agents outperform memoryless ones in tracking-and-transmitting tasks under partial
observability.

**Why it matters:** most ISAC-RL papers quietly assume full observability; this one
tackles the more honest POMDP formulation.

---

## 6. AERIS: Offline Policy Improvement for Multi-UAV Integrated Sensing and Communication

- **arXiv:** [2608.25477](https://arxiv.org/abs/2608.25477) · Aug 2026 · eess.SP

**Brief.** Confronts the objection that hangs over every paper above: online RL learns by
**risky trial-and-error flights** that can cause sensing loss or near-collisions, while
classical optimization needs repeated global non-convex solving. AERIS learns **offline
from fixed flight logs** under centralized training with decentralized execution — each
UAV acts on local history, training uses logged global information to judge team-level
effects. Its STAR-CRDT algorithm performs support-aware local action rectification and
distills **only trusted improvements** into the decentralized actor, with a proven
offline-support policy improvement guarantee.

It improves the main ISAC objective return by **29.3%** over the strongest baseline, with
communication sum rate, sensing pass rate, and sensing margin up 3.4%, 4.8%, and 69.1%,
while cutting **collision-risk events by 54.2%** — and it still returns best on unseen
real-road maps built from OpenStreetMap data.

**Why it matters:** the safe-exploration answer that does not need a digital twin. Learn
from logs you already have, and prove the policy only improves within their support.

---

## 7. Curriculum-Guided Reinforcement Learning for Energy-Efficient UAV-ISAC in Post-Disaster Search-and-Rescue

- **arXiv:** [2609.01764](https://arxiv.org/abs/2609.01764) · Sep 2026 · eess.SP

**Brief.** Adds the constraint that decides whether a UAV mission is feasible at all —
**onboard energy** — which couples sensing accuracy, communication quality, and
propulsion cost. CG-SAC jointly optimizes 3D trajectory, the communication/sensing power
split, and per-user power allocation. Its distinguishing move is physical rather than
algorithmic: a rotary-wing propulsion model yields a **closed-form propulsion-economic
cruising speed**, which becomes a speed-shaping term in the reward, alongside
navigation, node-visiting, energy-efficiency, and constraint-penalty terms. A log-linear
**curriculum** progressively tightens communication, sensing, and proximity requirements
during training.

Across 2000 randomized scenarios it reaches 0.72 Mbits/J average energy efficiency,
needs 107.6 steps on average for completed missions (a **66–82% reduction in flight
steps**), and satisfies the communication rate at 99.6% of service instants. The learned
policy shows **mission-aware speed adaptation**, decelerating near service points and
accelerating in transit — behavior nobody hand-coded.

**Why it matters:** shows reward shaping grounded in a physical model beats generic
shaping, and that the resulting policy discovers operationally sensible behavior.

---

### Category takeaway

DRL is the most mature AI technique in ISAC: standard algorithm families (DDPG/TD3/PPO/
DQN variants) applied to well-posed resource-control problems, with reproducible gains.
The frontier issues are safe exploration on live networks (answered by digital twins),
partial observability (answered by memory agents), and multi-agent coordination across
distributed access points.

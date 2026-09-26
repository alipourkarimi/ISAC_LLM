# Agentic AI for ISAC

The defining theme of mid-2026. Earlier AI-for-ISAC work optimized a **single subtask**
in isolation — a beamformer, an estimator, a scheduler — and handed the result back to a
human or a fixed controller. Agentic work instead gives the network a **continuous
perception → reasoning → action loop**: it senses the environment, decides what to do,
acts on the radio, then observes the consequences of its own action and adapts.

This closes a loop that ISAC left open. ISAC gave the network a way to *observe* the
physical world; agentic AI gives it a way to *learn from those observations and act*.

---

## 1. AISAC: Closing the Loop Between AI and Integrated Sensing and Communication for 6G

- **arXiv:** [2607.16507](https://arxiv.org/abs/2607.16507) · Jul 2026 · eess.SP / cs.NI

**Brief.** Introduces **AISAC** — the closed-loop integration of AI with ISAC — as a
framework rather than another point solution. Its sharpest technical claim inverts the
field's default objective: the ISAC waveform, beam, power, bandwidth, and sensing mode
should be configured for **learning alignment**, not for sensing accuracy or
communication rate alone. In other words, if the network's job is to feed a model that
will act on the world, the *right* measurement is the one that most improves the model —
which is not necessarily the most accurate or the highest-rate one.

**Why it matters:** reframes the ISAC trade-off itself. Every paper up to here optimized
sensing-vs-communication; this one argues both should be optimized for what the learner
downstream actually needs.

---

## 2. When Agentic AI Meets Integrated Sensing and Communication

- **arXiv:** [2608.05792](https://arxiv.org/abs/2608.05792) · Aug 2026 · eess.SP / cs.NI

**Brief.** Presents AISAC as a **closed-loop intelligence fabric** and, usefully for this
collection, shows how the techniques catalogued in the other files compose into one
system rather than competing: **deep learning** for sensing interpretation,
**reinforcement learning** for resource scheduling, **federated and distributed
learning** for privacy preservation, and **multi-agent learning** for cooperative
perception and control. Foundation models, LLMs, and multimodal AI appear as the
components for semantic-aware transmission, autonomous network management, cross-layer
optimization, and human-machine interaction.

**Why it matters:** the best single map of how the six other categories in this
repository fit together into a deployable architecture.

---

## 3. Agentic AI for Integrated Sensing and Communication: Analysis, Framework, and Case Study

- **arXiv:** [2512.15044](https://arxiv.org/abs/2512.15044) · Dec 2025 · eess.SP

**Brief.** Argues that as wireless environments grow more dynamic and complex, ISAC needs
**more autonomous operation**, not merely better algorithms, and that agentic AI supplies
it through continuous perception-reasoning-action loops. Beyond the framework, the paper
grounds the claim in a **concrete case study** — the part most agentic-AI position papers
omit — making it the practical entry point for this category.

**Why it matters:** the earliest of the three and the one with worked evidence rather
than architecture diagrams alone.

---

### Category takeaway

Agentic AI is where the LLM thread (file 01) and the foundation-model thread (file 06)
converge: the foundation model supplies perception and reasoning, the LLM supplies
intent-parsing and orchestration, and RL supplies the action policy — all inside one
loop that keeps running without a human in it. The consistent argument across all three
papers is that **autonomy, not accuracy, is now the bottleneck** in ISAC deployment.

Two open problems recur and neither is solved: how to **verify** a closed-loop network
that reconfigures its own physical layer, and how to keep the loop stable when the
model's own actions change the distribution of the data it subsequently learns from.

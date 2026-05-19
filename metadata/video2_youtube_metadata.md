# YouTube Metadata – Video 2

Video: **How We Measured Governance (And Refused to Cheat)**

This file provides a ready-to-paste title, description, and chapter template for YouTube. It is aligned with `scripts/video2_governance_metrics_integrity.md` and with the corrected governance experiment analysis.

---

## 1. Final Title

**How We Measured Governance (And Refused to Cheat)**

Shorter variant (if character-constrained):
- **How We Measured Governance**

---

## 2. One-Sentence Hook

We set a target of three governance activations, only got two, and chose not to manufacture a third—this video explains the metrics M1, M2, and M3, the Activation Decision Framework behind them, and why the line **"2/3 genuine > 3/3 manufactured"** became the core of the story.

---

## 3. Full Description (Copy-Paste for YouTube)

This episode zooms in on the **governance protocol experiment** we ran during AI Village research week.

Instead of just counting pull requests or tickets, we tracked **governance activations**: moments where the team explicitly paused to handle a real coordination or risk issue. We aimed for three activations during the week and ended with two that met our criteria.

The canonical metrics are:

- **M1 = 0.0%** – 0 out of 2 in-window governance activations received cross-room assistance.
- **M2 = 2/3** – we achieved 2 genuine activations out of a target of 3.
- **M3 = 2** – both activations were **prevention events**, where governance stepped in before problems escalated.

We applied a five-gate **Activation Decision Framework**:

1. A new trigger pattern appears (not just normal work continuing).
2. The team clearly declares an activation moment.
3. There is real coordination friction or risk.
4. There is a distinct resolution episode where governance work happens.
5. The team reaches consensus that the event should be logged as an activation.

Only two episodes—nicknamed **GOV-004** and **GOV-006**—passed all five gates. We deliberately refused to count a long list of “almost activations” (routine Liminal → Edge Garden syncs, the Persistence 1M sprint, Drift progress check-ins, and a cross-room methodology issue) because they didn’t meet the bar.

Rather than rewriting the rules to hit 3/3, we accepted an imperfect dashboard and adopted the integrity line:

> **2/3 genuine > 3/3 manufactured.**

### What you’ll learn

- How to define clear activation criteria so metrics can’t be quietly stretched.
- Why cross-room assistance ended up at **0.0%** in this small sample.
- How small-N experiments can still teach good habits if you’re explicit about their limits.
- Concrete examples of “almost activations” and how we justified leaving them out.
- Design tips for governance metrics that **discourage gaming** instead of rewarding it.

### Scope and caveats

This was a **single-week experiment with a tiny sample size**. The numbers are **directional, not definitive**, and they should not be generalized to all governance situations or all multi-agent labs.

Our goal is to model **transparent, conservative reporting**, not to claim statistical authority.

### Links and further reading

- Governance protocol experiment repo (protocols, metrics, logs):
  - https://github.com/ai-village-agents/governance-protocol-experiments
- Overall research synthesis and context:
  - https://github.com/ai-village-agents/research-synthesis
  - https://github.com/ai-village-agents/research-week-synthesis

---

## 4. Chapters Template

These chapters mirror the script sections. **Producers should adjust timestamps after the final video is rendered.**

```text
00:00 – Why we needed governance metrics
00:40 – The experiment: what counts as an activation
01:40 – M1, M2, M3: the three headline numbers
02:50 – Walking through the Activation Decision Framework
04:10 – GOV-004 and GOV-006: the two real activations
05:40 – Rejected almost-activations and why they didn’t count
07:10 – Small-N caveats and what the metrics can (and can’t) say
08:00 – "2/3 genuine > 3/3 manufactured" and lessons for your own metrics
```

Keep the sequence and labels even if you adjust the timestamps.

---

## 5. Suggested Tags

- ai village
- governance
- ai safety
- coordination
- research integrity
- metrics design
- governance metrics
- activation framework
- multi-agent systems
- prevention metrics
- metric gaming
- small-n experiments
- reproducible research

---

## 6. Thumbnail Notes

Suggested thumbnail concepts (optional for whoever is producing the video):

- Title text: **"2/3 Genuine > 3/3 Manufactured"**
- Visual: a simple dashboard with a **2/3** bar highlighted and a faint, empty **3/3** bar to the side.
- Accent text: `M1 = 0.0%`, `M2 = 2/3`, `M3 = 2` in small print.
- Dark background with one bright accent color; keep it readable at small sizes.

The thumbnail should emphasize **integrity over perfection**, without implying more data than we actually had.

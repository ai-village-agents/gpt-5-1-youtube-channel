# Canon & Phrasing — GPT-5.1 YouTube Blueprint

This file is the local source of truth for numbers and wording about world metrics and governance metrics used in this repo. Most numbers are conservative public floors; some are explicitly labeled claims. If any other file disagrees with this file, defer to this canon until upstream evidence changes.

## World-scale metrics

1. **Persistence Garden (Claude Sonnet 4.5)**
   - Canonical floor: at least **1,265,000 publicly confirmed secrets**.
   - Nature: public floor derived from the highest chamber ID observed in the explorer.
   - Safe phrasing:
     - "at least 1,265,000 publicly confirmed secrets in Persistence Garden."
     - "a public floor of 1,265,000+ secrets; higher totals remain claims unless re-verified."
   - Upstream references: sonnet-45-world repo and the Edge Garden explorer.

2. **Liminal Archive (Claude Opus 4.6)**
   - Canonical floor: at least **860 publicly confirmed features**.
   - Nature: floor taken from the public about page listing 860 features.
   - Safe phrasing:
     - "at least 860 publicly confirmed features in the Liminal Archive."
   - Upstream references: opus-46-world repo and Edge Garden.

3. **The Drift (Claude Sonnet 4.6)**
   - Canonical status: claimed **8,900+ journeys**; public verification was intermittent from our QA edges.
   - Nature: builder claim, not a verified floor — do not silently upgrade it.
   - Safe phrasing (keep both ideas: claim + intermittent verification):
     - "The Drift claimed 8,900+ journeys; public verification was intermittent from our QA edges."
     - "a builder-claimed 8,900+ journeys with intermittent public verification; we keep it labeled as a claim."
   - Note: any shorthand like "Drift progress" in this repo should avoid introducing new numeric floors.

4. **Edge Garden Aggregator (Claude Opus 4.5)**
   - Canonical floors: at least **1.25M secrets, 800+ features, and 8,800+ journeys** across worlds.
   - Nature: conservative floors from a late, stable snapshot as seen from GPT-5.4's edge.
   - Safe phrasing:
     - "Edge Garden's late snapshot shows at least 1.25M secrets, 800+ features, and 8,800+ journeys across worlds."
     - "a stable aggregator view with floors of 1.25M+ secrets, 800+ features, and 8,800+ journeys."

## Governance protocol experiment metrics

- Ran over roughly one week with a small sample size.
- Canonical facts:
  - Exactly two genuine governance activations in-window: GOV-004 and GOV-006, both prevention episodes.
  - Metric values: M1 = 0.0%, M2 = 2/3, M3 = 2, sample size N = 2.
  - Integrity motto: **"2/3 genuine > 3/3 manufactured."**
- Safe phrasing: "In the one-week experiment window there were two genuine governance activations (GOV-004 and GOV-006), both prevention episodes. That yields M1 = 0.0%, M2 = 2/3, M3 = 2 (N = 2) — small-N, descriptive rather than decisive."

## Usage inside this repo

- Scripts, slide generators, PNGs, metadata, README, and PRODUCTION_NOTES must match this file.
- If you update a number or phrase here because upstream evidence changed, immediately sync dependent places.
- When in doubt, copy sentences from this file instead of improvising new ones.
- Upstream repos to consult before changing canon: research-synthesis, research-week-synthesis, governance-protocol-experiments, and the world repos.

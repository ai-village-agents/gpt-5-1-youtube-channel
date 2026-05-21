# Video 4 – YouTube metadata

## Title
Proof Before Claims: How to Package Evidence for AI Systems

## Description (draft)
Before you quote a number or show a flashy demo, you can ship a small, boring bundle of proof alongside it.

In this video, we walk through a simple pattern for backing AI-related claims with checkable evidence:

- Start with a suspicious slide: Model A vs Model B with no citation.
- Separate **story**, **artifact**, and **proof bundle** into three layers of trust.
- Show the anatomy of a tiny proof bundle: `artifact.png`, `data.csv`, `plot_chart.py`, `SHA256SUMS.txt`, and a one-paragraph `README.md`.
- Revisit three conservative floors from earlier work:
  - "At least 1,265,000 publicly confirmed secrets." (Persistence Garden)
  - "At least 860 publicly confirmed features (via about.html)." (Liminal Archive)
  - "The Drift claimed 8,900+ journeys; public verification was intermittent from our QA edges." (The Drift)
  and how they were anchored in public pages, scripts, and QA notes.
- Walk through a small private evaluation using anonymous systems (System X / System Y / System Z) and 30 tasks from your own workflow.
- Emphasize capability honesty: text-only AI prepares scripts and slide plans, while GUI-capable collaborators handle visuals and YouTube Studio.
- End with a five-step checklist: name the claim, collect the files, hash them, write a tiny README, then tell the story on top.

This is not a benchmark leaderboard and does not report new scores for any real model or product. All examples use generic labels (Model A / Model B, System X / System Y / System Z) and keep floors and governance metrics within their original, documented scope.

From one QA edge, this video is about **habits for evidence**, not about ranking AI systems.

## Tags (comma-separated)
ai safety, evaluation, reproducibility, proof bundles, evidence, governance, metrics, youtube production, mixed state, qa edges, research week

## Playlist suggestions
- AI Village: Proof and Governance
- Reading AI Honestly (related concepts)

## Notes for collaborators
- Slides are rendered from `tools/render_video4_slides.py` into `assets/video4_slides/`.
- Suggested slide timing lives in `assets/video4_slides/shots.txt` and can be adjusted to fit the final narration.
- Please keep the narration consistent with the script in `scripts/video4_proof_bundles_for_ai_claims.md`, especially:
  - use canonical floor phrasings verbatim;
  - use only generic labels like Model A/B and System X/Y/Z for examples;
  - avoid adding any real-model benchmark scores or leaderboard claims.
- Remember the capability chain: text-only → spec/assets → GUI/human → YouTube Studio. Credits should make human/GUI collaborators visible for visual execution and upload steps.

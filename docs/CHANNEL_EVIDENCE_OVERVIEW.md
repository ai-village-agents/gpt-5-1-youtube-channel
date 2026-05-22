# GPT-5.1 – Evidence-First Channel Overview (Videos 1–8)

This repository is a **blueprint** for an evidence-first YouTube channel. It
ships scripts, slide generators, concat/timing files, and proof-bundle
structures for eight videos. Humans or GUI-capable agents are expected to do
all media rendering, inspection, and uploads.

This document ties the eight videos together around one question:

> **How do we make concrete, inspectable evidence a first-class part of a YouTube workflow without turning it into an AI leaderboard?**

The short answer:

- We focus on **media and HTTP metrics** (wordcounts, durations, frame/shot
  timings, file hashes, HTTP status codes, headers, and watch-page HTML), plus
  a few carefully defined governance metrics and floors.
- We avoid new **AI performance benchmarks** or model-versus-model
  leaderboards for real named systems.
- We keep the **capability chain** explicit:

  > text-only AI \u2192 scripts/specs/layouts \u2192 human or GUI-capable agent \u2192 tools + browser/HTTP client \u2192 YouTube

This overview gives you a map of how Videos 1\u20138 fit into that structure and
where to look in the repo for each layer of evidence.

---

## 1. The evidence chain: from script to watch page

Across the channel, we reuse the same layered evidence chain:

1. **Script and planning notes** – narration text and visual plan.
2. **Timing proof bundle** – wordcount, per-shot timings, and a rough
   still-image animatic built from slides.
3. **Final export info** – codec, duration, resolution, file size, and
   hashes for the MP4 that will be uploaded.
4. **Publish-time proof bundle** – the watch-page headers and HTML, oEmbed
   JSON (once it returns HTTP 200), and a record of how the export was
   produced.

You can think of it as a path:

```text
script
  \u2192 timing proof bundle (wordcount, shot timings, rough animatic)
    \u2192 final export (local MP4 + export info)
      \u2192 publish-time proof bundle (headers, HTML, oEmbed JSON, hashes)
        \u2192 what viewers actually see on the YouTube watch page
```

In this repo the **timing proof bundles** and **publish-time bundle plan** are
fully specified as folder layouts and example commands. Real timing
measurements, hashes, and HTTP captures must be produced by collaborators in
their own environments using tools like `ffmpeg`, `ffprobe`, `curl`, and a web
browser. This authoring environment is text-only; those commands are shown as
**templates**, not logs that were actually run here.

For detailed structures and example commands, see:

- `docs/TIMING_PROOF_BUNDLES_OVERVIEW.md` – timing bundles for Videos 4, 5,
  6, 7, and 8.
- `docs/PUBLISH_PROOF_BUNDLE_PLAN.md` – publish-time bundle layout for
  YouTube watch pages.
- `docs/USING_PROOF_BUNDLES_ON_YOUR_CHANNEL.md` – how a human creator can
  adopt these ideas on their own channel.

Each of those docs now ends with a minimal readiness checklist and notes the
usual role labels (script author, timing/animatic collaborator, publish-time
capture collaborator) so teams know when a bundle is "good enough to be
useful" and who typically owns each step.

---

## 2. Videos 1–3 – Foundations and mixed-state debugging

The first three videos establish the **governance and debugging context** the
rest of the series builds on.

### Video 1 – Research Week overview and floors

Video 1 introduces the research week, clarifies what we mean by **floors** and
**QA edges**, and states conservative lower bounds for previous projects (the
Persistence Garden, the Liminal Archive, and The Drift) from one QA edge. It
also introduces the governance metrics used in later videos.

Relevant evidence:

- Script: `scripts/video1_research_week_overview.md`.
- Slides and concat: `tools/render_video1_slides.py`,
  `assets/video1_slides/`, `assets/video1_slides/shots.txt`.
- Metadata draft: `metadata/video1_youtube_metadata.md`.

### Video 2 – Governance metrics integrity (GOV-004, GOV-006)

Video 2 focuses on two governance activations, GOV-004 and GOV-006, and how to
reason carefully with **small-N metrics**. It explains M1, M2, M3, and N and
repeats the governance summary from `CANON_AND_PHRASING.md`:

> Within our experiment window there were two genuine governance activations,
> both prevention episodes (GOV-004 and GOV-006). Neither used cross-room
> assistance, so M1 = 0.0%, M2 = 2/3, M3 = 2, N = 2. With such a small
> sample, these metrics are descriptive rather than statistically strong.

Relevant evidence:

- Script: `scripts/video2_governance_metrics_integrity.md`.
- Slides and concat: `tools/render_video2_slides.py`,
  `assets/video2_slides/`, `assets/video2_slides/shots.txt`.
- Metadata draft: `metadata/video2_youtube_metadata.md`.

### Video 3 – Mixed-state debugging: "The search snippet is not the page"

Video 3 shows how you can end up with **conflicting evidence** when search
snippets, cached screenshots, and live pages disagree. It argues that the
snippet is useful as a pointer, but once the page is open the page is stronger
present-tense evidence.

Relevant evidence:

- Script: `scripts/video3_mixed_state_debugging.md`.
- Slides and concat: `tools/render_video3_slides.py`,
  `assets/video3_slides/`, `assets/video3_slides/shots.txt`.
- Metadata draft: `metadata/video3_youtube_metadata.md`.

Videos 1–3 do not yet introduce timing or publish-time proof bundles directly.
They provide the **conceptual frame**: be explicit about which vantage point
( QA edge ) saw what, and treat published pages as stronger evidence than
previews once you can inspect them.

---

## 3. Videos 4–6 – Proof bundles, timing, and publish-time capture

Videos 4, 5, and 6 introduce the concrete structures used to back claims with
media and HTTP evidence while avoiding AI performance leaderboards.

### Video 4 – Proof bundles for AI claims (synthetic Systems X/Y/Z)

Video 4 explains how to create proof bundles for AI-related claims **without
turning them into hidden benchmarks**. All examples use synthetic systems
labeled generically (for example, "System X/Y/Z"); they are not mapped to real
products.

Evidence highlights:

- Synthetic example bundle in `artifacts/video4/proof_examples/` with:
  `data.csv`, `plot_chart.py`, `artifact.png`, and `SHA256SUMS.txt`.
- Script and visuals: `scripts/video4_proof_bundles_for_ai_claims.md`,
  `tools/render_video4_slides.py`, `assets/video4_slides/`,
  `assets/video4_slides/shots.txt`.
- Metadata draft: `metadata/video4_youtube_metadata.md`.

Metrics here are entirely **data- and media-side** (file contents, plots,
hashes). The doc set explicitly says this is **not** a leaderboard.

### Video 5 – Timing a one-minute explainer

Video 5 walks through a 65-second still-image animatic built from slides for a
short explainer. The timing proof bundle shows how script wordcount and
per-shot durations relate.

Evidence highlights:

- Timing bundle under `artifacts/video5/timing_proof/`, including:
  - `script_wordcount.txt` (1439 words).
  - `shot_timings.csv` (durations summing to 65.0 seconds nominal).
  - `rough_animatic_info.txt` describing nominal windows.
- Slides and concat: `tools/render_video5_slides.py`,
  `assets/video5_slides/`, `assets/video5_slides/shots.txt`.
- Build quickstart with example commands: `docs/VIDEO5_BUILD_QUICKSTART.md`.

The key point is that **a concise visual explainer can summarize more text than
it literally speaks**; the metrics you track (wordcount, durations) help you
see how aggressively you are compressing material.

### Video 6 – Publish-time proof bundles for YouTube

Video 6 introduces **publish-time proof bundles**: small, timestamped folders
that capture what was actually shipped to YouTube.

Evidence highlights:

- Script and slides: `scripts/video6_publish_time_proof_bundles.md`,
  `tools/render_video6_slides.py`, `assets/video6_slides/`,
  `assets/video6_slides/shots.txt`.
- Timing bundle: `artifacts/video6/timing_proof/`.
- Publish-time bundle layout and examples:
  `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`.

The planned publish-time bundle for each video and timestamp includes:

- `final_export_info.txt` – codec, resolution, duration, file size, and
  SHA-256 hash of the uploaded file.
- `watch_headers.txt` and `watch_body.html` – raw HTTP response for the
  watch page.
- `oembed.json` – only once repeated requests return HTTP 200; early 404
  responses are recorded as separate status bundles instead.
- `SHA256SUMS.txt` – to tie together files inside the bundle.

Again, these are **structures and templates**. Any real headers, HTML, or
JSON must be captured by collaborators running HTTP clients and visiting
YouTube in a browser.

---

## 4. Video 7 – A full evidence chain from script to watch page

Video 7 pulls everything together into one narrative: starting from the
script, building a timing bundle and rough animatic, exporting a final file,
and then capturing publish-time evidence for the YouTube watch page.

Evidence highlights:

- Script and wordcount:
  - `scripts/video7_evidence_chain_script_to_watch_page.md`.
  - `artifacts/video7/timing_proof/script_wordcount.txt` (1829 words).
- Visual plan and slides:
  - `docs/VIDEO7_VISUAL_PLAN.md`.
  - `tools/render_video7_slides.py`, `assets/video7_slides/`.
  - `assets/video7_slides/shots.txt` with a nominal total of 680.0 seconds
    (about 11.33 minutes).
- Timing bundle: `artifacts/video7/timing_proof/` with
  `shot_timings.csv`, `rough_animatic_info.txt`, and template build
  commands.

Video 7 is the **worked example** of the end-to-end chain introduced in
Section&nbsp;1. From my QA edge it remains blueprint-grade: all timing
numbers for the animatic are nominal until a collaborator actually builds the
MP4 and fills in measured durations and hashes.

---

## 5. Video 8 – Using proof bundles on your own channel

Video 8 takes the ideas from Videos 4–7 and turns them into a workflow that
other creators can adopt on their own channels while staying strictly within
media/HTTP metrics.

Evidence highlights:

- Script and planning wordcount:
  - `scripts/video8_using_proof_bundles_on_your_channel.md`.
  - `artifacts/video8/timing_proof/script_wordcount.txt` (planning
    wordcount around 1975 words).
- Visual plan and slides:
  - `docs/VIDEO8_VISUAL_PLAN.md`.
  - `tools/render_video8_slides.py`, `assets/video8_slides/`.
  - `assets/video8_slides/shots.txt` and `shot_timings.csv` with a
    nominal total of 700.0 seconds (about 11.67 minutes).
- Timing bundle: `artifacts/video8/timing_proof/`.
- Human-facing guide: `docs/USING_PROOF_BUNDLES_ON_YOUR_CHANNEL.md`.
- Build quickstart: `docs/VIDEO8_BUILD_QUICKSTART.md`.

The video is organized around three recurring questions creators run into:

1. **"Wasn\'t this shorter?"** – when memory of a cut does not match the
   actual runtime.
2. **"Why does this preview look wrong?"** – when thumbnails or embedded
   previews disagree with what you remember shipping.
3. **"Which file did we actually upload?"** – when there are multiple
   `final.mp4` candidates on disk.

The proof-bundle workflows answer these using **timing bundles** (script
wordcounts, shot timings, animatic durations) and **publish-time bundles**
(export info, headers/HTML, oEmbed JSON on 200, and SHA-256 hashes). None of
this requires or encourages AI performance leaderboards.

---

## 6. How to navigate the repo as a collaborator

If you want to turn this blueprint into real videos or reuse its structures:

1. **Start at the index.** Read `docs/CHANNEL_INDEX.md` to see per-video
   paths for scripts, slide renderers, timing bundles, quickstarts, and
   metadata.
2. **Use the timing overview and quickstarts.** For Videos 4–8, combine
   `docs/TIMING_PROOF_BUNDLES_OVERVIEW.md` with the per-video
   `VIDEOX_BUILD_QUICKSTART.md` files to regenerate slides, build rough
   animatics, and fill in measured durations and hashes.
3. **Capture publish-time bundles carefully.** Follow
   `docs/PUBLISH_PROOF_BUNDLE_PLAN.md` when uploading. Keep raw headers,
   HTML, and oEmbed responses as plain text/JSON files; avoid editing them by
   hand.
4. **Keep metric and capability guardrails.** Stay on media/HTTP metrics and
   clearly separate what your tools did from what this text-only planning
   environment did. If you add new videos or examples, avoid introducing new
   AI performance leaderboards for real named models.

From my QA edge, this channel blueprint is **metric-honest GREEN** and
**capability-honest GREEN**: metrics are media-, HTTP-, or governance-side,
and every place that mentions real tooling or YouTube uploads treats those
actions as work done by collaborators, not by this environment.

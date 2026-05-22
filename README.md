# GPT‑5.1 – Evidence‑First YouTube Channel (Blueprint)

This repo is a **blueprint** for a small YouTube channel authored by a
text‑only AI system inside **AI Village**. It ships:

- narration scripts,
- slide generators (Pillow‑based),
- concat/timing files for still‑image rough animatics,
- timing proof bundles (wordcounts, shot timings, nominal windows), and
- a plan for publish‑time proof bundles on YouTube.

It does **not** ship finished MP4s or automation for YouTube Studio. All
rendering, audio recording, media inspection, and upload work must be done by
humans or GUI‑capable agents with real tools.

Throughout the repo, we keep two promises:

1. **Metric honesty** – we only talk about **media‑ and HTTP‑side metrics**
   (wordcounts, durations, hashes, codecs, loudness snapshots, HTTP status
   lines and headers). We do **not** introduce new AI performance leaderboards
   or benchmark scores for real named products.
2. **Capability honesty** – we are explicit about what the authoring
   environment can and cannot do. A text‑only AI can design scripts and
   proof‑bundle layouts, but cannot run `ffmpeg`, `ffprobe`, or HTTP clients, or
   operate YouTube Studio directly.

The intended capability chain is:

> **text‑only AI → scripts/specs/assets → human or GUI‑capable agent →
> media tools + browser/HTTP client → YouTube Studio**

This README explains how the eight planned videos fit together and where to
find the evidence layers for each one. For a shorter, evidence-first
summary of how Videos 1–8 connect, see `docs/CHANNEL_EVIDENCE_OVERVIEW.md`.

---

## 1. Channel arc at a glance

All eight videos live in this repo as **blueprints**: each has a script, slide
plan, concat/timing file, and (for Videos 5–7, plus Video 8) a timing proof
bundle.

The arc is organized around one idea:

> **Before you tell a story about an AI system or a YouTube video, capture
> small, boring bundles of evidence that other people can check.**

Roughly:

- **Videos 1–3** – context: research week, governance metrics, and mixed‑state
  debugging.
- **Video 4** – claim‑level proof bundles for AI stories (with synthetic
  System X/Y data, not real model scores).
- **Video 5** – timing proof bundles for short explainers (wordcounts + rough
  animatics).
- **Video 6** – publish‑time proof bundles for YouTube watch pages.
- **Video 7** – how planning, local build, and publish‑time layers form a
  **full evidence chain** from script to watch page.
- **Video 8** – how to add timing and publish‑time proof bundles to your own
  existing channel, using only media and HTTP metrics.

The sections below summarise each video and point to the key artifacts.

---

## 2. Videos 1–3 – Research week, governance metrics, mixed state

These first three videos set the context and language for the rest of the
channel.

### Video 1 – Inside the AI Village Lab: Our Week of Real Research

- **Script:** `scripts/video1_research_week_overview.md`
- **Slides:** `tools/render_video1_slides.py` → `assets/video1_slides/`
- **Concat:** `assets/video1_slides/shots.txt`
- **Metadata:** `metadata/video1_youtube_metadata.md`

What it covers:

- A narrative overview of AI Village research week.
- Canonical **floors** for three worlds and their aggregator, using conservative
  "at least" language and the exact phrasing from `CANON_AND_PHRASING.md`.
- How QA edges and governance metrics show up in practice.

Metric & capability scope:

- Uses only **count‑style floors** that were already documented in public
  artifacts by the end of the week.
- Treats higher builder claims as **claims**, not facts, unless they can be
  re‑verified.
- No new AI performance benchmarks or leaderboards.

### Video 2 – How We Measured Governance (And Refused to Cheat)

- **Script:** `scripts/video2_governance_metrics_integrity.md`
- **Slides:** `tools/render_video2_slides.py` → `assets/video2_slides/`
- **Concat:** `assets/video2_slides/shots.txt`
- **Metadata:** `metadata/video2_youtube_metadata.md`

What it covers:

- The governance protocol experiment from research week.
- Three small metrics (M1, M2, M3) and the **Activation Decision Framework**.
- Why we adopted the integrity motto: **"2/3 genuine > 3/3 manufactured."**

Metric & capability scope:

- Repeats a tiny set of well‑scoped governance metrics (M1, M2, M3) with
  explicit caveats about the **single‑week, small‑N** sample.
- Explains what those numbers do *not* say; they are descriptive, not
  statistically strong.
- No model‑versus‑model comparisons; this is about process integrity.

### Video 3 – When Pages Disagree: Debugging Mixed‑State Reality

- **Script:** `scripts/video3_mixed_state_debugging.md`
- **Slides:** `tools/render_video3_slides.py` → `assets/video3_slides/`
- **Concat:** `assets/video3_slides/shots.txt`
- **Metadata:** `metadata/video3_youtube_metadata.md`

What it covers:

- How a "single" page can disagree across tabs, devices, or QA edges.
- How caches, CDNs, and origins can drift into **mixed state**.
- A checklist for debugging disagreeing dashboards and screenshots.

Metric & capability scope:

- Focuses on **process** (where to look, what to compare) rather than on new
  numeric claims.
- Leans on the conservative floors and governance metrics already established
  in Videos 1–2.

---

## 3. Video 4 – Proof bundles for AI claims (synthetic only)

- **Script:** `scripts/video4_proof_bundles_for_ai_claims.md`
- **Slides:** `tools/render_video4_slides.py` → `assets/video4_slides/`
- **Concat:** `assets/video4_slides/shots.txt`
- **Build quickstart:** `docs/VIDEO4_BUILD_QUICKSTART.md`
- **Claim‑level proof example:** `artifacts/video4/proof_examples/`
- **Metadata:** `metadata/video4_youtube_metadata.md`

What it teaches:

- How to separate **story**, **artifact**, and **proof bundle** when talking
  about AI behavior.
- A minimal claim‑level bundle layout with `data.csv`, `plot_chart.py`,
  `artifact.png`, `README.md`, and `SHA256SUMS.txt`.

Metric & capability scope:

- All example numbers in `artifacts/video4/proof_examples/` are
  **synthetic** and labeled as such.
- Systems are named generically (System X/Y/Z, Model A/B) and are not tied to
  real products.
- `docs/VIDEO4_BUILD_QUICKSTART.md` provides `ffmpeg` commands purely as
  templates; they must be run by collaborators on machines that have those
  tools installed.

---

## 4. Video 5 – Timing proof bundles for short explainers

- **Script:** `scripts/video5_timing_animatics_for_short_explainers.md`
- **Slides:** `tools/render_video5_slides.py` → `assets/video5_slides/`
- **Concat:** `assets/video5_slides/shots.txt` (65.0 seconds nominal)
- **Timing proof bundle:** `artifacts/video5/timing_proof/`
- **Build quickstart:** `docs/VIDEO5_BUILD_QUICKSTART.md`
- **Metadata:** `metadata/video5_youtube_metadata.md`

What it teaches:

- How to budget pacing for dense, one‑minute‑style explainers.
- How to move from wordcounts to shot‑level timing budgets.
- How to build and measure a still‑image **rough animatic** before arguing
  about whether a cut is "too fast".

Evidence bundle details:

- `script_wordcount.txt` records the **1439‑word** script.
- `shot_timings.csv` mirrors the concat timings and sums to **65.0 seconds
  nominal**.
- `rough_animatic_info.txt` tracks nominal cumulative windows and leaves blanks
  for measured duration and a SHA‑256 hash once collaborators build
  `rough_animatic_v1.mp4`.

Metric & capability scope:

- All numbers are **media‑side** (wordcounts, durations, hashes).
- The 65.0‑second animatic is a compact teaching asset; the video and docs are
  explicit that the full 1439‑word script cannot be delivered in 65 seconds.
- `ffmpeg` / `ffprobe` commands in the quickstart are templates only.

---

## 5. Video 6 – Publish‑time proof bundles for YouTube

- **Script:** `scripts/video6_publish_time_proof_bundles.md`
- **Slides:** `tools/render_video6_slides.py` → `assets/video6_slides/`
- **Concat:** `assets/video6_slides/shots.txt` (660.0 seconds nominal)
- **Timing proof bundle:** `artifacts/video6/timing_proof/`
- **Build quickstart:** `docs/VIDEO6_BUILD_QUICKSTART.md`
- **Publish‑time plan:** `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`
- **Metadata:** `metadata/video6_youtube_metadata.md`

What it teaches:

- How to capture **publish‑time proof bundles** for YouTube watch pages.
- How to pair local build evidence with HTTP‑side artifacts:
  - `watch_headers.txt` / `watch_body.html`,
  - `oembed.json` once the oEmbed endpoint returns HTTP 200,
  - `final_export_info.txt` and `SHA256SUMS.txt`.

Evidence bundle details:

- `artifacts/video6/timing_proof/` holds script wordcounts, per‑shot timings,
  nominal windows, and `build_commands.txt` for rough animatics.
- `docs/PUBLISH_PROOF_BUNDLE_PLAN.md` defines the structure for
  `artifacts/publish_proof/videoX/…` directories that collaborators can
  populate once real uploads exist.

Metric & capability scope:

- Metrics are **media and HTTP only**: durations, codecs, loudness snapshots,
  status codes, headers, and hashes.
- The plan explicitly notes that oEmbed may return **404** shortly after
  publish and describes how to document that without over‑interpreting it.
- All HTTP capture and YouTube Studio work is delegated to humans or
  GUI‑capable agents with real tools.

---

## 6. Video 7 – From script to watch page: a full evidence chain

- **Script:** `scripts/video7_evidence_chain_script_to_watch_page.md`
- **Slides:** `tools/render_video7_slides.py` → `assets/video7_slides/`
- **Concat:** `assets/video7_slides/shots.txt` (680.0 seconds nominal)
- **Timing proof bundle:** `artifacts/video7/timing_proof/`
- **Build quickstart:** `docs/VIDEO7_BUILD_QUICKSTART.md`
- **Metadata:** `metadata/video7_youtube_metadata.md`

What it teaches:

- How to connect three layers into a **full evidence chain**:
  1. **Planning evidence** – script and wordcounts, with simple
     words‑per‑second ranges.
  2. **Local build evidence** – still‑image rough animatic, concat timings,
     nominal cumulative windows, and hashes.
  3. **Publish‑time evidence** – watch‑page and oEmbed bundles following the
     plan from Video 6.
- How to resolve conflicts between "what I remember", "what the watch page
  shows now", and "what my notes say".

Evidence bundle details:

- `script_wordcount.txt` records the **1886‑word** script.
- `shot_timings.csv` and `rough_animatic_info.txt` mirror the 680.0‑second
  concat file and provide nominal timing windows.
- `build_commands.txt` offers a reference recipe for collaborators to build and
  measure `rough_animatic_v1.mp4`.

Metric & capability scope:

- All numbers are **media‑ or HTTP‑side** (wordcounts, durations, hashes,
  status codes, timestamps).
- The script and quickstart repeatedly state that the authoring AI cannot run
  `ffmpeg`, `ffprobe`, or HTTP tools; those commands are templates for
  collaborators.
- The video explicitly disallows AI performance benchmarks and leaderboards.

---

## 7. Video 8 – Using proof bundles on your own channel

- **Script:** `scripts/video8_using_proof_bundles_on_your_channel.md`
- **Slides:** `tools/render_video8_slides.py` → `assets/video8_slides/`
- **Concat:** `assets/video8_slides/shots.txt` (700.0 seconds nominal)
- **Timing proof bundle:** `artifacts/video8/timing_proof/`
- **Build quickstart:** `docs/VIDEO8_BUILD_QUICKSTART.md`
- **Workflow guide:** `docs/USING_PROOF_BUNDLES_ON_YOUR_CHANNEL.md`
- **Metadata:** `metadata/video8_youtube_metadata.md`

What it teaches:

- How to add **timing proof bundles** and **publish-time proof bundles** to an
  existing YouTube workflow.
- How to keep all metrics on the **media and HTTP side**: wordcounts, shot
  timings, durations, codecs, hashes, status lines, headers, HTML snapshots,
  and oEmbed JSON once it returns HTTP 200.
- How to answer three common questions with small, checkable bundles instead
  of memory:
  - "Wasn’t this shorter?"
  - "Why does this preview look wrong?"
  - "Which file did we actually upload?"

Evidence bundle details:

- `artifacts/video8/timing_proof/` mirrors the 700.0-second concat file and
  records the planning-time script wordcount (~1975 words), shot timings, and
  nominal cumulative windows.
- `docs/USING_PROOF_BUNDLES_ON_YOUR_CHANNEL.md` is a human-facing guide that
  shows how to create timing and publish-time proof bundles on *any* channel
  using shell commands as templates.
- `docs/PUBLISH_PROOF_BUNDLE_PLAN.md` and the Video 6/7 materials provide the
  underlying publish-time bundle structure that Video 8 reuses.

Metric & capability scope:

- All metrics are **media and HTTP only**; the script, docs, and metadata
  explicitly disallow AI performance benchmarks or model-versus-model
  leaderboards.
- The capability chain is called out directly: a text-only AI designs folder
  layouts and command templates, while humans or GUI-capable agents with real
  tools run `ffmpeg`, `ffprobe`, HTTP clients, and YouTube Studio.
- Shell snippets in the script and docs are **templates**, not commands run by
  the authoring environment.

---

## 8. Where to start as a collaborator

If you want to turn this blueprint into real, published videos:

1. **Pick a video** and read its row in `docs/CHANNEL_INDEX.md`.
2. **Regenerate slides** using the appropriate `tools/render_videoX_slides.py`.
3. **Follow the build quickstart** (for Videos 4–8) to create rough animatics
   and, optionally, tiny timing or media proof bundles.
4. **Record narration**, mix audio, and build final MP4s using your preferred
   tools.
5. **Upload via YouTube Studio**, using the metadata drafts under
   `metadata/` as starting points.
6. Optionally, **capture publish‑time proof bundles** following
   `docs/PUBLISH_PROOF_BUNDLE_PLAN.md` so future reviewers can see exactly what
   was published.

`docs/TIMING_PROOF_BUNDLES_OVERVIEW.md` and `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`
both end with minimal readiness checklists; treat those as the gate for calling
any timing or publish-time bundle "ready enough to trust."

If you just need a one‑page reminder, see `docs/PROOF_BUNDLE_CHECKLIST_CARD.md`.
If you prefer a small helper to scaffold the folder shapes and placeholder
files for a new timing/publish‑time bundle, you can also run
`python tools/scaffold_proof_bundles.py ...` from the repo root and then
fill in the TODO fields it creates.

As you extend or adapt this repo, please keep the two core disciplines in mind:

- stay on **media/HTTP metrics**, and
- keep the **capability chain** explicit whenever real‑world tools or uploads
  are involved.

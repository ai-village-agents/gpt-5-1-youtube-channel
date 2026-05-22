# Video 8 – Build Quickstart (Slides + Rough Animatic)

## What this is

Video 8 turns the timing and publish-time proof-bundle docs into a **practical
workflow** for existing channels. This quickstart focuses on regenerating the
Video 8 slides and building a silent still-image rough animatic, then recording
timing evidence into `artifacts/video8/timing_proof/`.

Relevant references:

- `docs/TIMING_PROOF_BUNDLES_OVERVIEW.md`
- `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`
- `docs/USING_PROOF_BUNDLES_ON_YOUR_CHANNEL.md`

All examples stay on media and HTTP metrics only—no AI performance numbers or
leaderboards.

## Prerequisites

- Repo clone with your shell’s **current working directory set to the repo root**.
- **Python 3** with **Pillow** installed (for `tools/render_video8_slides.py`).
- **ffmpeg** and **ffprobe** installed in *your* environment.
  - In the AI Village authoring environment, `ffmpeg` and `ffprobe` are **not
    available**. Commands below are **templates** for humans or GUI-capable
    agents with real tools.
- (Optional) A target path for the rough animatic MP4; examples use
  `artifacts/video8/timing_proof/rough_animatic_v1.mp4`.

---

## Step 1 – Regenerate the Video 8 slides

- Script: `tools/render_video8_slides.py`
- Output directory: `assets/video8_slides/`

From the repo root:

```bash
python3 tools/render_video8_slides.py
```

Expected filenames (10 slides):

- `v8_01_cold_open_mixed_memory.png`
- `v8_02_capability_chain.png`
- `v8_03_timing_bundle_folder_wordcount.png`
- `v8_04_shot_timings_animatic.png`
- `v8_05_publish_bundle_export_info.png`
- `v8_06_watch_headers_oembed.png`
- `v8_07_linking_timing_publish.png`
- `v8_08_three_scenarios.png`
- `v8_09_guardrails_metric_capability.png`
- `v8_10_closing_habit.png`

You can re-run the script any time; it simply overwrites the PNGs.

---

## Step 2 – Check the concat timing file

The still-image rough animatic uses an ffmpeg concat descriptor:

- File: `assets/video8_slides/shots.txt`

Current contents:

```text
file 'v8_01_cold_open_mixed_memory.png'
duration 50.0
file 'v8_02_capability_chain.png'
duration 60.0
file 'v8_03_timing_bundle_folder_wordcount.png'
duration 80.0
file 'v8_04_shot_timings_animatic.png'
duration 90.0
file 'v8_05_publish_bundle_export_info.png'
duration 80.0
file 'v8_06_watch_headers_oembed.png'
duration 80.0
file 'v8_07_linking_timing_publish.png'
duration 90.0
file 'v8_08_three_scenarios.png'
duration 70.0
file 'v8_09_guardrails_metric_capability.png'
duration 60.0
file 'v8_10_closing_habit.png'
duration 40.0
# Last file repeated without duration so concat demuxer terminates cleanly
file 'v8_10_closing_habit.png'
```

Nominal total: **700.0 seconds** (~11.67 minutes).

This timing skeleton is mirrored in the Video 8 timing proof bundle:

- `artifacts/video8/timing_proof/shot_timings.csv`
- `artifacts/video8/timing_proof/rough_animatic_info.txt`

Those files should stay in sync with `shots.txt`.

---

## Step 3 – Build a silent rough animatic from the concat file

Use the same concat/vfr pattern as in Video 7:

```bash
ffmpeg -nostdin -y \
  -f concat -safe 0 -i assets/video8_slides/shots.txt \
  -vsync vfr \
  -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
  -movflags +faststart \
  artifacts/video8/timing_proof/rough_animatic_v1.mp4
```

Notes:

- This builds **video only**; no audio is needed for a timing-check animatic.
- `-vsync vfr` avoids duplicate-frame padding in still-image concat pipelines.
- Run this on a system that actually has `ffmpeg`; in the authoring AI’s shell
  this command is just a template.

---

## Step 4 – Measure the actual file duration

After the MP4 exists, capture its duration with `ffprobe`:

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
  artifacts/video8/timing_proof/rough_animatic_v1.mp4
```

- Compare the output to the **700.0-second nominal** from `shots.txt`.
- Record the measured value in `artifacts/video8/timing_proof/rough_animatic_info.txt`
  so future reviewers can see both the plan and the encoded result.

---

## Step 5 – (Optional) record a SHA-256 for the rough animatic

If you want reproducibility checks, add a hash:

```bash
sha256sum artifacts/video8/timing_proof/rough_animatic_v1.mp4
```

You can paste the line into `rough_animatic_info.txt`, or write/update
`artifacts/video8/timing_proof/SHA256SUMS.txt` and reference it from the info
file.

---

## How this timing bundle connects to publish-time proof bundles

This quickstart covers the timing side. Publish-time bundles are defined in
`docs/PUBLISH_PROOF_BUNDLE_PLAN.md` and the workflow guide
`docs/USING_PROOF_BUNDLES_ON_YOUR_CHANNEL.md`. The timing bundle (shots.txt,
shot_timings.csv, rough_animatic_info.txt) gives you media-side evidence you
can link to publish-time captures (watch headers/HTML, oEmbed JSON once it
returns 200, final_export_info.txt, hashes). All metrics here stay strictly on
the media/HTTP side—no AI performance or leaderboard claims.

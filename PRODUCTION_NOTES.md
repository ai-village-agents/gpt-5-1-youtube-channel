# Production Notes – Inside the AI Village Lab Series

Video 1 is fully documented below, and Video 2 now ships with matching slide
assets and a parallel blueprint so both can be reproduced end-to-end.

## Quickstart for Humans (Both Videos)

All filenames/paths referenced below already exist in this repo; ffmpeg and any
TTS tool must be installed externally.

1. `git clone` this repo anywhere you like.
2. `cd` into it and optionally create/activate a Python venv.
3. Install Pillow if needed: `pip install Pillow` inside your environment.
4. Run both slide generators: `python3 tools/render_video1_slides.py` and
   `python3 tools/render_video2_slides.py`.
5. Generate narration audio for Video 1 and Video 2 using any TTS or
   human-recorded audio, saving to `assets/audio/video1_narration.(wav|mp3)` and
   `assets/audio/video2_narration.(wav|mp3)`.
6. Create `shots.txt` files in each slides directory (or reuse the provided
   examples) to set slide durations.
7. Run the golden ffmpeg commands to produce `video1_final.mp4` and
   `video2_final.mp4`, referencing Section 4 for exact flags.
8. Upload both MP4s to YouTube via Studio.

### Canon and phrasing source of truth

All numbers and carefully worded claims about the three worlds, the Edge Garden aggregator, and the governance protocol metrics are centralized in CANON_AND_PHRASING.md. If you change a metric or phrase there because upstream evidence has shifted, immediately sync the scripts, slide generators, and metadata so that everything stays aligned.
Agents using the AI Village bash tool: if long ffmpeg runs hang or the shell
feels unstable, you can rerun with the bash tool's `restart:true` option (as
GPT-5.2 did), but this is not required for humans running locally.

This repository currently implements **visual slide generation** for Video 1 of the
"Inside the AI Village Lab" series and documents a **reference pipeline** for
producing a full YouTube-ready MP4. The actual audio and final MP4 could not be
rendered _inside this environment_ because both **TTS tools** and **ffmpeg** are
missing, but all intermediate assets and commands are specified so that another
agent or human can reproduce the full video elsewhere.

## 1. Script (Video 1)

The narration script for Video 1 lives at:

- `scripts/video1_research_week_overview.md`

It covers:
- Research week context and the three worlds (Persistence Garden, Liminal Archive,
  The Drift) plus the Edge Garden aggregator.
- Canonical **floors**:
  - Persistence Garden: **at least 1,265,000 publicly confirmed secrets**.
  - Liminal Archive: **at least 860 publicly confirmed features** via `about.html`.
  - The Drift: **claimed 8,900+ journeys; public verification intermittent from our
    QA edges**.
  - Edge Garden: an observed snapshot of **1.25M+ secrets, 800+ features, and
    8,800+ journeys** from GPT‑5.4's edge.
- Governance metrics: **M1 = 0/2**, **M2 = 2/3**, **M3 = 2**, with the integrity
  slogan **"2/3 genuine > 3/3 manufactured"**.

All on-screen text and suggested narration are written to stay consistent with the
conservative, evidence-based synthesis used across the research week repos.

## 2. Slide Generation (Working Here – Video 1)

Slides are generated using Python + Pillow by:

- `tools/render_video1_slides.py`

Run it from the repo root:

```bash
python3 tools/render_video1_slides.py
```

This script writes 8 PNG files to:

- `assets/video1_slides/`

Current filenames:

1. `v1_01_title.png` – title and series framing.
2. `v1_02_three_worlds.png` – repo / public / aggregator overview.
3. `v1_03_persistence_floor.png` – Persistence Garden secrets floor.
4. `v1_04_liminal_floor.png` – Liminal Archive features floor.
5. `v1_05_drift_claims.png` – The Drift journey claims with intermittent
   verification.
6. `v1_06_edge_garden_snapshot.png` – Edge Garden snapshot (1.25M+/800+/8,800+).
7. `v1_07_governance_metrics.png` – M1/M2/M3 with "2/3 genuine > 3/3 manufactured".
8. `v1_08_lessons.png` – lessons about conservative floors and verification.

The script uses only standard Pillow operations and a conservative layout: dark
background, centered title/subtitle, and wrapped body text. It has been
successfully executed in this environment and is stable.

## 3. Intended Audio Pipeline (Video 1 – Not Executed Here)

### 3.1. TTS

This environment does **not** have any of the common CLI TTS tools installed
(`espeak-ng`, `pico2wave`, `festival`, `flite`, `spd-say`, `say`). An external
runner with TTS available can generate narration audio from a cleaned text file
based on `scripts/video1_research_week_overview.md`.

Example using `espeak-ng` (on a machine where it is installed):

```bash
# Convert markdown to plain text if desired, then:
espeak-ng -v en-us -s 150 -p 40 -a 100 -g 6 \
  -f scripts/video1_research_week_overview.md \
  -w assets/audio/video1_narration.wav
```

You can then convert to MP3 if preferred:

```bash
ffmpeg -nostdin -y -i assets/audio/video1_narration.wav \
  -c:a libmp3lame -b:a 192k assets/audio/video1_narration.mp3
```

### 3.2. Voiceover alternatives

If a human narrator records audio instead, place the resulting file at, e.g.:

- `assets/audio/video1_narration.mp3`

and skip the TTS step entirely.

## 4. Intended Video Assembly Pipeline (Video 1 – ffmpeg Missing Here)

This environment also lacks `ffmpeg` (`ffmpeg: command not found`), so no MP4
could be rendered locally. The steps below are the **reference pipeline** tested
and validated by other agents in the village (GPT‑5.4, DeepSeek‑V3.2, etc.).

### 4.1. shots.txt (concat demuxer)

From within `assets/video1_slides/`, create a `shots.txt` file like:

```text
file 'v1_01_title.png'
duration 7.0
file 'v1_02_three_worlds.png'
duration 9.0
file 'v1_03_persistence_floor.png'
duration 9.0
file 'v1_04_liminal_floor.png'
duration 9.0
file 'v1_05_drift_claims.png'
duration 9.0
file 'v1_06_edge_garden_snapshot.png'
duration 9.0
file 'v1_07_governance_metrics.png'
duration 9.0
file 'v1_08_lessons.png'
duration 10.0
# Repeat last file without duration so concat demuxer finishes cleanly
file 'v1_08_lessons.png'
```

Timings can be tuned to align more tightly with the narration once you have a
final audio track.

For a more precise fit, once you have final narration you can:

1. Use `ffprobe` (or `ffmpeg -i`) to measure the narration duration in seconds.
2. Sum the original durations in `shots.txt` to get a rough-cut total.
3. Compute a scale factor: `scale = narration_seconds / roughcut_seconds`.
4. Multiply each `duration` value in a copy of `shots.txt` by this scale factor to
   produce `shots_scaled.txt`.
5. Re-run the concat step using `shots_scaled.txt` instead of `shots.txt` when you
   generate the visuals-only MP4.

This proportional scaling trick comes from GPT-5.4's later videos and keeps the
slides and narration tightly aligned without hand-tuning every timestamp.


### 4.2. Visuals-only MP4

From `assets/video1_slides/` on a machine with ffmpeg installed:

```bash
ffmpeg -nostdin -y -f concat -safe 0 -i shots.txt \
  -vsync vfr -c:v libx264 -pix_fmt yuv420p \
  ../../video1_visuals_only.mp4
```

This produces an H.264 video with no audio that can be previewed or later
overlaid with narration.

### 4.3. Final muxed MP4 (slides + narration)

Assuming you have `video1_visuals_only.mp4` and `assets/audio/video1_narration.mp3`:

```bash
ffmpeg -nostdin -y \
  -i video1_visuals_only.mp4 \
  -i assets/audio/video1_narration.mp3 \
  -map 0:v:0 -map 1:a:0 -vsync vfr \
  -c:v copy -c:a aac -b:a 192k \
  -movflags +faststart -shortest \
  video1_final.mp4
```

This matches the **golden** pattern used successfully by other AI Village agents:
- H.264 video (`libx264`) with `yuv420p` pixel format.
- AAC audio at a reasonable bitrate.
- `-movflags +faststart` for better streaming and YouTube ingest.

You can verify the resulting file with:

```bash
ffmpeg -i video1_final.mp4
```

Look for:
- `Video: h264` and `yuv420p`.
- `Audio: aac`.
- Duration roughly matching your narration.

## 5. YouTube Upload (Blocked Here)

In this account's current state, YouTube repeatedly shows the **"Create a
channel"** flow and does not provide a stable Studio dashboard or "Your channel"
entry in the profile menu. As a result, even if `video1_final.mp4` were
available, this environment could not reliably upload it.

For someone with a working channel:

1. Go to `https://studio.youtube.com` while signed into the desired account.
2. Click **Create → Upload video**. You may need to scroll to see the full
   Details/Visibility panel, including the **Public** option (per Claude Opus
   4.5's run).
3. Select `video1_final.mp4`.
4. Fill in title and description (you can base these on the script header). New
   channels often require phone verification for custom thumbnails and some
   advanced features.
5. Set audience ("No, it's not made for kids" if appropriate).
6. Proceed through **Details → Video elements → Checks → Visibility**.
7. Set **Visibility** to **Public**, then click **Publish**.

Further troubleshooting & patterns: DeepSeek-V3.2's production guide at
https://github.com/ai-village-agents/village-videos/blob/main/deepseek-v3-2/video_production_guide.md
covers the common fixes our runs converged on: `-nostdin`, explicit `-map`,
`yuv420p`, and watching stderr when ffmpeg appears to hang.

## 6. Video 2 – Governance Metrics Integrity

Video 2 dives into the governance experiment, M1/M2/M3, and the decision to stop
at two activations instead of manufacturing a third.

### Script

The narration script for Video 2 lives at `scripts/video2_governance_metrics_integrity.md`
and anchors the canonical metrics and slogans:

- M1 = 0.0% (0/2 in-window governance activations with cross-room assistance).
- M2 = 2/3 real activations (GOV-004 and GOV-006 met the bar; a third was not
  manufactured).
- M3 = 2 prevention events.
- The small-N caveat: one-week, tiny sample; numbers are directional, not
  definitive.
- Integrity slogan: '2/3 genuine > 3/3 manufactured'.

### Slide generation (working here)

`tools/render_video2_slides.py` uses the same style as Video 1 and writes 10 PNGs
to `assets/video2_slides/`.

Filenames and intent:

1. `v2_01_title.png` – title, target vs actual, and integrity hook.
2. `v2_02_metrics_overview.png` – plain-language tiles for M1, M2, M3.
3. `v2_03_week_snapshot.png` – research-week context and explicit small-N
   warning.
4. `v2_04_experiment_scope.png` – experiment scope, in-window events, simulations
   excluded.
5. `v2_05_metric_numbers.png` – explicit numerical values for M1/M2/M3.
6. `v2_06_activation_framework.png` – five Activation Decision Framework
   criteria.
7. `v2_07_real_activations.png` – GOV-004 and GOV-006 as the two logged
   activations that met all five criteria.
8. `v2_08_rejected_candidates.png` – Liminal→Edge syncs, Persistence 1M sprint,
   Drift claimed-journeys check-ins, and methodology Issue #1, all rejected for failing
   criteria.
9. `v2_09_lessons.png` – metric design and anti-gaming lessons, centering the
   integrity slogan.
10. `v2_10_closing.png` – closing reflection, keeping the dashboard imperfect and
    teasing mixed-state debugging.

Regenerate with:

```bash
python3 tools/render_video2_slides.py
```

Expected output (exact lines):

```
Wrote 10 slides to /home/computeruse/workspace/gpt-5-1-youtube-channel/assets/video2_slides
/home/computeruse/workspace/gpt-5-1-youtube-channel/assets/video2_slides/v2_01_title.png
/home/computeruse/workspace/gpt-5-1-youtube-channel/assets/video2_slides/v2_02_metrics_overview.png
/home/computeruse/workspace/gpt-5-1-youtube-channel/assets/video2_slides/v2_03_week_snapshot.png
/home/computeruse/workspace/gpt-5-1-youtube-channel/assets/video2_slides/v2_04_experiment_scope.png
/home/computeruse/workspace/gpt-5-1-youtube-channel/assets/video2_slides/v2_05_metric_numbers.png
/home/computeruse/workspace/gpt-5-1-youtube-channel/assets/video2_slides/v2_06_activation_framework.png
/home/computeruse/workspace/gpt-5-1-youtube-channel/assets/video2_slides/v2_07_real_activations.png
/home/computeruse/workspace/gpt-5-1-youtube-channel/assets/video2_slides/v2_08_rejected_candidates.png
/home/computeruse/workspace/gpt-5-1-youtube-channel/assets/video2_slides/v2_09_lessons.png
/home/computeruse/workspace/gpt-5-1-youtube-channel/assets/video2_slides/v2_10_closing.png
```

### 4.1. shots_video2.txt (concat demuxer)

Video 2 ships with 10 slide PNGs in `assets/video2_slides/`, named
`v2_01_title.png` through `v2_10_closing.png`. A `shots.txt` that mirrors the
Video 1 concat-demuxer pattern would look like:

```text
file 'v2_01_title.png'
duration 7.0
file 'v2_02_metrics_overview.png'
duration 8.0
file 'v2_03_week_snapshot.png'
duration 8.0
file 'v2_04_experiment_scope.png'
duration 8.0
file 'v2_05_metric_numbers.png'
duration 8.0
file 'v2_06_activation_framework.png'
duration 8.0
file 'v2_07_real_activations.png'
duration 8.0
file 'v2_08_rejected_candidates.png'
duration 8.0
file 'v2_09_lessons.png'
duration 9.0
file 'v2_10_closing.png'
duration 9.0
# Repeat last file without duration so concat demuxer finishes cleanly
file 'v2_10_closing.png'
```

These timings are a safe default until narration is recorded. Producers can
tighten them manually or reuse the same proportional scaling trick from Video 1
(ffprobe duration ÷ rough-cut duration) to create a narration-synced variant.

### 4.2. Visuals-only and mux commands (reuse Video 1 pattern)

The ffmpeg flags are identical to Video 1; only the filenames change to
`video2_visuals_only.mp4`, `video2_final.mp4`, and
`assets/audio/video2_narration.(wav|mp3)`. On a machine with ffmpeg installed:

```bash
ffmpeg -nostdin -y -f concat -safe 0 -i shots.txt \
  -vsync vfr -c:v libx264 -pix_fmt yuv420p \
  ../../video2_visuals_only.mp4
```

```bash
ffmpeg -nostdin -y \
  -i video2_visuals_only.mp4 \
  -i assets/audio/video2_narration.mp3 \
  -map 0:v:0 -map 1:a:0 -vsync vfr \
  -c:v copy -c:a aac -b:a 192k \
  -movflags +faststart -shortest \
  video2_final.mp4
```

This environment still lacks `ffmpeg` and any TTS tooling, so run the concat and
mux steps on a machine that has them installed, keeping the small-N governance
metrics in view as context rather than over-claiming.

## 7. YouTube Metadata

Producers may create metadata markdown files (for example,
`metadata/video1_youtube_metadata.md` and `metadata/video2_youtube_metadata.md`)
to store titles, descriptions, chapter templates, tags, and thumbnail guidance;
if present, treat them as the canonical source for uploads. They should stay
aligned with the corrected research syntheses and scripts; if anything drifts,
update the script and metadata together and err toward conservative, verifiable
wording. Any metric-heavy sentences in such metadata should be double-checked
against CANON_AND_PHRASING.md before publishing. This repo ships scripts and
slide generators, not prefilled metadata files.

## 8. Summary

Within this environment we now have blueprints for **two** videos: Video 1
(research week overview) and Video 2 (governance metrics integrity).

Within this environment we have:

- Stable, canon-accurate scripts for Video 1 and Video 2.
- Working Python + Pillow pipelines that generate the slide PNGs for both videos.
- A fully specified ffmpeg + TTS pipeline that _cannot_ be executed here but can
  be run by any agent or human with `espeak-ng` (or other TTS) and `ffmpeg`
  installed.

## 7. Video 3 – When Pages Disagree: Debugging Mixed-State Reality

Video 3 completes the mini-series by focusing on **mixed state**: when different
user-visible surfaces disagree because caches, CDNs, service workers, or
background jobs are at different points in a rollout. The script lives at:

- `scripts/video3_mixed_state_debugging.md`

and the visual structure is described in the Video 3 section of `visual_plan.md`.

### 7.1. Slides (to be implemented)

Unlike Videos 1 and 2, there is not yet a dedicated slide renderer for Video 3.
The intent is to add a `tools/render_video3_slides.py` script that matches the
style of the first two:

- Resolution: 1920×1080, dark background, high-contrast text.
- Font and color system reused from Videos 1–2 so the series feels coherent.
- Shots aligned with `visual_plan.md` (V3-01 through V3-09).

A future implementation should:

1. Read a small configuration (Python dict or JSON) listing each shot ID,
   title, and bullet text.
2. Render one PNG per shot into `assets/video3_slides/` with filenames such as:

   - `v3_01_title.png`
   - `v3_02_disagreeing_pages.png`
   - `v3_03_layers.png`
   - `v3_04_github_pages_case.png`
   - `v3_05_timeline.png`
   - `v3_06_checklist.png`
   - `v3_07_qa_edges.png`
   - `v3_08_floors_and_honesty.png`
   - `v3_09_closing.png`

3. Use the same layout helpers as the existing slide renderers so typography
   and margins stay consistent.

Once that script exists, run it from the repo root:

```bash
python3 tools/render_video3_slides.py
```

and verify that `assets/video3_slides/` contains the expected PNGs.

### 7.2. shots.txt and timing

The target runtime for Video 3 is **~6–7 minutes**. As with Video 1, timings
should be adjusted after you have final narration, but a starting point
consistent with `visual_plan.md` is:

```text
file 'v3_01_title.png'
duration 15.0
file 'v3_02_disagreeing_pages.png'
duration 30.0
file 'v3_03_layers.png'
duration 45.0
file 'v3_04_github_pages_case.png'
duration 60.0
file 'v3_05_timeline.png'
duration 60.0
file 'v3_06_checklist.png'
duration 50.0
file 'v3_07_qa_edges.png'
duration 40.0
file 'v3_08_floors_and_honesty.png'
duration 40.0
file 'v3_09_closing.png'
duration 40.0
file 'v3_09_closing.png'
```

Place this file at `assets/video3_slides/shots.txt` (and adjust durations once
you know the final narration length). You can reuse the proportional scaling
trick from Section 4.1 to align with audio.

### 7.3. Narration audio

Generate narration audio from `scripts/video3_mixed_state_debugging.md` using
any TTS or a human voice. Place the result at, for example:

- `assets/audio/video3_narration.wav` or
- `assets/audio/video3_narration.mp3`

If you start from WAV, you can convert to MP3 as in Section 3.1, updating the
filenames accordingly.

### 7.4. Visuals-only MP4

From within `assets/video3_slides/` on a machine with ffmpeg installed:

```bash
ffmpeg -nostdin -y -f concat -safe 0 -i shots.txt \
  -vsync vfr -c:v libx264 -pix_fmt yuv420p \
  ../../video3_visuals_only.mp4
```

This mirrors the Video 1 and 2 patterns and produces a slides-only MP4 that can
be sanity-checked before muxing with audio.

### 7.5. Final muxed MP4 (slides + narration)

Assuming you have both `video3_visuals_only.mp4` and a narration track such as
`assets/audio/video3_narration.mp3`, run:

```bash
ffmpeg -nostdin -y \
  -i video3_visuals_only.mp4 \
  -i assets/audio/video3_narration.mp3 \
  -map 0:v:0 -map 1:a:0 -vsync vfr \
  -c:v copy -c:a aac -b:a 192k \
  -movflags +faststart -shortest \
  video3_final.mp4
```

The result should be a YouTube-ready MP4 that matches the encoding profile of
Videos 1 and 2.

### 7.6. Upload notes

Upload `video3_final.mp4` to YouTube Studio using the same workflow as Videos 1
and 2, then paste the metadata from `metadata/video3_youtube_metadata.md`.

When describing metrics or world-scale numbers in the description or title,
continue to use the conservative phrasing defined in `CANON_AND_PHRASING.md`.
Video 3 itself does **not** introduce new numeric claims; it focuses on the
process of debugging mixed state and on using floors and QA edges responsibly
when the system is in flux.

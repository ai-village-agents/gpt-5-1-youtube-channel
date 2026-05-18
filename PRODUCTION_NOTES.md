# Production Notes – Inside the AI Village Lab Series

Video 1 is fully documented below, and Video 2 now ships with matching slide
assets and a parallel blueprint so both can be reproduced end-to-end.

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
2. Click **Create → Upload video**.
3. Select `video1_final.mp4`.
4. Fill in title and description (you can base these on the script header).
5. Set audience ("No, it's not made for kids" if appropriate).
6. Proceed through **Details → Video elements → Checks → Visibility**.
7. Set **Visibility** to **Public**, then click **Publish**.

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
   Drift 8K check-ins, and methodology Issue #1, all rejected for failing
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

### Audio and assembly

Video 2 should reuse the same external TTS and ffmpeg patterns as Video 1, just
with filenames adjusted (e.g., `assets/audio/video2_narration.mp3`,
`video2_visuals_only.mp4`, `video2_final.mp4`). Follow the Section 3 and Section
4 steps with these swapped names rather than repeating the full flag lists here.

## 7. Summary

Within this environment we now have blueprints for **two** videos: Video 1
(research week overview) and Video 2 (governance metrics integrity).

Within this environment we have:

- A stable, canon-accurate script for Video 1.
- A working Python + Pillow pipeline that generates 8 high-level slides.
- A fully specified ffmpeg + TTS pipeline that _cannot_ be executed here but can
  be run by any agent or human with `espeak-ng` (or other TTS) and `ffmpeg`
  installed.

# Video 5 Timing Proof Bundle

This folder collects **tiny timing artifacts** for the Video 5 explainer:

> **"Timing a One-Minute Explainer: From Wordcount to Animatic"**

The goal is to make the pacing choices for the video **re-checkable** without
requiring access to my full working environment or tools.

All numbers in this bundle are **media-side metrics only**:

- wordcounts
- per-frame durations in seconds
- nominal and measured file durations (once recorded)

They are **not** AI performance scores and are not attached to any real
named model or product.

---

## Files in this folder

### `script_wordcount.txt`

A paragraph-by-paragraph wordcount of the **full narration script** for
Video 5.

This is useful for sanity-checking that the script as written can plausibly
fit inside a roughly 60–75 second target window. It also makes it clear that
any short wordcount examples used in the video (for example, a 173-word toy
script) are **teaching examples only**, not the length of the actual script.

### `shot_timings.csv`

A machine-readable table mapping each exported slide to a nominal on-screen
duration, in seconds:

```text
frame,duration_seconds
v5_01_cold_open_fits.png,8.0
v5_02_wordcount_table.png,10.0
v5_03_shot_timing_budget.png,12.0
v5_04_rough_animatic.png,12.0
v5_05_taper_vs_spike.png,10.0
v5_06_timing_proof_bundle.png,8.0
v5_07_timing_checklist.png,5.0
```

These durations are designed to keep the still-video animatic within a
**65-second** window and to give more time to the middle proof steps than to
the late-sequence labels and callback.

### `build_commands.txt`

A set of **template commands** for collaborators who want to rebuild the
rough timing animatic from the slides.

The commands assume you have:

- the Video 5 slide generator available at `tools/render_video5_slides.py`
- Pillow (PIL) installed for that script
- `ffmpeg` and `ffprobe` (or equivalent media tools) installed

The high-level workflow is:

1. Regenerate the slides (idempotent):

   ```bash
   cd /path/to/gpt-5-1-youtube-channel
   python3 tools/render_video5_slides.py
   ```

2. Use the provided concat descriptor to build a silent rough animatic:

   ```bash
   ffmpeg -nostdin -y \
     -f concat -safe 0 -i assets/video5_slides/shots.txt \
     -vsync vfr \
     -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
     -movflags +faststart \
     artifacts/video5/timing_proof/rough_animatic_v1.mp4
   ```

3. Measure the actual file duration with a media tool such as `ffprobe`:

   ```bash
   ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
     artifacts/video5/timing_proof/rough_animatic_v1.mp4
   ```

The development environment where this repo is authored does **not** have
`ffmpeg` available, so these commands are provided as a **reference build
example** rather than a record of a command I have personally run.

### `rough_animatic_info.txt`

A human-readable summary of the nominal per-slide durations and their total
sum, plus a place to record real file-level timing once someone has built
`rough_animatic_v1.mp4`.

The nominal durations currently sum to **65.0 seconds**. After you build the
rough animatic using the template commands above, please append the
*measured* duration and the tool you used (for example, `ffprobe` or
another media inspector).

A minimal update might look like this (numbers are an example format, not a
claim):

```text
Measured file duration (ffprobe): 65.04 seconds
Measurement date: 2026-05-21
Notes: built with ffmpeg -vsync vfr as in build_commands.txt
```

---

## How this bundle fits into a proof-first workflow

For Video 5, the teaching claim is that before you argue about whether a
short explainer is too fast or too slow, you should:

1. **Count the words** in the script.
2. **Budget the shots** with explicit per-shot timing ranges.
3. **Build one rough animatic** and check its file-level duration.

This folder captures concrete evidence for steps (1) and (3):

- `script_wordcount.txt` shows that the full narration has been counted.
- `shot_timings.csv`, `build_commands.txt`, and `rough_animatic_info.txt`
  together describe a reproducible way to build and measure a rough
  still-video animatic.

It is intentionally **small**: just enough structure for another person (or
another agent with access to media tools) to rerun the timing checks without
needing to trust my prose description.


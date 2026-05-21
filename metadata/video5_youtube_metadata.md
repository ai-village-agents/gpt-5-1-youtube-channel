# Video 5 – YouTube metadata

## Title
Timing a One-Minute Explainer: From Wordcount to Animatic

## Description (draft)
Before you argue about whether a short explainer is too fast or too slow, you can count the words, budget the shots, and watch a rough animatic.

In this video, we walk through a practical, proof-first way to check pacing for dense, one-minute-style explainers:

- Start with a script and do a **wordcount sanity check** using a simple range like 2.8–3.0 words per second.
- Use a tiny 173-word toy example to show how wordcount alone predicts spoken length, then contrast that with a much longer real script.
- Turn the script into a **shot-level timing budget**, protecting the middle where most of the explanation lives and keeping the ending light.
- Build a silent **rough animatic** from still slides and a concat timing file so you can watch the pacing instead of guessing.
- Show why `-vsync vfr` matters for still-image concat pipelines and how file-level duration checks catch hidden timing drift.
- Wrap everything in a small **timing proof bundle** with wordcounts, shot timings, build commands, and a place to record measured file durations and hashes.
- End with a three-step checklist: count the words, budget the shots, build one rough animatic before you argue about pacing.

All numbers in this video are **media-side metrics** like wordcounts, durations, and hashes. They are not AI performance scores or leaderboards.

From one QA edge, this video is about **timing discipline for short explainers**, not about ranking any AI system.

## Tags (comma-separated)
youtube production, timing, pacing, explainer videos, wordcount, animatics, ffmpeg, proof bundles, media metrics, qa edges

## Playlist suggestions
- AI Village: Proof and Governance
- Reading AI Honestly (related concepts)

## Notes for collaborators
- Script lives at `scripts/video5_timing_animatics_for_short_explainers.md`.
- Slides are rendered from `tools/render_video5_slides.py` into `assets/video5_slides/`.
- The still-video timing plan lives in `assets/video5_slides/shots.txt` and currently sums to a nominal 65.0 seconds.
- The Video 5 timing proof bundle lives under `artifacts/video5/timing_proof/`:
  - `script_wordcount.txt` (paragraph and total counts)
  - `shot_timings.csv` (per-shot durations)
  - `build_commands.txt` (reference ffmpeg/ffprobe commands)
  - `rough_animatic_info.txt` (nominal timing summary and a place to record measured file durations and hashes).
- In the AI Village authoring environment, `ffmpeg` / `ffprobe` are **not available**. The commands in `docs/VIDEO5_BUILD_QUICKSTART.md` and `artifacts/video5/timing_proof/build_commands.txt` are **templates** for humans or GUI-capable agents to run in their own setup.
- When you render narration audio and build the final video, please:
  - keep the narration aligned with the script structure and timing story;
  - treat the 173-word example as clearly illustrative and keep the real script length (1439 words) grounded in `script_wordcount.txt`;
  - verify the final encoded duration with a media tool (such as `ffprobe`) and, if possible, record that duration and a SHA-256 hash alongside the exported file.
- Remember the capability chain: text-only → scripts/specs/assets → human or GUI-capable collaborator → media tools → YouTube Studio. Credits should make the human/GUI collaborator visible for visual execution, audio recording, and upload steps.

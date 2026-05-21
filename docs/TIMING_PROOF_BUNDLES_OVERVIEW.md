# Timing Proof Bundles Overview
Timing proof bundles are media-side evidence packages about pacing and structure: they track wordcounts, shot timings, rough animatic durations, and optional hashes so collaborators can verify the rhythm of a short explainer. They are explicitly not AI performance metrics or leaderboard claims.

## Core ingredients
- Script wordcount breakdown (per paragraph plus total) to ground the expected narration length.
- Concat/timing file (e.g., `shots.txt`) paired with a CSV mirror so timings are easy to diff and plot.
- Rough animatic MP4 built from stills to show the nominal pacing before voiceover.
- Text summary file (e.g., `rough_animatic_info.txt`) that records nominal vs measured duration and, optionally, a SHA-256 of the rendered animatic.
- Pointers to any loudness or QC checks if audio exists, so reviewers know where to look for waveform evidence.

## How this shows up in this repo
### Video 4 – Claim-level proof example
Video 4 focuses on claim-level proof bundles using synthetic Systems X/Y. Its timing/proof example lives under `artifacts/video4/proof_examples/`, with synthetic CSV, plot, and hash artifacts that illustrate the format.

### Video 5 – Timing proof bundle
Video 5 includes a full timing proof bundle under `artifacts/video5/timing_proof/`: `script_wordcount.txt` (1439-word total); `shot_timings.csv` and `assets/video5_slides/shots.txt` (both summing to 65.0 seconds nominal); `rough_animatic_info.txt` with blanks for collaborator-measured `ffprobe` duration and SHA-256; and `build_commands.txt` with template `ffmpeg`/`ffprobe` invocations.

## For future videos
- Count words by paragraph and record the total.
- Lock a concat/timing file and mirror it in CSV form.
- Build a still-image animatic with `-vsync vfr`, then measure it.
- Record duration and hash in a text file alongside the animatic info.
- Keep everything together in a single `timing_proof/` directory for easy review.

All numbers here are media-side metrics (wordcounts, timings, hashes), not model scores or capability claims.

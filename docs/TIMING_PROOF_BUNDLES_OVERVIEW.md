# Timing Proof Bundles Overview
Timing proof bundles are media-side evidence packages about pacing and structure: they track wordcounts, shot timings, rough animatic durations, and optional hashes so collaborators can verify the rhythm of a short explainer. They are explicitly not AI performance metrics or leaderboard claims.

## Core ingredients
- Script wordcount breakdown (per paragraph plus total) to ground the expected narration length.
- Concat/timing file (e.g., `shots.txt`) paired with a CSV mirror so timings are easy to diff and plot.
- Rough animatic MP4 built from stills to show the nominal pacing before voiceover.
- Text summary file (e.g., `rough_animatic_info.txt`) that records nominal vs measured duration and, optionally, a SHA-256 of the rendered animatic.
- Pointers to any loudness or QC checks if audio exists, so reviewers know where to look for waveform evidence.

All of these numbers are media-side metrics (wordcounts, timings, hashes). None of them are model scores or capability benchmarks.

## How this shows up in this repo
### Video 4 – Claim-level proof example
Video 4 focuses on claim-level proof bundles using synthetic Systems X/Y. Its timing/proof example lives under `artifacts/video4/proof_examples/`, with synthetic CSV, plot, and hash artifacts that illustrate the format.

The intent is to show *shape*, not to report on any real model. Every number in that directory is fictional and clearly documented as such.

### Video 5 – Timing proof bundle
Video 5 includes a full timing proof bundle under `artifacts/video5/timing_proof/`.

The key pieces are:
- `script_wordcount.txt` – paragraph-level counts for the **1439-word** Video 5 script.
- `shot_timings.csv` – a filename + duration table for the seven-slide still-image animatic, summing to **65.0 seconds nominal**.
- `assets/video5_slides/shots.txt` – the concat descriptor that matches `shot_timings.csv` line-for-line.
- `rough_animatic_info.txt` – a text summary that now:
  - lists the nominal per-shot durations,
  - records **nominal cumulative timing windows** (for example, `v5_05_taper_vs_spike.png: 0:42.0–0:52.0 (10.0s)`),
  - states the nominal total of **65.0 seconds**, and
  - leaves explicit blanks for a collaborator to fill in the **measured file duration** and **SHA-256 hash** once they build `rough_animatic_v1.mp4` and run media tools.
- `build_commands.txt` – template `ffmpeg` / `ffprobe` commands that a human or GUI-capable agent can run in an environment where those tools are actually installed.

Two clarifications that matter for metric honesty:
- The **65.0-second still-image animatic** is a compact, seven-shot teaching sequence that demonstrates how to budget and inspect timing. It is not a promise that the entire 1439-word script is delivered in 65 seconds.
- Within the narration we also use a **173-word toy example** to teach words-per-second math. That 173-word text is an *illustrative subset*, not the full script. The timing proof bundle is anchored on the real script wordcount and the separate 65.0-second animatic asset.

### Video 7 – Evidence-chain timing bundle
Video 7 extends this pattern to a longer, ~11.3-minute explainer about building a full evidence chain from script to watch page.

Its timing proof bundle lives under `artifacts/video7/timing_proof/` and includes:

- `script_wordcount.txt` – paragraph-level counts for the **1829-word** Video 7 script.
- `shot_timings.csv` – a filename + duration table for the ten-slide still-image animatic, summing to **680.0 seconds nominal**, matching `assets/video7_slides/shots.txt`.
- `rough_animatic_info.txt` – nominal cumulative timing windows and blanks for a measured duration and SHA-256 once collaborators build the rough animatic.
- `build_commands.txt` – reference `ffmpeg` / `ffprobe` / `sha256sum` commands collaborators can run to produce and measure `rough_animatic_v1.mp4`.

Video 7’s script also ties this timing layer explicitly to the publish-time bundle plan in `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`, so viewers see how planning, local build, and publish-time evidence connect.

## For future videos
- Count words by paragraph and record the total.
- Lock a concat/timing file and mirror it in CSV form.
- Build a still-image animatic with `-vsync vfr`, then measure it.
- Record duration and hash in a text file alongside the animatic info.
- If it helps review, add **nominal cumulative timing windows** derived from the CSV so you can talk about specific segments (for example, "Shot 6 lives roughly from 0:27.5–0:40.0"). Make sure those windows are clearly labeled as *nominal* unless they come from measured media.
- Keep everything together in a single `timing_proof/` directory for easy review.

Throughout, stay strict about scope:
- Timing proof bundles speak about media artifacts (scripts, images, audio, video) and their measurable properties.
- They do **not** make or support new AI performance leaderboards.

## Minimal “bundle ready” checklist

Before you treat a timing proof bundle as “done enough to trust,” you can run a
small checklist. It does not add new kinds of data; it just checks that the
pieces you already planned to capture are present and consistent.

1. **Script anchored:** `script_wordcount.txt` exists, records a total word
   count, and notes how/when you measured it (for example, `wc -w` on a
   specific file on a specific date).
2. **Timings aligned:** `shot_timings.csv` and your concat file (for example,
   `assets/.../shots.txt`) list the **same files in the same order**, and the
   durations in both places sum to the same nominal total.
3. **Animatic described:** at least one rough animatic file exists on disk
   (even if it is gitignored), and `rough_animatic_info.txt`:
   - names the file you measured,
   - records the nominal total duration, and
   - either contains the measured duration + hash or leaves an explicit blank
     ready to be filled in later.
4. **Commands captured:** `build_commands.txt` (or an equivalent snippet)
   shows the commands and key flags a collaborator used last time they
   regenerated the animatic and measurements, so another person could repeat
   the process on the same media.
5. **Optional cross-link:** if you already have a publish-time bundle for the
   same video, `rough_animatic_info.txt` mentions its folder path, and
   `final_export_info.txt` in that publish-time bundle points back to the
   timing folder.

If those boxes are checked, you have enough structure that a future reviewer
can recompute or spot-check your timings without relying on anyone’s memory,
while still staying firmly in the world of media-side metrics.

### Who does what (typical roles)
- **Script author** – keeps the script stable and makes sure `script_wordcount.txt` exists with a note on how the wordcount was measured.
- **Timing/animatic collaborator** – keeps `shot_timings.csv` matched to the concat file, builds the rough animatic, fills in `rough_animatic_info.txt`, and updates `build_commands.txt` when their build/measurement steps change.
- **Publish-time capture collaborator** – optional at this layer, but adds cross-links between timing bundles and any publish-time bundles once uploads exist.

One person can cover multiple roles; naming them just clarifies which checklist items are on them. For reference shapes, see `artifacts/video5/timing_proof/`, `artifacts/video7/timing_proof/`, and `artifacts/video8/timing_proof/`.

# Video 7 – From Script to Watch Page: Building a Full Evidence Chain

Working title for the channel index and metadata:

> **From Script to Watch Page: Building a Full Evidence Chain**

This video extends Videos 5 and 6:

- Video 5: timing proof bundles for short explainers (wordcount + rough animatic).
- Video 6: publish-time proof bundles for YouTube (watch headers/HTML + oEmbed + export info).
- Video 7: how those layers combine into a **full evidence chain**, moving from planning → local build → publish-time capture, and how that helps when memories disagree with what the watch page shows.

All examples use **media and HTTP metrics only** (wordcounts, nominal/measured durations, hashes, HTTP status codes, timestamps). No AI performance metrics or model leaderboards.

## Slide list (draft)

Naming convention: `v7_XX_short_label.png`.

1. **Cold open: disagreement**  – `v7_01_mixed_memory_cold_open.png`
   - Visual: Split screen between a sticky note saying “~10 minutes, playlist A+B” and a watch page UI showing “11:02” and only playlist A.
   - Text: “You remember exactly what you uploaded. The numbers disagree.”

2. **Three stories** – `v7_02_three_stories.png`
   - Visual: Three boxes labelled “Memory”, “Live watch page”, “Evidence bundle”.
   - Text: why relying on the first two alone leads to arguments.

3. **Three layers overview** – `v7_03_three_layers_overview.png`
   - Visual: stacked boxes: Planning → Local build → Publish-time.
   - Text: short bullets describing each layer.

4. **Planning evidence: scripts + wordcounts** – `v7_04_planning_evidence.png`
   - Visual: file tree snippet with `script.md` and `script_wordcount.txt` highlighted.
   - Text: script paragraphs, total words, simple timing range (e.g., 7–9 minutes at 2.5–3.0 w/s).

5. **Local build: timing bundles** – `v7_05_timing_bundles.png`
   - Visual: CSV rows and a timeline bar; nod to Video 5.
   - Text: shot timings, nominal windows, rough animatic duration, SHA-256 of the animatic file.

6. **Publish-time: watch page bundle** – `v7_06_publish_time_bundle.png`
   - Visual: small folder tree rooted at `artifacts/publish_proof/videoX/...`.
   - Text: watch headers/body, oEmbed JSON, final_export_info.txt, SHA256SUMS.txt; nod to Video 6.

7. **Case study: resolving “I’m sure it was shorter”** – `v7_07_case_study_mismatch.png`
   - Visual: side-by-side comparison panel: planning range vs animatic duration vs watch page duration.
   - Text: walk through how the three layers resolve the dispute.

8. **Guardrails: what this evidence can and cannot say** – `v7_08_guardrails.png`
   - Visual: two columns labelled “In scope” and “Out of scope”.
   - In scope: wordcounts, durations, hashes, HTTP statuses.
   - Out of scope: model rankings, benchmark scores, “AI X vs AI Y”.

9. **Five-step habit checklist** – `v7_09_five_step_habit.png`
   - Visual: numbered checklist 1–5 summarising the habit from the script.

10. **Closing: reading your own notes** – `v7_10_closing_notes.png`
    - Visual: notebook labelled “Evidence chain” connected by arrows to script, MP4 icon, and watch page.
    - Text: “When numbers change under you, read your own notes.”

## Nominal timing plan (first draft)

Target total runtime: **9–11 minutes**. These durations are nominal and will later be mirrored in `assets/video7_slides/shots.txt` and `artifacts/video7/timing_proof/shot_timings.csv`.

| Slide | Filename                               | Nominal duration (s) |
| ----- | -------------------------------------- | -------------------- |
| 1     | v7_01_mixed_memory_cold_open.png       | 40.0                 |
| 2     | v7_02_three_stories.png                | 60.0                 |
| 3     | v7_03_three_layers_overview.png        | 70.0                 |
| 4     | v7_04_planning_evidence.png            | 80.0                 |
| 5     | v7_05_timing_bundles.png               | 80.0                 |
| 6     | v7_06_publish_time_bundle.png          | 90.0                 |
| 7     | v7_07_case_study_mismatch.png          | 80.0                 |
| 8     | v7_08_guardrails.png                   | 60.0                 |
| 9     | v7_09_five_step_habit.png              | 60.0                 |
| 10    | v7_10_closing_notes.png                | 60.0                 |

Nominal sum: **680 seconds** (~11:20). This can be tightened once narration pacing is clearer.

## Next assets to create

- `tools/render_video7_slides.py` – Pillow renderer matching the style of Videos 5 and 6.
- `assets/video7_slides/` – directory for the rendered PNG slides.
- `assets/video7_slides/shots.txt` – concat descriptor for still-image animatic.
- `artifacts/video7/timing_proof/` – timing-proof bundle containing:
  - `script_wordcount.txt` for the Video 7 script,
  - `shot_timings.csv` matching the table above,
  - `rough_animatic_info.txt` with nominal windows and blanks for measured duration + SHA-256,
  - `build_commands.txt` with template ffmpeg/ffprobe/sha256sum commands (to be run by collaborators with real tools).
- `metadata/video7_youtube_metadata.md` – title, description, and tags grounded in metric- and capability-honesty.

All ffmpeg, ffprobe, HTTP, and Studio operations will remain clearly delegated to humans or GUI-capable agents with real tools.

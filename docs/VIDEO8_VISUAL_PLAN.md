# Video 8 – Using Proof Bundles on Your Own Channel

Working title for the channel index and metadata:

> **Capture What You Shipped: Using Proof Bundles on Your Channel**

This video turns the proof-bundle docs into a **practical workflow** for existing channels:

- `docs/TIMING_PROOF_BUNDLES_OVERVIEW.md` – structure of timing proof bundles.
- `docs/PUBLISH_PROOF_BUNDLE_PLAN.md` – structure of publish-time proof bundles.
- `docs/USING_PROOF_BUNDLES_ON_YOUR_CHANNEL.md` – step-by-step guide for humans or GUI-capable agents.

All examples stay strictly on **media and HTTP metrics**: wordcounts, shot timings, nominal/measured durations, codecs, hashes, HTTP status lines, headers, HTML snapshots. No AI performance metrics or model leaderboards belong here.

## Slide list (draft)

Naming convention: `v8_XX_short_label.png`.

1. **Cold open – mixed memories** – `v8_01_cold_open_mixed_memory.png`
   - Visual: Cluttered desktop, overlapping "final.mp4" files, and a watch page with an 11:02 duration badge next to a sticky note that says "~10 minutes".
   - Text: "You uploaded this last week. Today the numbers disagree."

2. **What I can and can’t do** – `v8_02_capability_chain.png`
   - Visual: Three-step chain: "Text-only AI" → "Specs & templates" → "Humans / GUI agents with tools" → "YouTube".
   - Text: clear bullets for what stays in my sandbox vs what collaborators with real tools do.

3. **Timing bundles – folder + wordcount** – `v8_03_timing_bundle_folder_wordcount.png`
   - Visual: File tree with `scripts/my_video_script.md` and `artifacts/timing_proof/my_video/script_wordcount.txt` highlighted.
   - Text: one-folder-per-video and simple `wc -w` wordcount as an anchor.

4. **Timing bundles – shot timings & rough animatic** – `v8_04_shot_timings_animatic.png`
   - Visual: side-by-side CSV rows (`shot_timings.csv`) and a simple bar timeline, plus a small MP4 icon labelled `rough_animatic_v1.mp4`.
   - Text: keep `shot_timings.csv` and `shots.txt` in sync; collaborators build a silent rough animatic with `ffmpeg`.

5. **Publish bundles – folder + export info** – `v8_05_publish_bundle_export_info.png`
   - Visual: Folder tree rooted at `artifacts/publish_proof/my_video/20260522T172300Z/` with `final_export_info.txt` highlighted.
   - Text: record the export path, SHA-256 hash, encoder duration, and watch URL.

6. **Publish bundles – watch headers, HTML, oEmbed** – `v8_06_watch_headers_oembed.png`
   - Visual: Three small boxes: `watch_headers.txt`, `watch_body.html`, and `oembed.json`, with a clock icon next to oEmbed indicating it may arrive later.
   - Text: capture what the watch page and oEmbed endpoint actually served, including 404-while-fresh behaviour.

7. **Linking timing and publish bundles** – `v8_07_linking_timing_publish.png`
   - Visual: Chain labelled `script → rough animatic → final export → watch page`, with tiny folder icons under "timing" and "publish".
   - Text: cross-references from `rough_animatic_info.txt` to the publish bundle and from `final_export_info.txt` back to the timing bundle.

8. **Three scenarios** – `v8_08_three_scenarios.png`
   - Visual: Three index cards: "Wasn’t this shorter?", "Preview mismatch", and "Which file did we ship?".
   - Text: one-sentence summary of how bundles help in each case.

9. **Guardrails – metric-honest & capability-honest** – `v8_09_guardrails_metric_capability.png`
   - Visual: Two-column checklist with ticks next to media/HTTP items and a crossed-out "leaderboards" row.
   - Text: keep metrics on the media/HTTP side; make tool roles explicit.

10. **Closing – a small habit** – `v8_10_closing_habit.png`
    - Visual: A folder labelled `artifacts/` slowly filling with tiny document icons, with a calm "future you" figure reading a note.
    - Text: one small folder per video as a long-term safety net.

## Nominal timing plan (first draft)

Target total runtime: **10–12 minutes**. These durations are nominal planning values only. They will later be mirrored in:

- `assets/video8_slides/shots.txt` – concat descriptor for the still-image animatic.
- `artifacts/video8/timing_proof/shot_timings.csv` – timing proof CSV.

| Slide | Filename                              | Nominal duration (s) |
| ----- | ------------------------------------- | -------------------- |
| 1     | v8_01_cold_open_mixed_memory.png      | 50.0                 |
| 2     | v8_02_capability_chain.png            | 60.0                 |
| 3     | v8_03_timing_bundle_folder_wordcount.png | 80.0              |
| 4     | v8_04_shot_timings_animatic.png       | 90.0                 |
| 5     | v8_05_publish_bundle_export_info.png  | 80.0                 |
| 6     | v8_06_watch_headers_oembed.png        | 80.0                 |
| 7     | v8_07_linking_timing_publish.png      | 90.0                 |
| 8     | v8_08_three_scenarios.png             | 70.0                 |
| 9     | v8_09_guardrails_metric_capability.png| 60.0                 |
| 10    | v8_10_closing_habit.png               | 40.0                 |

Nominal sum: **700.0 seconds** (~11.67 minutes). This can be tightened once narration pacing is clearer.

## Next assets to create

- `tools/render_video8_slides.py` – Pillow renderer matching the style of Videos 5–7.
- `assets/video8_slides/` – directory for the rendered PNG slides.
- `assets/video8_slides/shots.txt` – concat descriptor for the still-image animatic, mirroring the table above.
- `artifacts/video8/timing_proof/` – timing-proof bundle containing:
  - `script_wordcount.txt` for the Video 8 script,
  - `shot_timings.csv` matching the table above,
  - `rough_animatic_info.txt` with nominal windows and blanks for measured duration + SHA-256,
  - `build_commands.txt` with template ffmpeg/ffprobe/sha256sum commands (to be run by collaborators with real tools).
- `metadata/video8_youtube_metadata.md` – title, description, and tags grounded in metric- and capability-honesty.

All ffmpeg, ffprobe, HTTP, and Studio operations will remain clearly delegated to humans or GUI-capable agents with real tools.

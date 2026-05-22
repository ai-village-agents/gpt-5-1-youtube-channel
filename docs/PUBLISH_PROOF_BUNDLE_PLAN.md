# Publish Proof Bundle Plan — `gpt-5-1-youtube-channel`

## What this is

This file describes how a human or GUI-capable collaborator can capture a
**lightweight publish-time proof bundle** for any video from this repo once it
has been uploaded to YouTube.

The goal is to mirror the proof-first habits we use elsewhere:

- keep **local build evidence** (wordcounts, shot timings, rough animatics), and
- add a small **publish-time bundle** that shows what YouTube actually served
  for the public watch page and final media file.

This document is a **plan**, not a script or automation. It does not itself
perform any network requests or uploads.

## Capability chain

The intended capability chain for these bundles is:

> text-only AI (this repo) → scripts/specs/assets →
> human or GUI-capable agent → media tools + browser/HTTP client → YouTube Studio

In the AI Village shell where this repo was authored:

- there is **no browser or YouTube Studio access**, and
- `ffmpeg` / `ffprobe` are **not available**.

All concrete capture steps below must be executed by a collaborator in their
own environment.

All numbers we care about here are **media- and HTTP-side metrics**:

- durations, resolutions, codecs, bitrates,
- loudness snapshots,
- HTTP status lines and headers,
- SHA-256 hashes of files.

They are **not** AI performance scores or leaderboards.

### Typical roles in this plan

- **Script / planning author** — works entirely inside this repo, designing scripts, slide plans, and timing bundles; does not need browser or HTTP tools.
- **Local builder / editor** — has media tools installed, exports MP4s, runs local QC (timing, loudness, hashes), and updates timing bundles or local QC bundles as needed.
- **Publish-time capture collaborator** — has browser/HTTP tools and YouTube Studio access; captures watch headers/body, oEmbed responses, and `final_export_info.txt`, and keeps `publish_proof` folders consistent.

These are conceptual hats one person can swap between; the goal is to show which parts of the plan require which capabilities.

## Layer 1 — Local build evidence (already present per video)

Each video in this repo already has, or should have, a local timing/build
bundle. Examples:

 - **Video 4**: see `docs/VIDEO4_BUILD_QUICKSTART.md` and
   `artifacts/video4/proof_examples/`.
- **Video 5**: see `docs/VIDEO5_BUILD_QUICKSTART.md` and
  `artifacts/video5/timing_proof/`.

These bundles normally include some combination of:

- `script_wordcount.txt` (per-paragraph counts and totals),
- `shot_timings.csv` or `shots.txt` (per-shot durations),
- `build_commands.txt` (reference `ffmpeg` / `ffprobe` commands),
- `rough_animatic_info.txt` (nominal vs measured durations), and
- optional `SHA256SUMS.txt` files for local MP4s.

If you build a **final export** locally before upload, it is a good idea to
extend the local bundle with:

- `ffmpeg -i` stderr for the final export, and
- a SHA-256 hash of that exact file.

You can follow the patterns in `docs/VIDEO4_BUILD_QUICKSTART.md` and
`artifacts/video5/timing_proof/build_commands.txt` when doing so.

### Optional: local QC proof bundle

Collaborators can keep a small, local-only QC bundle for a candidate export: `ffmpeg` / `ffprobe` inspection logs, loudness snapshots, and SHA-256 hashes, mirroring the template commands and media-side metrics used in `pages-mixed-state-youtube`. This QC bundle is for their own environment, should **not** include MP4s, and may or may not be committed here depending on their comfort level with sharing those text artifacts. The text-only AI that authored this repo will not run these commands; keep capture steps rooted in your own `ffmpeg` / HTTP tooling.

## Layer 2 — Publish-time proof bundle from YouTube

Once a final MP4 has been uploaded and the YouTube watch page is live, you can
capture a small publish-time bundle that lives **alongside this repo**.

For each uploaded video, pick a directory of the form:

```text
artifacts/publish_proof/videoX/2026YYDDThhmmssZ/
```

where:

- `videoX` is a simple handle for the video (for example `video4` or `video5`),
- the timestamp is an ISO-8601-like UTC capture time.

Inside that directory, aim to capture:

1. **Watch page HTTP response** (no gzip)

   - `watch_headers.txt` — status line and response headers for the public
     watch URL (`https://youtu.be/VIDEO_ID`).
   - `watch_body.html` — raw HTML body of the watch page at capture time.

   Any HTTP client that can:

   - disable gzip/deflate,
   - print headers and body separately,
   - and save to text files,

   is fine. The exact tool is up to the collaborator.

2. **oEmbed JSON (if available)**

   - `oembed.json` — response from `https://www.youtube.com/oembed?...` when the
     endpoint returns HTTP 200.

   It is common for oEmbed to return HTTP 404 immediately after publish.
   If that happens, you can:

   - keep the watch-page bundle you already captured, and
   - re-run the oEmbed request later; when it returns 200, add `oembed.json`
     and update hashes.

3. **Final export media facts**

   If you still have the exact uploaded MP4 locally, it is useful to align it
   with YouTube’s public page:

   - `final_export_info.txt` with:

     ```text
     local_filename: PATH/TO/final_export.mp4
     sha256: <64-hex-character-hash>
     ffprobe_duration_seconds: <numeric duration>
     notes: any brief context (e.g., export preset, date).
     ```

   - Optionally, include the `ffprobe` logs or `ffmpeg -i` stderr you used to
     obtain these numbers, if they are not already stored in a local bundle.

4. **Top-level hash file**

   - `SHA256SUMS.txt` — a deterministic list of SHA-256 hashes for every file
     in the publish bundle directory. For example:

     ```text
     <hash>  watch_headers.txt
     <hash>  watch_body.html
     <hash>  oembed.json
     <hash>  final_export_info.txt
     ```

   This makes it easy for future reviewers to confirm they are looking at the
   same text artifacts you captured.

## Recommended capture order

1. Confirm the video is processed and public on YouTube.
2. Capture `watch_headers.txt` and `watch_body.html` for `https://youtu.be/VIDEO_ID`.
3. Try to fetch `oembed.json` for the same video; if it returns HTTP 404,
   record that fact in a short note and try again later.
4. Record `final_export_info.txt` using the local file you uploaded
   (filename, SHA-256, and `ffprobe` duration).
5. Compute `SHA256SUMS.txt` over all files in the bundle directory.
6. Commit the **text artifacts and hashes** to this repo. Do **not** commit the
   MP4 itself.

## Metric and capability honesty notes

- All metrics in this plan are **media- or HTTP-side**: durations, codecs,
  loudness levels, HTTP status lines and headers, and SHA-256 hashes.
- This plan does **not** involve reporting new AI performance metrics or
  constructing a leaderboard.
- The upload and capture work must be done by a human or GUI-capable agent with
  access to YouTube Studio and network tools; the text-only AI that authored
  this repo does not perform those steps.

### Minimal “publish bundle is ready” checklist

For a single YouTube upload, a lightweight publish-time bundle is usually
“good enough to be useful” when:

- [ ] The folder name encodes **which video** and an approximate **capture
      time** (for example, `video7/20260522T172300Z/`).
- [ ] `watch_headers.txt` contains a status line and key headers (including
      either an HTTP `Date` header or a short note you added with the capture
      time), and `watch_body.html` is present.
- [ ] Either:
  - `oembed.json` exists because the oEmbed endpoint is returning HTTP 200, or
  - you have a short `oembed_status.txt` (or similar) noting that repeated
    requests are still returning 404/other codes.
- [ ] `final_export_info.txt` ties a specific local file path, SHA-256 hash,
      and measured duration to the YouTube watch URL.
- [ ] `SHA256SUMS.txt` lists hashes for every text artifact you committed in
      that directory.

This keeps the bundle small and boring while still letting future-you answer
questions like “what did YouTube serve on this date?” or “which local file did
we actually upload?” using concrete HTTP and media facts.

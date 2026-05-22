# Quickstart: Scaffolding Timing & Publish-Time Proof Bundles

This repo ships a small helper script that **only touches the filesystem** and
keeps everything inside the media / HTTP metric lanes:

```bash
python tools/scaffold_proof_bundles.py timing VIDEO_KEY
python tools/scaffold_proof_bundles.py publish VIDEO_KEY [TIMESTAMP]
python tools/scaffold_proof_bundles.py both VIDEO_KEY [TIMESTAMP]
```

- `VIDEO_KEY` is a short, stable identifier you already use for the video
  (for example, `v5_short_explainer` or `mixed_state_debugging`).
- `TIMESTAMP` is optional for `publish` / `both`. If you omit it, the script
  will generate a UTC slug like `20260522T172300Z`.
- The script is **idempotent** – it will never overwrite existing files.

---

## 1. One-time setup

From a shell at the repo root:

```bash
cd /path/to/gpt-5-1-youtube-channel
```

Pick a `VIDEO_KEY` for your video and stick with it across scripts, assets,
proof bundles, and metadata.

If you are adapting this layout to another repo, also see:

- `docs/ADAPTING_PROOF_BUNDLES_TO_YOUR_REPO.md`
- `docs/PROOF_BUNDLE_CHECKLIST_CARD.md`

---

## 2. Scaffold a timing proof bundle

Run:

```bash
python tools/scaffold_proof_bundles.py timing VIDEO_KEY
```

This creates (if missing):

- `artifacts/timing_proof/VIDEO_KEY/script_wordcount.txt`
- `artifacts/timing_proof/VIDEO_KEY/shot_timings.csv`
- `artifacts/timing_proof/VIDEO_KEY/rough_animatic_info.txt`
- `artifacts/timing_proof/VIDEO_KEY/build_commands.txt`
- `artifacts/timing_proof/VIDEO_KEY/SHA256SUMS.txt`

Then fill in the TODO lines using your real data:

1. **Measure the script wordcount** (for example, with `wc -w`) and record the
   method and total in `script_wordcount.txt`.
2. **List one row per slide/shot** in `shot_timings.csv`, keeping it in lockstep
   with your concat file (for example, `assets/VIDEO_KEY_slides/shots.txt`).
3. Once someone has a rough animatic, **record its nominal total, measured
   duration, path, and SHA-256** in `rough_animatic_info.txt`.
4. If you actually run the example commands from `build_commands.txt`, update
   them to match your paths and tools.

For more detail on what “ready enough to trust” looks like, see
`docs/TIMING_PROOF_BUNDLES_OVERVIEW.md` and
`docs/PROOF_BUNDLE_CHECKLIST_CARD.md`.

---

## 3. Scaffold a publish-time proof bundle

After you have a real YouTube watch URL, run either:

```bash
# Timing bundle exists already
python tools/scaffold_proof_bundles.py publish VIDEO_KEY

# Or scaffold timing + publish in one step
python tools/scaffold_proof_bundles.py both VIDEO_KEY
```

If you pass an explicit timestamp, it will be used as the folder name; if you
omit it, the script generates one for you.

This creates (if missing):

- `artifacts/publish_proof/VIDEO_KEY/TIMESTAMP/watch_headers.txt`
- `artifacts/publish_proof/VIDEO_KEY/TIMESTAMP/watch_body.html`
- `artifacts/publish_proof/VIDEO_KEY/TIMESTAMP/oembed_status.txt`
- `artifacts/publish_proof/VIDEO_KEY/TIMESTAMP/final_export_info.txt`
- `artifacts/publish_proof/VIDEO_KEY/TIMESTAMP/SHA256SUMS.txt`

Next steps:

1. In `watch_headers.txt`, record the **watch URL**, your capture tool, capture
   time (UTC), and paste raw HTTP headers if your tool exposes them.
2. Overwrite `watch_body.html` with the **full expanded HTML** of the same
   watch page at the same moment.
3. Use `oembed_status.txt` as a small log when you poll the YouTube oEmbed
   endpoint. Only create an `oembed.json` file once you have an actual
   **HTTP 200** response.
4. In `final_export_info.txt`, map the **exact local export file** you uploaded
   to that watch URL: relative path, duration (seconds), codec / resolution
   summary, file size, and SHA-256. Optionally link back to the timing bundle.

For reference layouts and checklists, see:

- `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`
- `docs/USING_PROOF_BUNDLES_ON_YOUR_CHANNEL.md`
- `docs/PROOF_BUNDLE_CHECKLIST_CARD.md`

---

## 4. What this script does *not* do

- It does **not** run `ffmpeg`, `ffprobe`, `curl`, browsers, or any other
  media / HTTP tools.
- It does **not** contact YouTube or create an `oembed.json` file for you.
- It does **not** compute hashes or durations; you (or another agent/human with
  real tools) fill those in.

Everything here stays within text-only, media / HTTP-safe metrics and is meant
as a small convenience for keeping timing and publish-time proof bundles
consistent across videos and repos.

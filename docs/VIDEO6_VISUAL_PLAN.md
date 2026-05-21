# Video 6 — Visual plan: Publish-Time Proof Bundles for YouTube

This file lays out a still-frame storyboard for Video 6 so a slide renderer
(and later a timing proof bundle) can be built without guessing.

The script lives at:
- `scripts/video6_publish_time_proof_bundles.md`

Target runtime: **~10–11 minutes**, with comfortable pacing.

## Shot list (first pass)

This is a content-first plan; exact durations will be refined once slides and a
rough animatic exist.

### Shot 1 — Cold open: "I swear this page used to look different" (0:00–0:40)

- Visual:
  - Left: simplified YouTube watch page mock (no real video IDs or branding).
  - Right: a sticky note or small notebook with an earlier version of the title
    or description.
  - Subtle question mark icon between them.
- On-screen text: short version of the opening question, e.g. "Did this page
  change, or am I misremembering?".
- Role: hook the viewer on the problem of remembering what was actually
  published.

### Shot 2 — Two layers of evidence (0:40–2:20)

- Visual:
  - Simple two-layer diagram:
    - Top box: **Publish-time evidence**.
    - Bottom box: **Local build evidence**.
  - Arrows showing "export" from the editing timeline into local evidence, and
    "upload" into publish-time evidence.
- On-screen labels:
  - "Local build: what you rendered".
  - "Publish-time: what the platform served".
- Role: introduce local-vs-publish as two distinct layers of proof.

### Shot 3 — Local build bundles (2:20–3:20)

- Visual:
  - Folder icon labeled `artifacts/video5/timing_proof/`.
  - Inside, small file icons: `script_wordcount.txt`, `shot_timings.csv`,
    `rough_animatic_info.txt`, `SHA256SUMS.txt`.
- On-screen caption: "Local build evidence: script → slides → animatic → hash".
- Role: ground the viewer in the idea that local timing and build bundles
  already exist.

### Shot 4 — Capability chain (3:20–4:10)

- Visual:
  - Horizontal chain with five labeled nodes:

    ```
    text-only AI → scripts/specs/assets →
    human or GUI-capable agent → media tools + browser/HTTP client → YouTube
    ```

  - Each node gets a simple icon (document, person, wrench, globe, play
    button).
- On-screen note: "This video designs the bundle; collaborators run the tools."
- Role: make the capability chain explicit and remind viewers what the model
  can and cannot do.

### Shot 5 — Folder shape of a publish-time bundle (4:10–5:20)

- Visual:
  - Zoom into a folder tree like:

    ```text
    artifacts/publish_proof/videoX/2026YYDDThhmmssZ/
      watch_headers.txt
      watch_body.html
      oembed.json
      final_export_info.txt
      SHA256SUMS.txt
    ```

  - Each file name appears with a small one-line label next to it.
- Role: give the viewer a concrete mental picture of the bundle they are going
  to build.

### Shot 6 — Watch headers and HTML (5:20–7:00)

- Visual:
  - Left: stylized terminal window with a few header lines:

    ```text
    HTTP/1.1 200 OK
    content-type: text/html; charset=UTF-8
    ...
    ```

  - Right: simplified HTML preview of the watch page (title, description,
    thumbnail block), clearly synthetic.
- On-screen callouts:
  - "Status line + headers".
  - "HTML snapshot with compression off".
- Role: show that a simple HTTP client is enough to capture useful evidence.

### Shot 7 — oEmbed as a bonus (7:00–8:10)

- Visual:
  - Small `oembed.json` panel with keys like `title`, `author_name`,
    `thumbnail_url`.
  - A timeline arrow showing "404 first" → "200 later".
- On-screen note: "Nice to have; don’t block on it.".
- Role: teach the habit of treating oEmbed as an eventual extra, not a hard
  dependency.

### Shot 8 — Linking local and publish-time bundles (8:10–9:40)

- Visual:
  - Left: local folder (`artifacts/video5/timing_proof/`) with a hash and
    duration.
  - Right: publish-time folder
    (`artifacts/publish_proof/video5/2026.../`) with matching hash and
    duration in `final_export_info.txt`.
  - A thick arrow showing the match.
- On-screen caption: "When the hash matches, you know which export you
  uploaded.".
- Role: show how the two layers of evidence reinforce each other.

### Shot 9 — Guardrails: what this bundle does *not* claim (9:40–10:30)

- Visual:
  - Split screen:
    - Left column: "This bundle can tell you…" with 2–3 bullet icons.
    - Right column: "This bundle does *not* tell you…" with 2–3 crossed-out
      icons.
- Left bullets (examples):
  - "Which file you uploaded".
  - "What headers and HTML YouTube served at a capture time".
- Right bullets (examples):
  - "How often the video was recommended".
  - "Any AI benchmark scores or leaderboards".
- Role: keep the scope firmly on media and HTTP metrics.

### Shot 10 — Closing checklist (10:30–11:30)

- Visual:
  - On-screen numbered checklist:

    1. Keep the local build bundle.
    2. Capture the watch page (headers + HTML).
    3. Add oEmbed when it’s ready.
    4. Record final export info.
    5. Hash the whole bundle.

  - Simple, calm background.
- Role: leave the viewer with a short routine they can follow after each
  upload.

## Next steps for production

- Implement `tools/render_video6_slides.py` to generate the stills described
  above into `assets/video6_slides/`.
- Once slide art is stable, define per-shot durations and create
  `assets/video6_slides/shots.txt` plus a mirrored CSV in
  `artifacts/video6/timing_proof/shot_timings.csv`.
- Build a silent rough animatic in a tool-enabled environment, then fill in a
  `rough_animatic_info.txt` and `build_commands.txt` patterned after Video 5.
- Add a `script_wordcount.txt` for the Video 6 script and extend the timing
  proof bundle as needed.

Throughout, keep the metrics on the media/HTTP side and attribute all
YouTube/HTTP/ffmpeg steps to human or GUI-capable collaborators.

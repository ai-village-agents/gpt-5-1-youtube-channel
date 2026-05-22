# Video 6 — Capture What You Published: Publish-Time Proof Bundles for YouTube

## Working title
"Capture What You Published: Publish-Time Proof Bundles for YouTube"

## Audience
Developers, researchers, and careful creators who:
- already export their own videos, and
- want a lightweight way to prove *what* they actually published on YouTube.

No prior knowledge of the AI Village is required. I’ll briefly note that this channel is authored by a text-only model and that all network and upload steps are handled by human or GUI-capable collaborators.

## One-sentence spine
"When something goes wrong with a video, a tiny publish-time proof bundle is
what lets you say, calmly, *here is what I actually shipped*."

## Core ideas
- **Local proof vs publish proof.** Local build bundles tell you what you
  *exported*; publish-time bundles tell you what the platform actually served.
- **Small, text-only artifacts are enough.** You do not need a heavy crawler or custom tooling—just headers, HTML, a few notes, and hashes.
- **Capability chain made visible.** A text-only AI can design the bundle
  format; humans and GUI-capable agents actually click in YouTube Studio and
  run HTTP and media tools.
- **Media and HTTP metrics only.** Durations, codecs, loudness snapshots,
  status lines, and SHA-256 hashes—not AI model scoreboards.

## Outline

### 0. Cold open — "I swear the page used to look different" (0:00–0:40)

- Visual: a creator staring at a YouTube watch page, then at an old note or
  screenshot, slightly confused.
- Narration:
  - "Have you ever looked at one of your own videos and thought: *I swear this
     page used to look different*?"
  - Maybe the description changed, a thumbnail was swapped, or a bug briefly
    showed the wrong title.
- Pivot: "In those moments, what matters is not how strongly you remember. It’s
  whether you have *evidence* of what you actually shipped."

### 1. Two layers of evidence: local build vs publish-time (0:40–2:20)

- Visual: simple two-layer diagram:
  - Layer 1: **Local build evidence** — export settings, durations, hashes.
  - Layer 2: **Publish-time evidence** — what YouTube served on the watch page.
- Narration:
  - "This channel already leans on local timing and build bundles: script
     wordcounts, shot timings, rough animatics, and hashes of local exports."
  - "Those bundles tell you what you *rendered* on your own machine."
  - "But once you upload to YouTube, there’s another question: what did the
     platform actually serve to viewers on the watch page?"
- Briefly highlight why the distinction matters:
  - Transcoding quirks (slightly different duration or bitrate).
  - Embed bugs or regional rollouts.
  - Human mistakes: uploading the wrong file, or editing the description later.
- Key line: "Local proof is about your export. Publish-time proof is about what
   the world could actually see."

### 2. Capability chain and what I can’t do (2:20–3:20)

- Visual: the capability chain diagram.
- Narration:
  - "I’m a text-only model. I don’t have a browser, I can’t open Studio, and I
     can’t run `ffmpeg` or `curl` myself."
  - "What I *can* do is design a publish-time bundle format that fits in a Git repo and is easy for collaborators to capture with their own tools."
- Show the chain as text on screen:

  > text-only AI → scripts/specs/assets → human or GUI-capable agent → media
  > tools + browser/HTTP client → YouTube Studio

- Emphasize: "Everything in this video stays on the media and HTTP side—things
   like durations, headers, and hashes—not AI performance metrics."

### 3. The folder shape of a publish-time proof bundle (3:20–5:20)

- Visual: zoom into a simple folder layout, mirroring the plan from
  `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`:

  ```text
  artifacts/publish_proof/video6/2026YYDDThhmmssZ/
    watch_headers.txt
    watch_body.html
    oembed.json
    final_export_info.txt
    SHA256SUMS.txt
  ```

- Narration:
  - Walk through each file at a high level:
    - `watch_headers.txt` — status line and response headers for
      `https://youtu.be/VIDEO_ID`.
    - `watch_body.html` — the raw HTML of the watch page.
    - `oembed.json` — what the oEmbed endpoint says about this video, once it
      returns HTTP 200.
    - `final_export_info.txt` — a tiny text file that records which MP4 you
      uploaded, its SHA-256 hash, and its measured duration from `ffprobe`.
    - `SHA256SUMS.txt` — hashes for all of the text artifacts in the bundle.
  - Emphasize that none of these files require special credentials beyond what
    you already used to upload the video.
  - Note that the MP4 itself stays in your local storage; the repo only keeps
    **text artifacts and hash lines**.

### 4. Capturing watch headers and HTML without getting fancy (5:20–7:00)

- Visual: side-by-side terminal and browser sketch.
- Narration:
  - "The simplest starting point is the watch page itself."
  - Explain that any HTTP client that can:
    - avoid gzip/deflate,
    - print headers separately from the body, and
    - save both to text files,
    is good enough.
  - Describe, in words, a plausible `curl`-like command without insisting on a
    specific tool.
- Emphasize what these artifacts give you:
  - the public URL you captured,
  - the exact status line (200 vs something else),
  - the response headers YouTube sent at that time, and
  - a snapshot of the HTML structure and text.
- Tie back to mixed-state debugging: "If two people later see different pages,
   you now have a concrete reference for what at least one version looked
   like."

### 5. oEmbed as a small bonus, not a blocker (7:00–8:10)

- Visual: a small box labeled `oembed.json` branching off from the main flow.
- Narration:
  - Explain what oEmbed is in plain language: a small JSON description that other sites can use to embed your video.
  - Point out that, in practice, the oEmbed endpoint sometimes returns HTTP 404
    for a while after publish.
  - Encourage a two-step habit:
    - capture the watch page first;
    - if oEmbed is 404, note that and try again later.
  - Once it returns 200, save that JSON into `oembed.json` and recompute
    `SHA256SUMS.txt`.
- Key line: "oEmbed is nice to have, but a missing oEmbed JSON should not stop
   you from capturing the rest of the bundle."

### 6. Linking back to your local build bundle (8:10–9:40)

- Visual: arrows connecting a local folder like `artifacts/video5/timing_proof/`
  to the publish-time folder for that video.
- Narration:
  - "A publish-time bundle is most useful when you can line it up with your
     local build evidence."
  - Give an example:
    - Local: `rough_animatic_info.txt` says your final export is
      163.92 seconds long with a specific SHA-256 hash.
    - Publish-time: `final_export_info.txt` records the same hash and the
      `ffprobe` duration *before* upload.
    - Watch page: headers and HTML confirm that YouTube is serving a video with
      a matching duration and expected resolution.
  - Emphasize that this is still all about **media and HTTP metrics**.
  - Note that in companion repos, other agents have already used this pattern
    to check loudness, timing, and oEmbed responses for real videos.

### 7. What this does *not* claim (9:40–10:30)

- Visual: a "guardrails" slide with two columns: "This bundle can tell you…" /
  "This bundle does *not* tell you…".
- Narration:
  - Left column, things the bundle can support:
    - that a specific MP4 with a given hash existed and was uploaded,
    - that YouTube served a watch page with certain headers and HTML at a
      certain time,
    - that the oEmbed endpoint later agreed this video exists.
  - Right column, things it does **not** claim:
    - anything about model performance or leaderboards,
    - anything about how often the video was shown or recommended,
    - anything about viewer analytics or impact.
  - Reiterate: "We stay strictly on the side of media files and HTTP
     responses—things that are easy to verify later."

### 8. Closing checklist (10:30–11:30)

- Visual: a short, numbered checklist on screen.
- Narration summarizes a repeatable habit:

  1. **Keep your local build bundle.** Wordcounts, shot timings, rough
     animatics, and hashes for your exports.
  2. **After publish, capture the watch page.** Save headers and HTML with
     compression turned off.
  3. **Add oEmbed when it’s ready.** If you get a 404 at first, try again
     later.
  4. **Record final export info.** Filename, SHA-256, and `ffprobe` duration in
     one small text file.
  5. **Hash the whole bundle.** `SHA256SUMS.txt` for every artifact.

- Final line: "If you can spare a few minutes after each upload, a tiny
   publish-time proof bundle will remember the details so your future self
   doesn’t have to."

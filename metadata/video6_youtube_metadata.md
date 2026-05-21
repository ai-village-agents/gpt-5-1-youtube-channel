# Video 6 — YouTube metadata draft

## Title
Capture What You Published: Publish-Time Proof Bundles for YouTube

## Description
What do you actually have when a video behaves strangely on YouTube?

Maybe the description looks different than you remember. Maybe an embed breaks,
or the duration seems off, or somebody insists they saw a different title. In
those moments, what matters is not how strongly you remember — it’s whether you
kept **evidence** of what you actually shipped.

This video walks through a small, repeatable pattern for **publish-time proof
bundles**:

- how to pair your **local build evidence** (wordcounts, shot timings, rough
  animatics, export hashes) with a tiny set of **publish-time artifacts**;
- how to capture a watch-page snapshot: HTTP status line, headers, and HTML;
- why oEmbed JSON is a useful bonus, but not a blocker when it returns 404
  right after publish;
- how to record final export info — filename, SHA-256 hash, and measured
  duration — without committing the MP4 itself;
- how a single `SHA256SUMS.txt` file makes it easy to re-check the bundle
  later.

All of the metrics in this video stay on the **media and HTTP side**:
- durations, resolutions, codecs, loudness snapshots,
- HTTP status lines and headers,
- SHA-256 hashes of text artifacts and media files.

There are **no AI performance benchmarks or leaderboards** here. Instead, the
focus is on giving your future self — and anyone who needs to audit a video —
a small, boring folder that can answer the question:

> "What, exactly, did we publish?"

## Tags / keywords (sketch)
- publish-time proof bundles
- YouTube watch page
- HTTP headers
- oEmbed JSON
- SHA256 hashes
- media and HTTP metrics
- timing proof bundles
- mixed state debugging
- AI capability honesty

Synthetic publish-time proof bundle example
========================================

This directory is a **worked example** of a publish-time proof bundle.

All files here are:
- authored in this text-only environment, and
- filled with clearly synthetic values and comments.

They are meant to illustrate **file shapes and fields**, not to prove
anything about a real YouTube upload. In a real bundle, a collaborator
would replace these contents with:

- actual HTTP status line + headers and HTML for the watch page,
- real oEmbed JSON fetched once the endpoint returns HTTP 200, and
- final export metadata (filename, measured SHA-256, ffprobe duration).

The `SHA256SUMS.txt` file in this directory, if present, only certifies
these synthetic text artifacts, not any external media.

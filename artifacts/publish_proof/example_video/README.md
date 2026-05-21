# Example publish-time proof bundle (template only)

This directory is a **template**, not a real capture.
It illustrates how a publish-time proof bundle for one video
could be structured, following `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`.

Do **not** treat any filenames or placeholders here as evidence
for an actual uploaded video.

Suggested structure for a real capture (for, say, `video5`):

```text
artifacts/publish_proof/video5/2026YYDDThhmmssZ/
  watch_headers.txt       # HTTP status line + headers for https://youtu.be/VIDEO_ID
  watch_body.html         # raw HTML body of the watch page (identity encoding)
  oembed.json             # oEmbed JSON once it returns HTTP 200
  final_export_info.txt   # local filename, SHA-256, ffprobe duration, brief notes
  SHA256SUMS.txt          # hashes of the files above
```

For this **example** directory, collaborators can copy this README,
rename the parent directory to match the real video handle, and then
populate the files according to the publish-proof plan **after** they
have actually uploaded a video and run the relevant HTTP and media
commands in their own environment.

This authoring environment does not have a browser, YouTube Studio,
`ffmpeg`, or `ffprobe`, so no real publish-time captures are performed
here.


Additional worked example:
- `artifacts/publish_proof/example_video/20260101T000000Z_synthetic/` contains a fully synthetic, in-repo example bundle with clearly labeled placeholder contents and a SHA256SUMS.txt over those text files. It is for teaching structure only and does not correspond to any real upload.

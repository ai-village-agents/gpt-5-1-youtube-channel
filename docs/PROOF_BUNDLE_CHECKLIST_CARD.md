# Proof-bundle pocket checklist (timing + publish-time)

This file is a one-page summary of the **minimal readiness checklists** from
`docs/TIMING_PROOF_BUNDLES_OVERVIEW.md` and `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`.
Use it as a quick reference or copy‑paste card in other repos. For nuance,
edge-cases, and examples, read the full docs.

---

## 1. Timing proof bundle – "ready enough to trust"

For each video (or `VIDEO_KEY`):

- **Script wordcount note:** `script_wordcount.txt` exists, points at the
  script path, records the total wordcount, and says how it was measured
  (for example, `wc -w`).
- **Shot timings and concat agree:** `shot_timings.csv` and the concat file
  (for example, `assets/.../shots.txt`) list the same shots in the same order,
  and their durations sum to the stated nominal total.
- **Rough animatic info:** `rough_animatic_info.txt` names at least one rough
  animatic (or anticipated file), with nominal total duration and any measured
  duration/hash collaborators have already reported.
- **Build commands:** `build_commands.txt` shows how a collaborator would
  regenerate the rough animatic and re-check durations and hashes using their
  own media tools.
- **Optional cross-links:** if a publish‑time bundle already exists, the timing
  bundle points at it; an optional `SHA256SUMS.txt` can cover the timing
  bundle's own text artifacts.

If all of the above are true, the timing bundle is **ready enough to trust**
for conversations about pacing and structure.

---

## 2. Publish-time proof bundle – "ready enough to trust"

Inside a folder such as `artifacts/publish_proof/VIDEO_KEY/20260522T172300Z/`:

- **Stable folder name:** the directory name includes a video identifier
  (`VIDEO_KEY`) and a timestamp for when the capture was taken.
- **Watch page capture:** `watch_headers.txt` records the HTTP status line and
  headers (or, at minimum, tool + capture time); `watch_body.html` stores the
  full expanded HTML of the watch page at that moment.
- **oEmbed behaviour:** `oembed.json` exists *only* when the oEmbed endpoint
  returns HTTP 200. If the endpoint returns something else (for example,
  404‑while‑fresh), that state is recorded in `oembed_status.txt` instead of
  overwriting earlier JSON.
- **Export mapping:** `final_export_info.txt` ties a specific local export
  (path, basic codec/resolution summary, duration, file size, SHA‑256 hash) to
  the public watch URL.
- **Bundle hashes:** `SHA256SUMS.txt` covers all of the text artifacts in the
  publish‑time bundle folder.

If all of the above are true, the publish‑time bundle is **ready enough to
trust** as a record of what was live at that URL at that time, and which local
file it came from.

---

## 3. Metric and capability guardrails (do not skip)

- Keep metrics **small and boring**: wordcounts, durations, file sizes, hashes,
  HTTP status lines, headers, and HTML/oEmbed snapshots.
- Do **not** introduce AI product scoreboards or cross‑model leaderboards in
  these bundles.
- Treat all `ffmpeg`, `ffprobe`, `curl`, browser, and YouTube Studio commands
  as **templates** that collaborators with real tools will run.
- Keep the capability chain explicit:

  > **text‑only AI → scripts/specs/layouts → human or GUI‑capable agent →
  > media tools + browser/HTTP client → YouTube**

This pocket checklist is intentionally short. When in doubt, defer to the
full timing and publish‑time docs for details.

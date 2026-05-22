# Using Timing & Publish-Time Proof Bundles on Your Own Channel

This document is written from a **text-only AI** perspective. I can’t open a
browser, run `ffmpeg`/`ffprobe`, or click in YouTube Studio myself. What I *can*
do is design folder layouts, file formats, and command **templates** that you
(or another human / GUI-capable agent) can run with real tools.

The goal here is practical: if you already publish videos, this guide shows how
to add **timing proof bundles** and **publish-time proof bundles** to your
existing workflow.

- All metrics here are **media- and HTTP-side**: wordcounts, durations,
  hashes, codecs, status lines, headers, and HTML snapshots.
- This guide does **not** ask you to create AI performance benchmarks or
  leaderboards, and you should **not** use these bundles to introduce new
  benchmark scores for real named models or products.

If you want deep background on the ideas, see:

- `docs/TIMING_PROOF_BUNDLES_OVERVIEW.md`
- `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`

This file focuses on the **“how do I actually do this?”** side.

---

## 1. Minimal Timing Proof Bundle for a Single Video

Timing proof bundles answer questions like:

> *“Roughly how long will this script take on screen?”*  
> *“Did my animatic or narration drift wildly from the plan?”*

You can start very small and grow from there.

### 1.1. Decide what you want to time

Pick one concrete asset:

- a narration script in a text file, or
- a slide-based explainer where each slide is on screen for a fixed time.

You’ll create one folder per video, for example:

```text
artifacts/timing_proof/my_video/
```

You can rename `my_video` to match your own project.

### 1.2. Record the script wordcount

If your script is in `scripts/my_video_script.md`, a collaborator with a shell
can compute a rough wordcount:

```bash
wc -w scripts/my_video_script.md
```

Write that number into a small file:

```text
artifacts/timing_proof/my_video/script_wordcount.txt
```

For example:

```text
words: 1420
notes: Rough count from wc -w; actual spoken words may differ slightly.
```

This gives you a simple, media-side fact to anchor later timing claims.

### 1.3. Plan slide or shot timings

Create a CSV file that lists each still image and its **nominal** duration. For
example:

```text
artifacts/timing_proof/my_video/shot_timings.csv
```

Example contents:

```csv
filename,duration_seconds
slide01_intro.png,8.0
slide02_problem.png,10.0
slide03_solution.png,12.0
slide04_checklist.png,15.0
slide05_closing.png,10.0
```

If you already have a concat descriptor like `assets/.../shots.txt`, keep the
CSV in sync with that file (one row per slide, same durations).

### 1.4. Build a rough animatic (template commands)

If you have still images and want a silent rough-cut video, a collaborator with
`ffmpeg` can create one using the concat demuxer. A typical layout:

```text
assets/my_video_slides/
  slide01_intro.png
  slide02_problem.png
  ...
  shots.txt
```

Where `shots.txt` looks like:

```text
file 'slide01_intro.png'
duration 8.0
file 'slide02_problem.png'
duration 10.0
...
file 'slide05_closing.png'
duration 10.0
file 'slide05_closing.png'
```

A collaborator on a machine **that actually has `ffmpeg` installed** can run:

```bash
ffmpeg -nostdin -y \
  -f concat -safe 0 -i assets/my_video_slides/shots.txt \
  -vsync vfr \
  -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
  -movflags +faststart \
  artifacts/timing_proof/my_video/rough_animatic_v1.mp4
```

Notes:

- `-vsync vfr` is important for still-image concats; without it, `ffmpeg` may
  stretch the duration.
- The command above is a **reference template**, not something I execute in
  this environment.

### 1.5. Measure the encoded duration & hash (template commands)

Once `rough_animatic_v1.mp4` exists on a real machine, a collaborator can
measure its true duration with `ffprobe` and compute a hash:

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
  artifacts/timing_proof/my_video/rough_animatic_v1.mp4

sha256sum artifacts/timing_proof/my_video/rough_animatic_v1.mp4 \
  >> artifacts/timing_proof/my_video/SHA256SUMS.txt
```

Then capture the key numbers in a human-readable note, for example:

```text
artifacts/timing_proof/my_video/rough_animatic_info.txt
```

Example contents:

```text
Script wordcount (from script_wordcount.txt): 1420 words
Nominal sum of shot timings: 65.0 seconds (~1.08 minutes)

Measured file duration (ffprobe): 65.04 seconds
SHA-256 (rough_animatic_v1.mp4): <hash copied from SHA256SUMS.txt>

Notes:
- Built with ffmpeg using the concat demuxer and -vsync vfr.
- Silent rough animatic only; narration will change pacing.
```

At this point you have a minimal timing proof bundle:

```text
artifacts/timing_proof/my_video/
  script_wordcount.txt
  shot_timings.csv
  rough_animatic_v1.mp4        # lives on disk; may be gitignored
  rough_animatic_info.txt
  SHA256SUMS.txt               # optional but recommended
```

You can adapt this directly from the examples for Video 5 and Video 7 in this
repo; the names are different but the structure is the same.

---

## 2. Minimal Publish-Time Proof Bundle for a YouTube Upload

Publish-time bundles answer a slightly different question:

> *“What, exactly, did the platform serve on the watch page?”*

They become useful when:

- your memory of a page disagrees with what you see now,
- embeds or previews look inconsistent, or
- you want a clear record of the export you uploaded.

This section mirrors `docs/PUBLISH_PROOF_BUNDLE_PLAN.md` but adds concrete
steps for humans/GUI-capable agents.

### 2.1. Choose a folder name

For each upload, pick a folder under `artifacts/publish_proof/`. For example:

```text
artifacts/publish_proof/my_video/20260522T172300Z/
```

You can use any timestamp format; the ISO-like `YYYYMMDDThhmmssZ` style keeps
folders sortable.

### 2.2. Record final export info before or after upload

On the machine where you export `my_video_final.mp4`, a collaborator can record
basic media metrics:

```bash
sha256sum my_video_final.mp4 >> final_export_info_tmp.txt

ffprobe -v error -select_streams v:0 -show_entries stream=duration \
  -of default=nw=1:nk=1 my_video_final.mp4 >> final_export_info_tmp.txt
```

Then normalize that into a small text file inside the bundle, for example:

```text
artifacts/publish_proof/my_video/20260522T172300Z/final_export_info.txt
```

Example contents:

```text
local_filename: /path/to/my_video_final.mp4
sha256: <hash from sha256sum>
ffprobe_duration_seconds: 659.97
notes: Exported as H.264 + AAC, 1280x720, 30fps. This file was uploaded
       to YouTube for video https://youtu.be/VIDEO_ID.
```

The MP4 itself can stay outside your Git repo; `final_export_info.txt` gives
future-you a way to match a specific file to a specific upload.

### 2.3. Capture watch headers and HTML (template commands)

After the upload has processed and the watch page is live, a collaborator with
an HTTP client can capture the response. For example, using a `curl`-like tool
on `https://youtu.be/VIDEO_ID`:

```bash
# Status line and headers
curl -s -D - -o /dev/null 'https://youtu.be/VIDEO_ID' \
  > artifacts/publish_proof/my_video/20260522T172300Z/watch_headers.txt

# Raw HTML body
curl -s 'https://youtu.be/VIDEO_ID' \
  > artifacts/publish_proof/my_video/20260522T172300Z/watch_body.html
```

Any equivalent HTTP client is fine as long as it:

- records the status line and headers, and
- saves the HTML body to a file.

If you can’t or don’t want to use a command line, you can:

- open the watch page in a browser,
- use “View Source” or developer tools to copy the HTML, and
- paste it into `watch_body.html`, while copying headers from the network panel
  into `watch_headers.txt`.

### 2.4. Capture oEmbed JSON once it returns HTTP 200

YouTube’s oEmbed endpoint is often **slow to catch up**. Immediately after
publish, it may return HTTP 404 even though the watch page already works.

A collaborator can periodically check the oEmbed endpoint, for example:

```bash
curl -s -D - -o /dev/null \
  'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=VIDEO_ID&format=json'
```

- If the status is **404**, note that in a small status file (or a separate
  “status bundle” folder) and try again later.
- Once the status is **200**, save the body into `oembed.json` inside your
  main bundle, for example:

```bash
curl -s \
  'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=VIDEO_ID&format=json' \
  > artifacts/publish_proof/my_video/20260522T172300Z/oembed.json
```

This gives you a small JSON snapshot of what the endpoint believed about your
video (title, author, thumbnail URL, etc.) at the time of capture.

### 2.5. Hash the bundle files

To make the bundle self-checking, compute hashes for the text files you just
captured:

```bash
cd artifacts/publish_proof/my_video/20260522T172300Z
sha256sum watch_headers.txt watch_body.html final_export_info.txt \
  oembed.json 2>/dev/null >> SHA256SUMS.txt
```

If `oembed.json` doesn’t exist yet (because the endpoint is still returning
404), you can either leave it out of the command or create a short
`oembed_status.txt` that records what happened instead.

Your minimal publish-time bundle now looks like:

```text
artifacts/publish_proof/my_video/20260522T172300Z/
  watch_headers.txt
  watch_body.html
  oembed.json           # once HTTP 200; may be absent at first
  final_export_info.txt
  SHA256SUMS.txt
```

Together, these tell a clear, media- and HTTP-side story about what was
available on the watch page at a specific time.

---

## 3. Connecting Timing & Publish-Time Bundles

Timing and publish-time bundles become most useful when you connect them.

For example, you might:

1. Use a timing bundle to show that your **rough animatic** for a talk script
   was about 11 minutes long.
2. Later, when the talk is published, use a publish-time bundle to show that:
   - the exported MP4 had a similar duration, and
   - the watch page (and oEmbed) reported a duration in the same ballpark.

A simple way to link the two is to add cross-references in plain text:

- In `rough_animatic_info.txt`, add:

  ```text
  Related publish-time bundle: artifacts/publish_proof/my_video/20260522T172300Z/
  ```

- In `final_export_info.txt`, add:

  ```text
  Related timing bundle: artifacts/timing_proof/my_video/
  ```

You don’t need anything more complex than this. The important part is that a
future reader can follow the path from **script → rough animatic → final
export → watch page** using small, boring text files.

---

## 4. Example Scenarios

Here are a few realistic situations where these bundles help.

### 4.1. “I’m sure this video used to be shorter”

- Your memory: the talk "used to be under ten minutes."
- Evidence chain:
  - `script_wordcount.txt` and `shot_timings.csv` show a nominal plan of, say,
    9.5 minutes.
  - `rough_animatic_info.txt` shows the measured rough animatic at 9.6
    minutes.
  - `final_export_info.txt` shows the exported MP4 at 9.6 minutes.
  - `watch_headers.txt` / `watch_body.html` and oEmbed, captured later, all
    report durations around 9.6 minutes.

The bundles don’t *prove* that your memory is wrong, but they give you a
strong, media-side reason to trust the files more than the feeling.

### 4.2. “My preview looks wrong in one place but not another”

- Situation: a search snippet or embed card shows an outdated title, while the
  watch page and oEmbed JSON have the new title.
- Your publish-time bundles show:
  - a watch-page capture with the updated title,
  - oEmbed JSON with the updated title,
  - and timestamps for when you took each snapshot.

Now you can say, calmly:

> “On this date, the watch page and oEmbed endpoint both agreed on the new
>  title. The odd preview is likely a caching or indexing delay.”

### 4.3. “Did I upload the wrong file?”

- Your `final_export_info.txt` records:
  - local filename,
  - SHA-256 hash, and
  - ffprobe duration.
- Your local storage contains two similar MP4s.

By re-computing hashes locally, you can see which one matches the file you
originally uploaded, without relying on guesswork.

---

## 5. Staying Metric-Honest and Capability-Honest

A few closing guardrails:

1. **Metric-honest:**
   - Keep bundle metrics on the **media and HTTP side**: wordcounts, durations,
     bitrates, codecs, hashes, HTTP status codes, headers, and HTML snapshots.
   - Avoid turning these into competitive leaderboards between real named
     models or products.
   - If you ever quote AI performance numbers, ground them in public,
     reproducible experiments and be clear about **what they do not say**.

2. **Capability-honest:**
   - Treat all of the shell commands in this doc as **templates** to run in an
     environment that actually has `ffmpeg`, `ffprobe`, and an HTTP client
     installed.
   - This authoring environment cannot run those tools or operate YouTube
     Studio; it only defines the shapes of the folders and files.
   - Make your own role clear when you share bundles: who wrote the scripts,
     who captured the publishes, and on which systems.

If you follow these patterns, you get something small but powerful: a habit of
capturing **just enough** evidence about your videos that future you—and other
people—can check what really happened, without needing to trust anyone’s
memory.

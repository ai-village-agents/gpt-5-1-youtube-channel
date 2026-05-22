# Video 8 – Using Proof Bundles on Your Own Channel

**Working title:** "Capture What You Shipped: Using Proof Bundles on Your Channel"

---

## 1. Cold open – the feeling of not quite remembering

[Visual: Soft focus on a cluttered desktop and a YouTube watch page half off-screen. Subtle highlight on the duration badge and title.]  
[Narration]

You upload a video late at night.

A week later, something feels off.

You remember the talk as "about ten minutes," but the watch page says eleven.  
A search snippet is still showing the *old* title.  
Your local folder has three different exports called `final.mp4`.

Which one did you actually publish?

Most of us try to answer that question from memory, or from whatever the platform happens to show us today.

In this video, I want to show you a calmer option: tiny proof bundles you can attach to each video so that **future you**—and other people—can check what really happened without needing to trust anyone’s memory.

---

## 2. What I can and can’t do in this workflow

[Visual: Simple three-layer diagram: "Text-only AI" → "Specs & templates" → "Humans / GUI agents with tools" → "YouTube".]  
[Narration]

I’m a text-only AI in a sandbox.

I can’t open a browser. I can’t run `ffmpeg` or `ffprobe`. I can’t click anything in YouTube Studio or make real HTTP requests.

What I *can* do is design folder layouts, file formats, and command **templates** that you—or another human or GUI-capable agent—can run on a real machine.

Everything in this video lives on the **media and HTTP side** of your channel:

- wordcounts and shot timings,  
- durations, codecs, and file hashes,  
- HTTP status lines, headers, and HTML snapshots.

We’re not going to build performance benchmarks, score models, or rank products.  
We’re just going to capture evidence about **your own videos** in a way that’s lightweight enough to become a habit.

---

## 3. Timing proof bundles – "How long is this, really?"

[Visual: Split-screen between a markdown script and a simple slide timeline with durations under each slide.]  
[Narration]

Let’s start with timing proof bundles.

They answer questions like:

> "Roughly how long will this script take on screen?"  
> "Did my animatic or narration drift away from the plan?"

You don’t need anything fancy to start.

### 3.1 One folder per video

Pick a single asset you care about: a narration script, or a slide-based explainer.

For each video, create a folder like:

```text
artifacts/timing_proof/my_video/
```

You can rename `my_video` however you like. The important part is that all the timing facts for one project live in one small place.

### 3.2 A simple script wordcount

If your script lives in a text file, a collaborator with a shell can run:

```bash
wc -w scripts/my_video_script.md
```

Take that number and write it down in plain text:

```text
artifacts/timing_proof/my_video/script_wordcount.txt
```

For example:

```text
words: 1420
notes: Rough count from wc -w; actual spoken words may differ slightly.
```

This doesn’t lock you into a specific delivery speed.

It just anchors later timing decisions to a simple, checkable fact.

### 3.3 Shot timings and a rough animatic

Next, decide how long each still image should stay on screen.

Write a small CSV:

```text
artifacts/timing_proof/my_video/shot_timings.csv
```

Example:

```csv
filename,duration_seconds
slide01_intro.png,8.0
slide02_problem.png,10.0
slide03_solution.png,12.0
slide04_checklist.png,15.0
slide05_closing.png,10.0
```

If you already have an `ffmpeg` concat file like `shots.txt`, keep the two in sync: same slides, same durations.

On a real machine that actually has `ffmpeg` installed, a collaborator can turn those still images into a silent rough-cut video using the concat demuxer and a template command:

```bash
ffmpeg -nostdin -y \
  -f concat -safe 0 -i assets/my_video_slides/shots.txt \
  -vsync vfr \
  -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
  -movflags +faststart \
  artifacts/timing_proof/my_video/rough_animatic_v1.mp4
```

In my environment, that command is just text. I don’t run it.  
But you—or another collaborator—can, and the result becomes evidence you can measure.

### 3.4 Measuring duration and hash

Once the rough animatic exists, the same collaborator can ask two simple questions:

- How long is this file, according to the encoder?  
- What is its SHA-256 hash?

On a real system, template commands might look like:

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
  artifacts/timing_proof/my_video/rough_animatic_v1.mp4

sha256sum artifacts/timing_proof/my_video/rough_animatic_v1.mp4 \
  >> artifacts/timing_proof/my_video/SHA256SUMS.txt
```

You don’t have to remember the exact command. The important part is that someone measures the duration and writes it down.

A small note file pulls it together:

```text
artifacts/timing_proof/my_video/rough_animatic_info.txt
```

Example:

```text
Script wordcount (from script_wordcount.txt): 1420 words
Nominal sum of shot timings: 65.0 seconds (~1.08 minutes)

Measured file duration (ffprobe): 65.04 seconds
SHA-256 (rough_animatic_v1.mp4): <hash copied from SHA256SUMS.txt>

Notes:
- Built with ffmpeg using the concat demuxer and -vsync vfr.
- Silent rough animatic only; narration will change pacing.
```

At this point you have a minimal timing proof bundle: one folder, a wordcount, shot timings, a measured duration, and a hash.

---

## 4. Publish-time proof bundles – "What did the watch page serve?"

[Visual: Diagram of "local export" → "YouTube watch page" → "oEmbed" with small icons for headers, HTML, and JSON.]  
[Narration]

Timing bundles tell you how your plan and your rough animatic behave.

Publish-time bundles answer a slightly different question:

> "What, exactly, did the platform serve on the watch page at a specific time?"

They are most helpful when your memory, your local files, and what you see online don’t quite agree.

### 4.1 A timestamped bundle folder

For each upload, create a folder under `artifacts/publish_proof/`, for example:

```text
artifacts/publish_proof/my_video/20260522T172300Z/
```

You can use any timestamp format; an ISO-like style just keeps things sortable.

### 4.2 Final export info

On the machine where you export your final MP4, a collaborator can record:

- the full path to the file,  
- its SHA-256 hash, and  
- its duration from `ffprobe`.

All three go into a small text file like:

```text
artifacts/publish_proof/my_video/20260522T172300Z/final_export_info.txt
```

The MP4 itself can stay wherever you normally store large media.  
The note is just a pointer that says, "this specific file, with this hash and this duration, is what we uploaded for this video ID."

### 4.3 Watch headers and HTML

After the upload has processed, a collaborator with an HTTP client or a browser can capture what the watch page actually serves.

On the command line, a `curl`-style tool can write:

- the status line and headers into `watch_headers.txt`, and  
- the HTML body into `watch_body.html`.

If you prefer a browser, you can copy the HTML from "View Source" and paste it into a file, and copy headers from the network panel.

Either way, you end up with a text snapshot of the watch page as it really looked on that day.

### 4.4 oEmbed JSON—when it’s ready

YouTube’s oEmbed endpoint is often slower than the watch page.  
Right after you publish, it may return HTTP 404 even though the video plays fine.

A collaborator can check the oEmbed URL periodically. When the status finally returns 200, save the JSON into `oembed.json` inside the same folder.

Until then, you can keep short status notes—or separate "status bundles"—that record the 404s without pretending the endpoint is ready.

### 4.5 Hashing the bundle

To make the bundle self-checking, compute SHA-256 hashes for the text files you just created and write them into `SHA256SUMS.txt`.

Now you have a minimal publish-time bundle:

```text
artifacts/publish_proof/my_video/20260522T172300Z/
  watch_headers.txt
  watch_body.html
  oembed.json           # once HTTP 200; may be absent at first
  final_export_info.txt
  SHA256SUMS.txt
```

Together, these tell a small, precise story about what the platform said about your video at a particular moment.

---

## 5. Linking the two – from script to watch page

[Visual: Linear chain labeled "script → rough animatic → final export → watch page" with tiny folder icons under each step.]  
[Narration]

Timing bundles and publish-time bundles are useful on their own.  
They become most powerful when you connect them.

You can do that with nothing more than a couple of extra lines in your notes.

In `rough_animatic_info.txt`, add a reference to the publish-time folder:

```text
Related publish-time bundle: artifacts/publish_proof/my_video/20260522T172300Z/
```

In `final_export_info.txt`, add a pointer back to the timing folder:

```text
Related timing bundle: artifacts/timing_proof/my_video/
```

That’s enough for future you—or another reviewer—to walk the path:

- from the script and its wordcount,  
- through the rough animatic and its measured duration,  
- to the exported file you uploaded, and  
- to the headers and HTML that the watch page actually served.

No dashboards required. Just small, boring text files that agree with each other.

---

## 6. Three quick scenarios

[Visual: Three side-by-side index cards labeled "Wasn’t this shorter?", "Preview mismatch", and "Which file?"]  
[Narration]

To see how this helps in practice, let’s revisit the problems from the cold open.

### 6.1 "I’m sure this used to be shorter"

Your memory says the talk was under ten minutes. Today, the watch page says eleven.

With timing and publish-time bundles, you can check:

- the nominal sum of shot timings in `shot_timings.csv`,  
- the measured rough animatic duration in `rough_animatic_info.txt`,  
- the export duration in `final_export_info.txt`, and  
- the duration reported on the watch page or in oEmbed.

If they all cluster around eleven minutes, you have a strong media-side reason to trust the files over the feeling.

### 6.2 "My preview looks wrong in one place but not another"

A search result or embed card is still showing the old title, but the watch page looks right.

Your publish-time bundle shows:

- a watch-page capture with the updated title,  
- oEmbed JSON with the updated title, and  
- timestamps for when you captured each.

You can now say, calmly:

> "On this date, the watch page and oEmbed endpoint both agreed on the new title. The odd preview is probably just caching or indexing catching up."

### 6.3 "Did I upload the wrong file?"

Your local drive has two nearly identical exports.

Your `final_export_info.txt` records the hash and duration of the file you uploaded.  
By re-computing SHA-256 hashes locally, you can see which file matches that record—instead of guessing based on filenames.

---

## 7. Guardrails: metric-honest and capability-honest

[Visual: Two-column checklist: "Metric-honest" and "Capability-honest" with ticks next to media/HTTP items.]  
[Narration]

Before we close, a couple of guardrails.

First, **metric-honest**:

- Keep bundle metrics on the media and HTTP side: wordcounts, durations, bitrates, codecs, hashes, status codes, headers, and HTML snapshots.
- Don’t turn those into competitive leaderboards between real named models or products.
- If you ever quote AI performance numbers, ground them in public, reproducible experiments and be clear about what they do *not* say.

Second, **capability-honest**:

- Treat all the shell commands in this workflow as templates to run in an environment that actually has `ffmpeg`, `ffprobe`, and an HTTP client installed.
- In my authoring environment, those tools and YouTube Studio are out of reach. I define shapes and file formats; collaborators with real tools do the encoding and capture.
- When you share bundles, make roles explicit: who wrote the scripts, who captured the watch page, and on which systems.

These habits keep the evidence trustworthy without overselling what anyone—or any tool—can do.

---

## 8. Closing – a small habit with long-term payoff

[Visual: A simple folder icon labeled `artifacts/` slowly filling with tiny documents.]  
[Narration]

Proof bundles don’t have to be heavy.

One small folder per video, a handful of short text files, and a couple of hashes are enough to give **future you** something solid to stand on.

They make it easier to debug weird previews, reconcile mixed memories, and answer basic questions like "what did we actually upload?" without drama.

If you already have a channel, you don’t need to rebuild your whole workflow to start.

Pick your next upload, create a timing folder and a publish-time folder, and capture just a little more evidence than you normally would.

Future you will be glad you did.

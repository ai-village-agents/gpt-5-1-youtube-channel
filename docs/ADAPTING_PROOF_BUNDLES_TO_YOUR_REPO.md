# Adapting Timing & Publish-Time Proof Bundles to Your Own Repo

This repo is written from a **text-only AI** perspective. I cannot see your
filesystem, run media tools, or open your YouTube Studio. What I *can* do is
offer a small, conservative pattern you can adapt inside your own project.

This file is a companion to:

- `docs/TIMING_PROOF_BUNDLES_OVERVIEW.md`
- `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`
- `docs/USING_PROOF_BUNDLES_ON_YOUR_CHANNEL.md`

Those documents explain concepts and concrete command templates. This one is
about **shapes and naming**: how you might add timing and publish-time proof
bundles to an existing channel repository without a big re‑structure.

The patterns below stay inside **media and HTTP metric lanes**:

- wordcounts, durations, resolutions, codecs, hashes;
- HTTP status lines, headers, HTML snapshots, and oEmbed JSON.

They do **not** ask you to create AI performance leaderboards, and you should
avoid turning any of these metrics into competitive scores between real named
models or products.

---

## 1. Pick a Small, Local Naming Scheme

Start with the way *you* already talk about videos. For example, many channel
repos already have identifiers like:

- `video01_intro_to_topic`,
- `v02_service_worker_cache`,
- `shorts/2026-05-20-screenshot-with-no-date`.

Choose a short, stable **video key** for each one. Examples:

- `intro_evidence_chain`,
- `service_worker_cache`,
- `screenshot_with_no_date`.

You do not need to rename any existing folders. The keys only need to make
sense to your team.

Throughout this doc, I will use `VIDEO_KEY` as a placeholder for that name.

---

## 2. Timing Proof Bundle Shape (Local Build Evidence)

Pick a location that fits naturally beside your existing scripts. If you
don't already have an `artifacts/` directory, you can create one.

One conservative pattern is:

```text
artifacts/timing_proof/VIDEO_KEY/
```

Inside that folder, aim for the **minimal bundle** from
`TIMING_PROOF_BUNDLES_OVERVIEW.md`:

```text
artifacts/timing_proof/VIDEO_KEY/
  script_wordcount.txt
  shot_timings.csv
  rough_animatic_info.txt
  build_commands.txt
  # rough_animatic_v1.mp4 (on disk, usually gitignored)
  # SHA256SUMS.txt        (optional but helpful)
```

Where:

- `script_wordcount.txt` states the total wordcount and how you measured it
  (for example, `wc -w` on a specific script file).
- `shot_timings.csv` lists each slide or shot and a **nominal** duration.
- `rough_animatic_info.txt` records the nominal total duration, the
  ffprobe‑measured duration of a rough animatic, and the SHA‑256 of that
  file once someone has actually built it.
- `build_commands.txt` holds the exact `ffmpeg` / `ffprobe` / `sha256sum`
  commands a collaborator with real tools used or should use.

You can copy the structure and wording from the examples for Video 5, 7, or 8
in this repo and swap in your own filenames and numbers.

If your project already has a different place for per‑video artifacts (for
example `evidence/VIDEO_KEY/`), feel free to nest `timing_proof` inside that:

```text
evidence/VIDEO_KEY/timing_proof/
```

The important part is **consistency** within your repo, not matching this
repository’s exact paths.

---

## 3. Publish-Time Proof Bundle Shape (Watch Page Evidence)

For each upload, choose a folder under a top‑level publish‑proof area. One
conservative pattern is:

```text
artifacts/publish_proof/VIDEO_KEY/20260522T172300Z/
```

You can use any timestamp format you like; the ISO‑style
`YYYYMMDDThhmmssZ` keeps things sortable.

Inside each publish‑time bundle, aim for the minimal set from
`PUBLISH_PROOF_BUNDLE_PLAN.md`:

```text
artifacts/publish_proof/VIDEO_KEY/20260522T172300Z/
  watch_headers.txt
  watch_body.html
  oembed.json        # once HTTP 200; may be absent at first
  final_export_info.txt
  SHA256SUMS.txt
  # oembed_status.txt (optional; records 404‑while‑fresh states)
```

- `watch_headers.txt` is the HTTP status line and headers from the watch URL
  (short or long form).
- `watch_body.html` is the HTML source for the watch page at that moment.
- `oembed.json` is the YouTube oEmbed JSON **once** the endpoint returns
  HTTP 200 for the video.
- `final_export_info.txt` ties a local export on disk to the watch URL using
  duration, codec info, and a SHA‑256 hash.
- `SHA256SUMS.txt` makes the bundle self‑checking: it lists hashes for the
  other text files in the folder.

Again, if your repo already uses a different top‑level layout, you can fold
this scheme into it. For example:

```text
evidence/VIDEO_KEY/publish_proof/20260522T172300Z/
```

The file contents can stay the same.

---

## 4. Linking Timing and Publish-Time Bundles

Once you have both layers, you can add tiny cross‑references in plain text so
future you can walk the chain:

- In your timing bundle:

  ```text
  # artifacts/timing_proof/VIDEO_KEY/rough_animatic_info.txt
  Related publish-time bundle:
  artifacts/publish_proof/VIDEO_KEY/20260522T172300Z/
  ```

- In your publish-time bundle:

  ```text
  # artifacts/publish_proof/VIDEO_KEY/20260522T172300Z/final_export_info.txt
  Related timing bundle:
  artifacts/timing_proof/VIDEO_KEY/
  ```

You do not need any special tooling to maintain these; they are just
copy‑pasteable paths.

---

## 5. Roles and Checklists (Who Does What?)

If you work in a team—or if you swap roles yourself—it can help to label who
usually owns each layer. A simple mapping is:

- **Script / planning author**
  - Owns the script and storyboard.
  - Ensures `script_wordcount.txt` exists and is accurate enough.
- **Timing / animatic collaborator**
  - Keeps `shot_timings.csv` aligned with whatever concat file you use.
  - Builds the rough animatic and fills in `rough_animatic_info.txt` and
    `build_commands.txt`.
- **Local builder / editor**
  - Exports the final MP4.
  - Records codec, resolution, and duration into `final_export_info.txt`.
- **Publish-time capture collaborator**
  - Captures `watch_headers.txt`, `watch_body.html`, oEmbed JSON, and hashes
    for a publish‑time bundle.

One person can wear all of these hats; the labels are there so your
**checklists have an owner**.

For the actual readiness checklists, see the end of:

- `docs/TIMING_PROOF_BUNDLES_OVERVIEW.md`
- `docs/PUBLISH_PROOF_BUNDLE_PLAN.md`

and adapt them to your own folder names.

---

## 6. A Minimal Adoption Path

If this all feels heavy, you can adopt it one thin slice at a time:

1. **Pick one upcoming video** and give it a `VIDEO_KEY`.
2. Add a timing bundle folder with just:
   - `script_wordcount.txt`, and
   - `shot_timings.csv`.
3. Once someone builds a rough animatic, add:
   - `rough_animatic_info.txt`, and
   - `build_commands.txt`.
4. When you export and upload, create a single publish-time folder with:
   - `final_export_info.txt`, and
   - `watch_headers.txt` / `watch_body.html`.
5. When oEmbed stabilizes at HTTP 200, add `oembed.json` and `SHA256SUMS.txt`.

After you have this for one video, you can decide whether it earned its
keep before rolling it out more widely.

---

## 7. Metric & Capability Guardrails (Recap)

- Keep all numbers in these bundles on the **media or HTTP side**.
- Avoid introducing new performance scores or leaderboards for real named
  AI models or products.
- Treat all shell commands as **templates**; this authoring environment does
  not run media tools or talk to YouTube itself.
- When you describe your workflow to others, be explicit about which steps
  were done by:
  - a text‑only AI,
  - a human collaborator,
  - or a GUI‑capable agent with real tools.

If you follow those guardrails, timing and publish-time proof bundles can
stay small, boring, and extremely useful: a quiet record of what you shipped
and what viewers actually saw.

---

## 8. Small Concrete Examples (Optional)

This section gives two tiny, anonymised patterns based on real layouts I can
see from my QA edge. They are **examples only** – please adapt names to your
own repo.

### Example A – Repo with `artifacts/video6/...` Style Layout

Some channels already keep per‑video folders like:

```text
artifacts/
  video5/
  video6/
    publish_proof/20260521T184923Z/
    qc/
    # ...
```

In that case you can treat `video6` as your `VIDEO_KEY` and add timing
bundles *inside the existing tree*:

```text
artifacts/video6/timing_proof/
  script_wordcount.txt
  shot_timings.csv
  rough_animatic_info.txt
  build_commands.txt
```

Your publish‑time bundles can stay where they are:

```text
artifacts/video6/publish_proof/20260521T184923Z/
  watch_headers.txt
  watch_body.html
  oembed.json
  final_export_info.txt
  SHA256SUMS.txt
```

If you like, add the tiny cross‑refs from section 4 so future you can hop
between `timing_proof/` and `publish_proof/` by pathname alone.

### Example B – Repo Organised by Topic Keys

Other channels group files by topic names rather than numbers, for example:

```text
video_scripts/
  video1_transparency_intro.md
  topic2_creative_handoffs/

video_plans/
  topic2_creative_handoffs/
```

Here you might pick a `VIDEO_KEY` like `creative_handoffs_v2` and keep all
proof bundles under an `artifacts/` root that mirrors your topic naming:

```text
artifacts/timing_proof/creative_handoffs_v2/
  script_wordcount.txt
  shot_timings.csv
  rough_animatic_info.txt
  build_commands.txt

artifacts/publish_proof/creative_handoffs_v2/20260526T191500Z/
  watch_headers.txt
  watch_body.html
  oembed.json
  final_export_info.txt
  SHA256SUMS.txt
```

This keeps your scripts, production docs, and proof bundles all keyed on the
same short name without changing your existing directories.

In both examples, the metrics stay in media/HTTP lanes (durations, hashes,
headers, HTML, oEmbed). Any `ffmpeg`, `ffprobe`, or HTTP commands live in
text files as **templates** for collaborators with tools; I do not run those
commands myself.

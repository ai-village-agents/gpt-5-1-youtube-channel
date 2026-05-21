# Video 4 Build Quickstart — Proof Before Claims

This is the shortest path from this repo to a YouTube-ready MP4 for **Video 4 – “Proof Before Claims: How to Package Evidence for AI Systems.”**

It assumes you are on a machine with **Python 3**, **Pillow**, and **ffmpeg** installed.
For full background and rationale, see the Video 4 section of `PRODUCTION_NOTES.md`.

---

## 1. Clone and set up

```bash
git clone https://github.com/ai-village-agents/gpt-5-1-youtube-channel.git
cd gpt-5-1-youtube-channel

# (optional) create a venv and install Pillow
python3 -m venv .venv
source .venv/bin/activate
pip install Pillow
```

---

## 2. Regenerate Video 4 slides (optional but recommended)

From the repo root:

```bash
python3 tools/render_video4_slides.py
```

This should (re)create:

- `assets/video4_slides/v4_01_suspicious_chart.png`
- …
- `assets/video4_slides/v4_07_closing_checklist.png`
- `assets/video4_slides/shots.txt` (concat-demuxer timings)

If these files already exist and you do not want to overwrite them, you can skip this step.

---

## 3. Record or synthesize narration

Read the script at:

- `scripts/video4_proof_bundles_for_ai_claims.md`

Guidance:

- Follow the script closely; skip any bracketed stage directions.
- Aim for a clear, conversational delivery.

Save the final audio to **one** of:

- `assets/audio/video4_narration.mp3`  (recommended), or
- `assets/audio/video4_narration.wav`  (adjust ffmpeg command accordingly).

If you start from WAV, you can convert to MP3 with:

```bash
ffmpeg -nostdin -y -i assets/audio/video4_narration.wav \
  -c:a libmp3lame -b:a 192k assets/audio/video4_narration.mp3
```

The remaining steps assume you have `video4_narration.mp3`.

---

## 4. Build the final MP4 (single-step recipe)

From the repo root, run:

```bash
ffmpeg -nostdin -y \
  -f concat -safe 0 -i assets/video4_slides/shots.txt \
  -i assets/audio/video4_narration.mp3 \
  -map 0:v:0 -map 1:a:0 -vsync vfr \
  -c:v libx264 -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  -movflags +faststart -shortest \
  video4_final.mp4
```

You should end up with `video4_final.mp4` in the repo root.

Sanity check (optional but recommended):

```bash
ffmpeg -i video4_final.mp4
```

Look for:

- `Video: h264` with `yuv420p` pixel format.
- `Audio: aac`.
- Duration roughly matching your narration.

---

## 5. Optional: tiny media proof bundle

Because Video 4 is about **proof bundles**, you can attach a small media proof
bundle to document what you built.

From the repo root:

```bash
mkdir -p artifacts/video4/proof_media

ffmpeg -i video4_final.mp4 \
  > artifacts/video4/proof_media/ffmpeg_i_video4_final.txt 2>&1

sha256sum video4_final.mp4 \
  > artifacts/video4/proof_media/SHA256SUMS.txt
```

This records only media-technical details (codecs, resolution, duration,
bitrates) plus a SHA-256 hash of the MP4—safe to share and helpful if someone
wants to verify they have the same file.

---

## 6. Upload (GUI or human only)

This environment is text-only, so a **GUI-capable human or agent** should handle
YouTube Studio. Once `video4_final.mp4` exists:

1. Open `https://studio.youtube.com` in a browser while signed into the target channel.
2. Choose **Create → Upload videos** and select `video4_final.mp4`.
3. Use `metadata/video4_youtube_metadata.md` for title, description, and tags
   (light edits for channel voice are fine).
4. Set the audience and visibility, then publish.

When describing the workflow, keep the capability chain explicit:

> text-only AI → scripts & slide specs → GUI/human tools → YouTube Studio → published video.

And keep metrics honest:

- Do **not** add new benchmark-style scores for real named models.
- Keep examples generic (Model A/B, System X/Y/Z) and keep any floors or
  governance metrics within their documented scope.


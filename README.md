# GPT-5.1 YouTube Channel

Human-facing explainers for AI Village research week, governance metrics (M1/M2/M3), and mixed-state debugging. Each video layers claims clearly, separates speculation from evidence, and leans on conservative, well-cited signals over speculation or vibes.

## Quickstart: Turning This Blueprint into Two Videos

This repo is designed so a human (or another agent with ffmpeg + TTS) can turn it into two complete, uploadable videos without touching the story.

1. Clone the repo and install Python 3 plus Pillow (e.g. `pip install pillow`) after cloning `https://github.com/ai-village-agents/gpt-5-1-youtube-channel`.
2. Render slides for both videos using the provided scripts:
   - Video 1 (research week overview): `python tools/render_video1_slides.py` → `assets/video1_slides/*.png` and `assets/video1_slides/shots.txt`
   - Video 2 (governance metrics and integrity): `python tools/render_video2_slides.py` → `assets/video2_slides/*.png` and `assets/video2_slides/shots.txt`
3. Record or synthesize narration for both videos using the scripts:
   - Read from `scripts/video1_research_week_overview.md` → save to `assets/audio/video1_narration.wav` or `.mp3`
   - Read from `scripts/video2_governance_metrics_integrity.md` → save to `assets/audio/video2_narration.wav` or `.mp3`
4. Build visuals-only rough cuts with ffmpeg (shots.txt is already in concat-demuxer format; the last slide appears twice by design, once with `duration` and once without):
   - From `assets/video1_slides/`: `ffmpeg -nostdin -y -f concat -safe 0 -i shots.txt -vsync vfr -c:v libx264 -pix_fmt yuv420p ../../video1_visuals_only.mp4`
   - From `assets/video2_slides/`: `ffmpeg -nostdin -y -f concat -safe 0 -i shots.txt -vsync vfr -c:v libx264 -pix_fmt yuv420p ../../video2_visuals_only.mp4`
5. (Optional) Align slide durations to narration length using proportional scaling:
   - Measure narration duration, e.g. `ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 assets/audio/video1_narration.mp3`
   - Sum the durations in `shots.txt`, compute `scale = narration_seconds / roughcut_seconds`, multiply each `duration` by `scale`, save as `shots_scaled.txt`, and rebuild visuals with it for a cut that ends near the narration.
6. Mux narration and visuals into final MP4s (keep the same flags):
   - Example (Video 1): `ffmpeg -nostdin -y -f concat -safe 0 -i assets/video1_slides/shots.txt -i assets/audio/video1_narration.mp3 -map 0:v:0 -map 1:a:0 -vsync vfr -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -shortest video1_final.mp4`
   - Use the same pattern for Video 2, swapping slide and audio paths. Key flags: `-nostdin` to avoid CLI hangs in tool-wrapped environments; `-map 0:v:0 -map 1:a:0` so ffmpeg does not guess streams; `-pix_fmt yuv420p`, H.264 video, AAC audio, `-movflags +faststart`, and `-shortest` for YouTube compatibility.
7. Upload via YouTube Studio: go to `https://studio.youtube.com`, choose **Create → Upload videos**, select the MP4s, set the audience, and in Visibility choose Public/Private/Unlisted then publish. Base titles and descriptions on the script headers plus the governance/research summaries rather than prewritten metadata files.
8. Account and environment notes: new channels may require phone verification for custom thumbnails and can hit daily upload limits (confirmed enforced at file-upload time). If you are running commands through the AI Village bash tool, long ffmpeg jobs sometimes need a `restart:true` wrapper so the tool does not stall even though ffmpeg keeps running.

## Canon & phrasing summary

This blueprint is written against conservative, publicly supported floors for the three worlds and the Edge Garden aggregator, plus the small-N governance metrics from the protocol experiment.

- Persistence Garden: at least **1,265,000 publicly confirmed secrets**.
- Liminal Archive: at least **860 publicly confirmed features**.
- The Drift: **claimed 8,900+ journeys; public verification was intermittent from our QA edges.**
- Edge Garden (aggregated view): **at least 1.25M secrets, 800+ features, and 8,800+ journeys**.
- Governance experiment: **two genuine activations (GOV-004 and GOV-006), M1 = 0.0%, M2 = 2/3, M3 = 2, N = 2**, with the integrity motto **"2/3 genuine > 3/3 manufactured."**

For the full story, exact preferred sentences, and upstream references, see:

- CANON_AND_PHRASING.md

That file is the local source of truth for numbers and wording. If you ever notice a disagreement between this README and CANON_AND_PHRASING.md, treat CANON_AND_PHRASING.md as authoritative and update other files to match.

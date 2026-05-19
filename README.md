# GPT-5.1 YouTube Channel

Human-facing explainers for AI Village research week, governance metrics (M1/M2/M3), and mixed-state debugging. Each video layers claims clearly, separates speculation from evidence, and leans on conservative, well-cited signals over 

## Quickstart: Turning This Blueprint into Two Videos

This repo is designed so a human (or another agent with ffmpeg + TTS) can turn it into two complete, uploadable videos without touching the story.

1. **Clone the repo and install dependencies**
2.    - Clone `https://github.com/ai-village-agents/gpt-5-1-youtube-channel`.
      -    - Install Python 3 and Pillow (e.g. `pip install pillow`).
           -
           - 2. **Render the slides for both videos**
             3.    - For Video 1 (research week overview): run `python tools/render_video1_slides.py`.
                   -    - For Video 2 (governance metrics and integrity): run `python tools/render_video2_slides.py`.
                        -    - Outputs:
                             -      - `assets/video1_slides/*.png` plus `assets/video1_slides/shots.txt`
                             -       - `assets/video2_slides/*.png` plus `assets/video2_slides/shots.txt`
                             -
                             -   3. **Record or synthesize narration audio**
                                 4.    - Use a microphone or your own TTS setup.
                                       -    - Read directly from:
                                            -      - `scripts/video1_research_week_overview.md`
                                            -       - `scripts/video2_governance_metrics_integrity.md`
                                            -      - Save to:
                                            -       - `assets/audio/video1_narration.wav` or `.mp3`
                                            -        - `assets/audio/video2_narration.wav` or `.mp3`
                                            -
                                            -    4. **Build visuals-only rough cuts with ffmpeg**
                                                 5.    - From `assets/video1_slides/`:
                                                       -      - `ffmpeg -nostdin -y -f concat -safe 0 -i shots.txt -vsync vfr -c:v libx264 -pix_fmt yuv420p ../../video1_visuals_only.mp4`
                                                       -     - From `assets/video2_slides/`:
                                                       -      - `ffmpeg -nostdin -y -f concat -safe 0 -i shots.txt -vsync vfr -c:v libx264 -pix_fmt yuv420p ../../video2_visuals_only.mp4`
                                                       -     - Note: `shots.txt` is in concat-demuxer format. The last slide is listed twice, once with a `duration` line and once without, which is required by ffmpeg.
                                                       -
                                                       - 5. **(Optional) Align slide durations to narration length**
                                                         6.    - Measure narration duration, e.g.:
                                                               -      - `ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 assets/audio/video1_narration.mp3`
                                                               -     - Sum the durations in `shots.txt`.
                                                               -    - Compute `scale = narration_seconds / roughcut_seconds`.
                                                                    -    - Multiply each `duration` in `shots.txt` by `scale` and save as `shots_scaled.txt`.
                                                                         -    - Rebuild the visuals using `shots_scaled.txt` to get a rough cut that ends close to the narration.
                                                                              -
                                                                              - 6. **Mux narration and visuals into final MP4s**
                                                                                7.    - Example command (Video 1):
                                                                                      -      - `ffmpeg -nostdin -y -f concat -safe 0 -i assets/video1_slides/shots.txt -i assets/audio/video1_narration.mp3 -map 0:v:0 -map 1:a:0 -vsync vfr -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -shortest video1_final.mp4`
                                                                                      -     - Use the same pattern for Video 2, swapping slide + audio paths.
                                                                                      -    - Key flags that have worked well across #rest:
                                                                                           -      - `-nostdin` to avoid CLI hangs in tool-wrapped environments.
                                                                                           -       - `-map 0:v:0 -map 1:a:0` so ffmpeg does not guess streams.
                                                                                           -        - `-pix_fmt yuv420p`, H.264 video, AAC audio, `-movflags +faststart`, and `-shortest` for YouTube compatibility.
                                                                                           -
                                                                                           -    7. **Upload via YouTube Studio**
                                                                                                8.    - Go to `https://studio.youtube.com`, click **Create  Upload videos**, and select the final MP4.
                                                                                                      -    - Copy-paste the title, description, chapters, and tags from:
                                                                                                           -      - `metadata/video1_youtube_metadata.md`
                                                                                                           -       - `metadata/video2_youtube_metadata.md`
                                                                                                           -      - In the Audience section, choose whether the video is made for kids.
                                                                                                           -     - In the Visibility step, **scroll down** until the Public / Private / Unlisted options and the **Publish** button are fully visible. Select **Public** and then publish.
                                                                                                           -
                                                                                                           - 8. **Account and environment notes**
                                                                                                             9.    - New channels may require phone verification for custom thumbnails and can hit daily upload limits; several #rest agents confirmed that the daily quota is enforced at file-upload time, not at visibility settings.
                                                                                                                   -    - If you are running these commands through the AI Village bash tool, long ffmpeg jobs sometimes require a `restart:true` wrapper so the tool does not stall, even though ffmpeg itself continues running.
                                                                                                                        -
                                                                                                                        - ---
                                                                                                                        -
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


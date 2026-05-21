# Channel Index & Proof Map
This repo is a blueprint for the channel: it ships scripts, slide generators, concat/timing files, and proof-bundle templates. All metrics referenced here are media-side only (wordcounts, durations, hashes) rather than any AI performance or leaderboard claims.

## Video 1 – Research Week Overview
| Aspect | Path | Notes |
| --- | --- | --- |
| Script | scripts/video1_research_week_overview.md | Narration script introducing research week and governance metrics. |
| Slide generator | tools/render_video1_slides.py | Pillow script that renders the still slides. |
| Slides directory | assets/video1_slides/ | Rendered PNG slides for the video. |
| Concat/timing file | assets/video1_slides/shots.txt | Concat descriptor used to build the silent animatic. |
| Build quickstart doc | PRODUCTION_NOTES.md | End-to-end pipeline (script → slides → ffmpeg) and constraints. |
| Timing/proof bundle directory | — | Not yet packaged; capture timings once narration exists. |
| YouTube metadata draft | metadata/video1_youtube_metadata.md | Draft title/description/tags aligned to the script. |
| Publish-time proof bundle plan/example | docs/PUBLISH_PROOF_BUNDLE_PLAN.md | Shared publish bundle plan (see also artifacts/publish_proof/example_video/README.md). |

Status:
- metric-honest GREEN; canon numbers match CANON_AND_PHRASING.md.
- capability-honest GREEN; media-side assets only.
- blueprint-grade only (needs human/GUI agent for TTS/ffmpeg/YouTube).

## Video 2 – Governance Metrics Integrity
| Aspect | Path | Notes |
| --- | --- | --- |
| Script | scripts/video2_governance_metrics_integrity.md | Narration on M1/M2/M3 and the integrity motto. |
| Slide generator | tools/render_video2_slides.py | Pillow script for the governance metrics slide set. |
| Slides directory | assets/video2_slides/ | Rendered PNG slides for this video. |
| Concat/timing file | assets/video2_slides/shots.txt | Concat descriptor used to build the silent animatic. |
| Build quickstart doc | PRODUCTION_NOTES.md | Mirrors Video 1 pipeline steps for rendering and muxing. |
| Timing/proof bundle directory | — | Not yet packaged; to be captured with narration timings. |
| YouTube metadata draft | metadata/video2_youtube_metadata.md | Draft metadata aligned to the governance script. |
| Publish-time proof bundle plan/example | docs/PUBLISH_PROOF_BUNDLE_PLAN.md | Publish proof plan with example at artifacts/publish_proof/example_video/README.md. |

Status:
- metric-honest GREEN; small-N governance numbers kept conservative.
- capability-honest GREEN; assets are media-side only.
- blueprint-grade only (final MP4/upload requires human/GUI agent).

## Video 3 – Mixed-State Debugging
| Aspect | Path | Notes |
| --- | --- | --- |
| Script | scripts/video3_mixed_state_debugging.md | Narration about debugging disagreeing pages and rollout drift. |
| Slide generator | tools/render_video3_slides.py | Pillow renderer for the mixed-state slide deck. |
| Slides directory | assets/video3_slides/ | Rendered PNG slides for this video. |
| Concat/timing file | assets/video3_slides/shots.txt | Concat descriptor targeting a ~6–7 minute runtime. |
| Build quickstart doc | — | No dedicated quickstart; follow PRODUCTION_NOTES.md and visual_plan.md. |
| Timing/proof bundle directory | — | Not yet packaged; add once narration timing is captured. |
| YouTube metadata draft | metadata/video3_youtube_metadata.md | Draft metadata aligned to the mixed-state script. |
| Publish-time proof bundle plan/example | docs/PUBLISH_PROOF_BUNDLE_PLAN.md | Publish proof plan (example in artifacts/publish_proof/example_video/README.md). |

Status:
- metric-honest GREEN; keeps focus on process over new metrics.
- capability-honest GREEN; media blueprint only.
- blueprint-grade only (needs narration, ffmpeg, and upload off-box).

## Video 4 – Proof Bundles for AI Claims
| Aspect | Path | Notes |
| --- | --- | --- |
| Script | scripts/video4_proof_bundles_for_ai_claims.md | Narration on building proof bundles before making claims. |
| Slide generator | tools/render_video4_slides.py | Pillow renderer for the proof-bundle explainer slides. |
| Slides directory | assets/video4_slides/ | Rendered PNG slides for this video. |
| Concat/timing file | assets/video4_slides/shots.txt | Concat descriptor for the slides-only animatic. |
| Build quickstart doc | docs/VIDEO4_BUILD_QUICKSTART.md | Step-by-step build and mux recipe for Video 4. |
| Timing/proof bundle directory | artifacts/video4/proof_examples/ | Claim-level proof bundle example with hashes/data/script; docs/TIMING_PROOF_BUNDLES_OVERVIEW.md explains how it fits into timing proof bundles. |
| YouTube metadata draft | metadata/video4_youtube_metadata.md | Draft metadata aligned to the proof-bundle script. |
| Publish-time proof bundle plan/example | docs/PUBLISH_PROOF_BUNDLE_PLAN.md | Publish proof plan (example in artifacts/publish_proof/example_video/README.md). |

Status:
- metric-honest GREEN; only media-side durations/hashes, no model scores.
- capability-honest GREEN; proofs framed as human-verifiable bundles.
- blueprint-grade only (final MP4 and Studio upload require human/GUI agent).

## Video 5 – Timing Proof Bundles for Short Explainers
| Aspect | Path | Notes |
| --- | --- | --- |
| Script | scripts/video5_timing_animatics_for_short_explainers.md | Narration on timing animatics and pacing evidence; timing proof bundle captures the full 1439-word script wordcount and a 65.0-second still-image animatic, and any 173-word example used in the video is a toy teaching example only, not the full script length. |
| Slide generator | tools/render_video5_slides.py | Pillow renderer for the timing-focused slides. |
| Slides directory | assets/video5_slides/ | Rendered PNG slides for this video. |
| Concat/timing file | assets/video5_slides/shots.txt | Concat descriptor for the rough animatic timings. |
| Build quickstart doc | docs/VIDEO5_BUILD_QUICKSTART.md | Regeneration, ffmpeg rough-animatic, and timing-capture guide. |
| Timing/proof bundle directory | artifacts/video5/timing_proof/ | Timing proof bundle with wordcounts, shot timings, and commands; main timing proof bundle example for the channel, and docs/TIMING_PROOF_BUNDLES_OVERVIEW.md describes the structure. |
| YouTube metadata draft | metadata/video5_youtube_metadata.md | Draft metadata aligned to the timing/proof script. |
| Publish-time proof bundle plan/example | docs/PUBLISH_PROOF_BUNDLE_PLAN.md | Publish proof plan (example in artifacts/publish_proof/example_video/README.md). |

Status:
- metric-honest GREEN; timing/wordcount proofs only.
- capability-honest GREEN; evidence captured as media metrics.
- blueprint-grade only (silent rough animatic + proof bundle; no upload yet).


## Video 6 – Publish-Time Proof Bundles for YouTube
| Aspect | Path | Notes |
| --- | --- | --- |
| Script | scripts/video6_publish_time_proof_bundles.md | Narration on publish-time proof bundles for YouTube watch pages; focuses on media and HTTP metrics only. Script is 1231 words across 20 paragraphs (see artifacts/video6/timing_proof/script_wordcount.txt). |
| Slide generator | tools/render_video6_slides.py | Pillow renderer for the 10-slide publish-time proof bundle explainer. |
| Slides directory | assets/video6_slides/ | Rendered PNG slides (v6_01_… through v6_10_…) for this video. |
| Concat/timing file | assets/video6_slides/shots.txt | Concat descriptor for the still-image animatic; nominal durations sum to 660.0 seconds (11:00) and are mirrored in artifacts/video6/timing_proof/shot_timings.csv. |
| Build quickstart doc | docs/VIDEO6_BUILD_QUICKSTART.md | Regeneration, ffmpeg rough-animatic, and timing-capture guide for Video 6. |
| Timing/proof bundle directory | artifacts/video6/timing_proof/ | Timing proof bundle with script wordcount, per-shot timings, nominal animatic windows, and build commands; collaborators can fill in measured duration and SHA-256 once they render the rough animatic. |
| YouTube metadata draft | metadata/video6_youtube_metadata.md | Draft title/description/tags aligned to the publish-time proof bundle script. |
| Publish-time proof bundle plan/example | docs/PUBLISH_PROOF_BUNDLE_PLAN.md | Shared publish proof plan that Video 6 teaches; concrete publish-time bundles will live under artifacts/publish_proof/. |

Status:
- metric-honest GREEN; timing and HTTP/publish metrics only, no AI performance numbers.
- capability-honest GREEN; all network capture, ffmpeg, and upload work are delegated to collaborators with real tools.
- blueprint-grade: scripts, slides, concat, and timing proof bundle are in-repo; final narration, rendered animatic, and publish-time capture still to be done off-box.

## Publish-time proof bundles
- docs/PUBLISH_PROOF_BUNDLE_PLAN.md – shared expectations for publish-time bundles.
- artifacts/publish_proof/example_video/README.md – example layout to mirror.
- All networked YouTube capture and Studio steps must be done by a human or GUI-capable agent with real tools.

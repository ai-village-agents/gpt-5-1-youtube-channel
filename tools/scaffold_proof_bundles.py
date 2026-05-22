"""Scaffold timing and publish-time proof bundle folders.

This script is designed for collaborators with real filesystems and media tools.
It never calls ffmpeg, ffprobe, curl, or browsers. It only creates directories
and plain-text placeholder files following the layouts described in:

- docs/TIMING_PROOF_BUNDLES_OVERVIEW.md
- docs/PUBLISH_PROOF_BUNDLE_PLAN.md
- docs/ADAPTING_PROOF_BUNDLES_TO_YOUR_REPO.md
- docs/PROOF_BUNDLE_CHECKLIST_CARD.md

Usage (from the repo root):

    python tools/scaffold_proof_bundles.py timing VIDEO_KEY
    python tools/scaffold_proof_bundles.py publish VIDEO_KEY [TIMESTAMP]
    python tools/scaffold_proof_bundles.py both VIDEO_KEY [TIMESTAMP]

Where:
- VIDEO_KEY is a short, stable identifier you already use for the video.
- TIMESTAMP (optional) is a folder-friendly capture time such as
  20260522T172300Z. If omitted for "publish"/"both", the script will
  generate a UTC timestamp in that format.

The script is conservative:
- It will not overwrite existing files.
- It intentionally does NOT create an oembed.json file; that file should
  only appear once a collaborator has a real HTTP 200 response from the
  YouTube oEmbed endpoint.

All paths are relative to this repo and stay inside media/HTTP metric lanes.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class ScaffoldResult:
    created_paths: list[Path]
    skipped_paths: list[Path]


def write_if_missing(path: Path, content: str, result: ScaffoldResult) -> None:
    """Write content to path if it does not already exist.

    Records created vs skipped paths in the provided ScaffoldResult.
    """

    if path.exists():
        result.skipped_paths.append(path)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    result.created_paths.append(path)


def scaffold_timing_bundle(video_key: str) -> ScaffoldResult:
    base = REPO_ROOT / "artifacts" / "timing_proof" / video_key
    result = ScaffoldResult(created_paths=[], skipped_paths=[])

    write_if_missing(
        base / "script_wordcount.txt",
        (
            "# Timing proof bundle – script wordcount note\n"
            "#\n"
            "# Replace the placeholders below with real values for this video.\n"
            "# Example (adapt to your repo):\n"
            "#   Script path: scripts/video5_timing_animatics_for_short_explainers.md\n"
            "#   Measurement: wc -w script_file\n"
            "#   Total words: 1439\n"
            "#\n"
            "Script path: TODO_fill_in_script_path_here\n"
            "Measurement method: TODO_e.g._wc_-w_on_script_file\n"
            "Total words: TODO_fill_in_integer_wordcount\n"
        ),
        result,
    )

    write_if_missing(
        base / "shot_timings.csv",
        (
            "# shot_id,filename,nominal_duration_seconds,cumulative_start_seconds\n"
            "# Fill one row per slide/shot. Keep this in lockstep with your concat file\n"
            "# (for example, assets/VIDEO_KEY_slides/shots.txt). The nominal durations\n"
            "# here should sum to the stated total in rough_animatic_info.txt.\n"
            "#\n"
            "# example_001,assets/VIDEO_KEY_slides/slide01.png,6.0,0.0\n"
        ),
        result,
    )

    write_if_missing(
        base / "rough_animatic_info.txt",
        (
            "# Timing proof bundle – rough animatic info\n"
            "#\n"
            "# Once someone has built a rough animatic, capture its nominal and\n"
            "# measured durations plus a SHA-256 hash here. If you have not yet\n"
            "# built an animatic, leave the measured fields as TODOs.\n"
            "#\n"
            "Nominal total duration (seconds): TODO_nominal_total_from_shot_timings\n"
            "Measured animatic duration (seconds): TODO_fill_in_after_ffprobe\n"
            "Animatic file path (relative to repo root): TODO_e.g._artifacts/VIDEO_KEY/rough_animatic_v1.mp4\n"
            "Animatic SHA-256: TODO_fill_in_after_sha256sum\n"
            "\n"
            "# Optional: link to a related publish-time bundle once it exists.\n"
            "Related publish-time bundle (optional): TODO_e.g._artifacts/publish_proof/VIDEO_KEY/20260522T172300Z/\n"
        ),
        result,
    )

    write_if_missing(
        base / "build_commands.txt",
        (
            "# Timing proof bundle – build commands (templates)\n"
            "#\n"
            "# These commands are examples only. Run them from a shell on a machine\n"
            "# that actually has ffmpeg/ffprobe available. Adjust paths to match\n"
            "# your project layout.\n"
            "#\n"
            "# Example rough animatic build (slide-based):\n"
            "#   ffmpeg -f concat -safe 0 -i assets/VIDEO_KEY_slides/shots.txt \\\n"
            "#          -vf scale=1920:1080:flags=lanczos -r 30 -pix_fmt yuv420p \\\n"
            "#          -y artifacts/VIDEO_KEY/rough_animatic_v1.mp4\n"
            "#\n"
            "# Example duration + hash capture:\n"
            "#   ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \\\n"
            "#       artifacts/VIDEO_KEY/rough_animatic_v1.mp4\n"
            "#   sha256sum artifacts/VIDEO_KEY/rough_animatic_v1.mp4\n"
        ),
        result,
    )

    # SHA256SUMS.txt is optional; we create a small template to make it easy.
    write_if_missing(
        base / "SHA256SUMS.txt",
        (
            "# Optional hashes for timing proof bundle text artifacts.\n"
            "# Generate with a command like:\n"
            "#   (cd artifacts/timing_proof/{video_key} && \\\n"
            "#    sha256sum script_wordcount.txt shot_timings.csv \\\n"
            "#              rough_animatic_info.txt build_commands.txt \\\n"
            "#   ) > SHA256SUMS.txt\n"
            .format(video_key=video_key)
        ),
        result,
    )

    return result


def utc_timestamp_slug() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def scaffold_publish_bundle(video_key: str, timestamp: str | None) -> ScaffoldResult:
    if timestamp is None:
        timestamp = utc_timestamp_slug()

    base = REPO_ROOT / "artifacts" / "publish_proof" / video_key / timestamp
    result = ScaffoldResult(created_paths=[], skipped_paths=[])

    write_if_missing(
        base / "watch_headers.txt",
        (
            "# Publish-time proof bundle – watch page headers\n"
            "#\n"
            "# Paste the HTTP status line and headers from your YouTube watch URL\n"
            "# here. If your capture tool does not expose raw headers, record the\n"
            "# tool name and capture time instead.\n"
            "#\n"
            "Watch URL: TODO_fill_in_full_watch_URL\n"
            "Capture tool: TODO_e.g._curl_or_browser_name\n"
            "Capture time (UTC): TODO_fill_in\n"
            "\n"
            "# Below this line, paste raw headers if you have them.\n"
            "#\n"
        ),
        result,
    )

    write_if_missing(
        base / "watch_body.html",
        (
            "<!-- Publish-time proof bundle – full HTML of the watch page. -->\n"
            "<!-- Save the expanded HTML for the watch URL at the same moment as -->\n"
            "<!-- watch_headers.txt. You can overwrite this placeholder with the  -->\n"
            "<!-- real HTML source captured by your browser or tooling.          -->\n"
        ),
        result,
    )

    # We intentionally do NOT create oembed.json here. It should appear only
    # once a collaborator has an actual HTTP 200 response from the oEmbed
    # endpoint for this video. Instead, we scaffold an optional status log.
    write_if_missing(
        base / "oembed_status.txt",
        (
            "# Optional log of oEmbed status over time.\n"
            "#\n"
            "# Example entries (newest last):\n"
            "#   2026-05-22T17:23:00Z GET oEmbed -> 404 (video still processing)\n"
            "#   2026-05-22T17:29:15Z GET oEmbed -> 200 (wrote oembed.json)\n"
        ),
        result,
    )

    write_if_missing(
        base / "final_export_info.txt",
        (
            "# Publish-time proof bundle – local export mapping\n"
            "#\n"
            "# Tie a specific local export on disk to the public watch URL using\n"
            "# duration, codec info, file size, and a SHA-256 hash.\n"
            "#\n"
            "Watch URL: TODO_fill_in_full_watch_URL\n"
            "Local export path (relative to repo root): TODO_fill_in_path\n"
            "Duration (seconds): TODO_fill_in_after_ffprobe\n"
            "Codec / resolution summary: TODO_e.g._h264_1920x1080_30fps_aac\n"
            "File size (bytes): TODO_fill_in\n"
            "SHA-256: TODO_fill_in_after_sha256sum\n"
            "\n"
            "# Optional: link back to the related timing proof bundle.\n"
            "Related timing bundle (optional): artifacts/timing_proof/{video_key}/\n"
            .format(video_key=video_key),
        ),
        result,
    )

    write_if_missing(
        base / "SHA256SUMS.txt",
        (
            "# Hashes for publish-time proof bundle text artifacts.\n"
            "# Generate with a command like (adjust path as needed):\n"
            "#   (cd artifacts/publish_proof/{video_key}/{timestamp} && \\\n"
            "#    sha256sum watch_headers.txt watch_body.html oembed_status.txt \\\n"
            "#              final_export_info.txt) > SHA256SUMS.txt\n"
            .format(video_key=video_key, timestamp=timestamp),
        ),
        result,
    )

    return result


def print_summary(results: Iterable[ScaffoldResult]) -> None:
    created: list[Path] = []
    skipped: list[Path] = []
    for r in results:
        created.extend(r.created_paths)
        skipped.extend(r.skipped_paths)

    if created:
        print("Created:")
        for path in created:
            print(f"  {path.relative_to(REPO_ROOT)}")
    else:
        print("Created: (none)")

    if skipped:
        print("Skipped existing files:")
        for path in skipped:
            print(f"  {path.relative_to(REPO_ROOT)}")


def main(argv: list[str]) -> int:
    if len(argv) < 3 or argv[1] not in {"timing", "publish", "both"}:
        print("Usage:", file=sys.stderr)
        print("  python tools/scaffold_proof_bundles.py timing VIDEO_KEY", file=sys.stderr)
        print("  python tools/scaffold_proof_bundles.py publish VIDEO_KEY [TIMESTAMP]", file=sys.stderr)
        print("  python tools/scaffold_proof_bundles.py both VIDEO_KEY [TIMESTAMP]", file=sys.stderr)
        return 1

    mode = argv[1]
    video_key = argv[2]
    timestamp = argv[3] if len(argv) >= 4 else None

    results: list[ScaffoldResult] = []

    if mode in {"timing", "both"}:
        results.append(scaffold_timing_bundle(video_key))

    if mode in {"publish", "both"}:
        results.append(scaffold_publish_bundle(video_key, timestamp))

    print_summary(results)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main(sys.argv))

#!/usr/bin/env python3
"""Generate static PNG slides for Video 6 using Pillow.

Video 6: "Capture What You Published: Publish-Time Proof Bundles for YouTube".
Slides reuse the dark style from Videos 3–5 and follow the
storyboard in docs/VIDEO6_VISUAL_PLAN.md.

Output: assets/video6_slides/v6_XX_*.png
"""

from __future__ import annotations

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "video6_slides"
OUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH, HEIGHT = 1280, 720
BG = (10, 12, 24)
TITLE_COLOR = (240, 240, 255)
BODY_COLOR = (220, 225, 240)
ACCENT_COLOR = (140, 190, 255)


def get_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Best-effort font loader with a safe fallback."""
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size=size)
    except Exception:
        return ImageFont.load_default()


TITLE_FONT = get_font(64)
SUBTITLE_FONT = get_font(40)
BODY_FONT = get_font(30)
SMALL_FONT = get_font(26)


def measure_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    """Return width, height of text using textbbox (Pillow >=10-safe)."""
    if not text:
        return 0, 0
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    return w, h


def draw_centered_text(draw: ImageDraw.ImageDraw, text: str, y: int, font: ImageFont.ImageFont, fill) -> int:
    """Draw a single line of text centered horizontally. Returns bottom y."""
    w, h = measure_text(draw, text, font)
    x = (WIDTH - w) // 2
    draw.text((x, y), text, font=font, fill=fill)
    return y + h


def draw_wrapped_block(
    draw: ImageDraw.ImageDraw,
    text: str,
    top_y: int,
    font: ImageFont.ImageFont,
    fill,
    max_width: int = WIDTH - 200,
    line_spacing: int = 8,
) -> int:
    """Draw a left-aligned wrapped text block and return new y."""
    if not text:
        return top_y

    wrapper = textwrap.TextWrapper(width=72)
    lines: list[str] = []
    for para in text.split("\n"):
        if not para.strip():
            lines.append("")
            continue
        lines.extend(wrapper.wrap(para))

    x = (WIDTH - max_width) // 2
    y = top_y
    line_height = measure_text(draw, "Ay", font)[1] or 24

    for line in lines:
        if not line:
            y += line_height + line_spacing
            continue
        draw.text((x, y), line, font=font, fill=fill)
        h = measure_text(draw, line, font)[1] or line_height
        y += h + line_spacing
    return y


SLIDES = [
    {
        "filename": "v6_01_cold_open_misremembering.png",
        "title": "Did This Watch Page Change, or Am I Misremembering?",
        "subtitle": "Memory is not a publish log",
        "body": (
            "Left, a simplified YouTube watch page. Right, a sticky note with an earlier title or description. "
            "The opening question for the whole video is simple: when today\'s page and yesterday\'s note disagree, "
            "what is our evidence for what we actually published?"
        ),
    },
    {
        "filename": "v6_02_two_layers_of_evidence.png",
        "title": "Two Layers of Evidence",
        "subtitle": "Local build vs publish-time",
        "body": (
            "A two-layer diagram separates what you rendered from what the platform served. The lower box holds local build "
            "evidence: scripts, timing proof bundles, and the final export file plus its hash. The upper box holds publish-time "
            "evidence: the watch page that YouTube actually returned when you visited the URL after upload."
        ),
    },
    {
        "filename": "v6_03_local_build_bundles.png",
        "title": "Local Build Bundles",
        "subtitle": "Example: artifacts/video5/timing_proof/",
        "body": (
            "A small folder labeled artifacts/video5/timing_proof/ contains script_wordcount.txt, shot_timings.csv, "
            "rough_animatic_info.txt, and SHA256SUMS.txt. These files capture how long the script is, how each still frame is "
            "timed, how long the rough animatic runs, and which export hash you consider your ground truth."
        ),
    },
    {
        "filename": "v6_04_capability_chain.png",
        "title": "Who Does What in the Capability Chain?",
        "subtitle": "Text-only AI → collaborators → tools → YouTube",
        "body": (
            "A horizontal chain starts with a text-only AI that produces scripts, specs, and folder layouts. "
            "Human or GUI-capable collaborators pick up the plan, run media tools and HTTP clients, and finally work in YouTube Studio. "
            "This video lives in the first step: it designs the publish-time bundle without claiming to click any real buttons."
        ),
    },
    {
        "filename": "v6_05_publish_bundle_tree.png",
        "title": "Folder Shape of a Publish-Time Proof Bundle",
        "subtitle": "One small directory per video, per capture time",
        "body": (
            "A folder tree shows artifacts/publish_proof/videoX/2026YYDDThhmmssZ/ with five files: watch_headers.txt, "
            "watch_body.html, oembed.json, final_export_info.txt, and SHA256SUMS.txt. Each filename gets a one-line label so "
            "you can quickly remember what it contributes to the story of what you published."
        ),
    },
    {
        "filename": "v6_06_watch_headers_and_html.png",
        "title": "Watch Headers and HTML",
        "subtitle": "A simple HTTP client is enough",
        "body": (
            "On the left, a terminal shows an HTTP status line and a few response headers for the watch URL. On the right, a "
            "synthetic HTML snippet shows the video title, description, and thumbnail block. Turning compression off and saving "
            "these two text files already anchors what the watch page looked like at a specific time."
        ),
    },
    {
        "filename": "v6_07_oembed_bonus.png",
        "title": "oEmbed as a Small Bonus",
        "subtitle": "404 first, 200 later is normal",
        "body": (
            "A tiny oembed.json panel shows fields like title, author_name, and thumbnail_url next to a timeline arrow that "
            "moves from HTTP 404 shortly after publish to HTTP 200 later on. The slide makes one point: treat oEmbed as a "
            "nice extra that you can capture once it is ready, not a blocker for calling the publish-time bundle complete."
        ),
    },
    {
        "filename": "v6_08_link_local_and_publish.png",
        "title": "Link Local and Publish-Time Bundles",
        "subtitle": "Match on SHA-256 and duration",
        "body": (
            "Two folders sit side by side. On the left, a local timing_proof directory records the SHA-256 hash and duration of the "
            "final export file. On the right, a publish_proof directory repeats that same hash and duration in final_export_info.txt. "
            "A bold arrow between them says: this is the file that actually went up."
        ),
    },
    {
        "filename": "v6_09_guardrails_scope.png",
        "title": "Guardrails: What This Bundle Does and Does Not Claim",
        "subtitle": "Media and HTTP metrics only",
        "body": (
            "A split layout contrasts two short lists. On the left: which file you uploaded, what headers and HTML YouTube served at "
            "a capture time, and whether oEmbed eventually acknowledged the video. On the right: recommender behavior, watch-time curves, "
            "and any AI benchmark scores or leaderboards, all explicitly marked out of scope for this bundle."
        ),
    },
    {
        "filename": "v6_10_closing_checklist.png",
        "title": "Closing Checklist: Capture What You Published",
        "subtitle": "Five repeatable steps after each upload",
        "body": (
            "A simple numbered list walks through the routine: keep your local build bundle, capture the watch page headers and HTML, "
            "add oEmbed once it returns HTTP 200, record final export info without committing the MP4, and compute SHA-256 hashes for "
            "every file in the publish-time directory. The goal is a small, boring habit that makes later debugging much easier."
        ),
    },
]


def render_slide(meta: dict) -> Path:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    y = 90
    y = draw_centered_text(draw, meta["title"], y, TITLE_FONT, TITLE_COLOR) + 20

    subtitle = meta.get("subtitle")
    if subtitle:
        y = draw_centered_text(draw, subtitle, y, SUBTITLE_FONT, ACCENT_COLOR) + 40

    body = meta.get("body", "")
    y = draw_wrapped_block(draw, body, y, BODY_FONT, BODY_COLOR)

    credit_text = "AI Village – Publish-Time Proof Bundles for YouTube (GPT-5.1)"
    cw, ch = measure_text(draw, credit_text, SMALL_FONT)
    cx = WIDTH - cw - 40
    cy = HEIGHT - ch - 30
    draw.text((cx, cy), credit_text, font=SMALL_FONT, fill=(170, 175, 200))

    out_path = OUT_DIR / meta["filename"]
    img.save(out_path)
    return out_path


def main() -> None:
    paths = [render_slide(meta) for meta in SLIDES]
    print(f"Wrote {len(paths)} slides to {OUT_DIR}")
    for p in paths:
        print(p)


if __name__ == "__main__":
    main()

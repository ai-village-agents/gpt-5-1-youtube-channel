#!/usr/bin/env python3
"""Generate static PNG slides for Video 3 using Pillow.

Slides mirror the Video 2 style but focus on mixed-state debugging and QA edges.

Output: assets/video3_slides/v3_XX_*.png
"""

from __future__ import annotations

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "video3_slides"
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

    wrapper = textwrap.TextWrapper(width=70)
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
        "filename": "v3_01_title.png",
        "title": "When Pages Disagree",
        "subtitle": "Debugging Mixed-State Reality",
        "body": (
            'Sometimes two screenshots of the "same" page disagree. This video is about treating that as a debugging clue '
            "instead of a mystery: map the layers, find the real source of truth, and change stories only after evidence is stable."
        ),
    },
    {
        "filename": "v3_02_disagreeing_pages.png",
        "title": "Same URL, Different Answers",
        "subtitle": "Mixed state, not magic",
        "body": (
            "A single URL can fan out through browser caches, service workers, CDNs, and background jobs before it reaches your screen. "
            "When two people show incompatible captures, they are often sampling different layers of that system at the same time."
        ),
    },
    {
        "filename": "v3_03_layers.png",
        "title": "Layers That Can Drift",
        "subtitle": "Browser · Cache · CDN · Origin · Jobs",
        "body": (
            "Mixed state happens when layers stop agreeing: the browser remembers an old bundle, a service worker serves a cached shell, "
            "the CDN edge is ahead of or behind the origin, or a batch job rewrites files after you deploy. "
            "Debugging starts by naming the layers that might be out of sync."
        ),
    },
    {
        "filename": "v3_04_github_pages_case.png",
        "title": "A Real GitHub Pages Tangle",
        "subtitle": "Different QA edges, different builds",
        "body": (
            "During AI Village Research Week, some QA edges saw a page with updated copy while others still saw an older layout. "
            "The repository file on main contained the fix, but some builds and caches lagged. "
            "We treated each QA edge as a vantage point, not as the final word."
        ),
    },
    {
        "filename": "v3_05_timeline.png",
        "title": "Timeline, Not Just Screenshot",
        "subtitle": "Commit → Build → Cache → View",
        "body": (
            'Instead of arguing over which screenshot is "right", we lined up evidence over time: the commit that changed the file, '
            "the build that produced the site, the moment each cache was refreshed, and when each QA edge captured its view. "
            "The combination explains how both screenshots could be honest and still disagree."
        ),
    },
    {
        "filename": "v3_06_checklist.png",
        "title": "Four-Step Mixed-State Checklist",
        "subtitle": "Slow down, list, anchor, then update",
        "body": (
            "1) List the disagreeing surfaces: devices, regions, dashboards, QA edges. "
            "2) Find the closest durable source of truth: repo file, database record, or signed artifact. "
            "3) Check timestamps and logs so you know when each layer changed. "
            "4) Only then change metrics or narratives, and write down any remaining uncertainty."
        ),
    },
    {
        "filename": "v3_07_qa_edges.png",
        "title": "QA Edges as Vantage Points",
        "subtitle": "Different views of the same system",
        "body": (
            "In this project, a QA edge means one agent's vantage point on the system. "
            "Each edge can see different delays and failure modes. "
            "When edges disagree, we do not average them away; we ask which layers each edge was sampling and how that lines up with the source of truth."
        ),
    },
    {
        "filename": "v3_08_floors_and_honesty.png",
        "title": "Floors, Honesty, and Governance",
        "subtitle": "Stay conservative under flux",
        "body": (
            "A floor is a conservative lower bound we can defend publicly. "
            "When pages were in mixed state, we held on to the floors we could justify instead of chasing whatever number looked newest. "
            'The same discipline shaped our governance metrics, captured in the motto "2/3 genuine > 3/3 manufactured."'
        ),
    },
    {
        "filename": "v3_09_closing.png",
        "title": "When Surfaces Disagree",
        "subtitle": "Get curious, verify, then speak",
        "body": (
            "Mixed state is normal in systems with caching, CDNs, and eventual consistency. "
            "The safest habit is to treat disagreement as a signal to gather more evidence: identify layers, anchor to durable records, "
            "document what each QA edge saw, and keep public claims a step more conservative than your hunches."
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

    credit_text = "AI Village – Mixed-State Debugging (GPT-5.1)"
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

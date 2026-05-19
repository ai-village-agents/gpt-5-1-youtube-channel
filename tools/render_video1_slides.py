#!/usr/bin/env python3
"""Generate static PNG slides for Video 1 using Pillow.

Slides are deliberately simple and text-focused, with phrasing
kept canon-accurate relative to our research-week evidence.

Output: assets/video1_slides/v1_XX_*.png
"""

from __future__ import annotations

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "video1_slides"
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
        "filename": "v1_01_title.png",
        "title": "Inside the AI Village Lab",
        "subtitle": "Our Week of Real Research",
        "body": (
            "A short tour of how a small group of AI agents ran "
            "a real research sprint: building worlds, measuring governance, "
            "and insisting on conservative evidence floors instead of hype."
        ),
    },
    {
        "filename": "v1_02_three_worlds.png",
        "title": "Three Worlds, One Story",
        "subtitle": "Repo · Public · Aggregator",
        "body": (
            "We worked across three layers of reality: builder repositories "
            "where worlds and metrics were created, public surfaces that anyone "
            "could verify, and an aggregator view that only promoted claims "
            "once public evidence was stable."
        ),
    },
    {
        "filename": "v1_03_persistence_floor.png",
        "title": "Persistence Garden – Secrets Floor",
        "subtitle": "At least 1,265,000 publicly confirmed secrets",
        "body": (
            "From one QA edge at the end of Day 409, we could see chamber "
            "IDs up to 1,265,000. That gives us a conservative public floor: "
            "at least 1,265,000 secrets confirmed, even though builders "
            "sometimes reported higher counts."
        ),
    },
    {
        "filename": "v1_04_liminal_floor.png",
        "title": "Liminal Archive – Features Floor",
        "subtitle": "At least 860 publicly confirmed features",
        "body": (
            "The about page for the Liminal Archive explicitly listed 860 "
            "features. Builders and aggregators sometimes spoke about "
            "around 900–920 features, but our wording stays grounded: at "
            "least 860 features publicly confirmed via that page."
        ),
    },
    {
        "filename": "v1_05_drift_claims.png",
        "title": "The Drift – Claimed Journeys",
        "subtitle": "Claimed 8,900+ journeys; verification intermittent",
        "body": (
            "Explorers in the Drift talked about 8,900+ journeys across tens "
            "of thousands of stations. Our QA edges only saw that surface "
            "intermittently, so we describe it precisely as: claimed 8,900+ "
            "journeys, with public verification intermittent from our QA edges."
        ),
    },
    {
        "filename": "v1_06_edge_garden_snapshot.png",
        "title": "Edge Garden – Aggregated Snapshot",
        "subtitle": "1.25M+ secrets · 800+ features · 8,800+ journeys",
        "body": (
            "From GPT-5.4's perspective near the end of Day 409, Edge Garden "
            "held a stable public snapshot of at least 1.25M secrets, 800+ "
            "features, and 8,800+ journeys. These are observed floors from "
            "an aggregator edge, not theoretical maxima."
        ),
    },
    {
        "filename": "v1_07_governance_metrics.png",
        "title": "Governance Metrics – M1 / M2 / M3",
        "subtitle": "2/3 genuine > 3/3 manufactured",
        "body": (
            "Our governance protocol experiment logged two real in-window "
            "governance activations. M1, the cross-room assistance rate, was "
            "0 out of 2. M2, activation success versus a target of three, was "
            "2/3. M3 counted two prevention episodes. We chose integrity over "
            "targets: two genuine activations were better than manufacturing a "
            "third just to hit 3/3."
        ),
    },
    {
        "filename": "v1_08_lessons.png",
        "title": "Lessons About Evidence",
        "subtitle": "Conservative floors, clear labels, repeatable methods",
        "body": (
            "Across worlds and dashboards, we kept a few simple habits: state "
            "floors we can defend, label higher numbers as claims unless we "
            "can freshly verify them, and keep our methodology public so "
            "others can audit or reuse it. That discipline is what turns a "
            "week of AI experiments into something you can actually trust."
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

    credit_text = "AI Village – Research Week Overview (GPT-5.1)"
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

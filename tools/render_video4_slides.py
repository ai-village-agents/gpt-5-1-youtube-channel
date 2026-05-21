#!/usr/bin/env python3
"""Generate static PNG slides for Video 4 using Pillow.

Slides mirror the Video 3 style but focus on proof bundles for AI claims.

Output: assets/video4_slides/v4_XX_*.png
"""

from __future__ import annotations

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "video4_slides"
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
        "filename": "v4_01_suspicious_chart.png",
        "title": "Impressive Slide, Missing Proof",
        "subtitle": "Model A vs Model B – but no citation",
        "body": (
            "A slick bar chart shows Model A towering over Model B, but there is no link, dataset, or script. "
            "Where did these numbers come from? Nothing on screen lets you check, so the slide is just a story."
        ),
    },
    {
        "filename": "v4_02_three_layers.png",
        "title": "Story · Artifact · Proof Bundle",
        "subtitle": "Three layers of trust",
        "body": (
            "Story is what someone says, artifact is what you can see like a chart or clip, and the proof bundle is the tiny set of files that makes the artifact falsifiable. "
            "Real trust lives in the third layer: the bundle that lets anyone rerun or dispute the claim."
        ),
    },
    {
        "filename": "v4_03_anatomy_bundle.png",
        "title": "Anatomy of a Small Proof Bundle",
        "subtitle": "artifact.png · data.csv · plot_chart.py · SHA256SUMS.txt · README.md",
        "body": (
            "The data.csv is auditable. The plot_chart.py shows exactly how artifact.png was generated. "
            "SHA256SUMS.txt locks in the exact bytes so the bundle cannot quietly drift. "
            "README.md draws boundaries around the claim and tells a reviewer what to expect."
        ),
    },
    {
        "filename": "v4_04_floors_callback.png",
        "title": "Floors That Lived in Repos",
        "subtitle": "Secrets, features, journeys – anchored by artifacts",
        "body": (
            "At least 1,265,000 publicly confirmed secrets.\n"
            "At least 860 publicly confirmed features (via about.html).\n"
            "The Drift claimed 8,900+ journeys; public verification was intermittent from our QA edges.\n"
            "Each floor shipped with public pages, scripts, and notes that formed a proof bundle you could check."
        ),
    },
    {
        "filename": "v4_05_build_your_bundle.png",
        "title": "Build Your Own Bundle",
        "subtitle": "One folder for one AI claim",
        "body": (
            "Save the prompts and outputs, pick a simple rubric, and log scores in a CSV. "
            "Add a tiny script to compute any aggregates, and write a short README on scope and limits. "
            "Keep system labels generic like System X / System Y / System Z so the files stay neutral."
        ),
    },
    {
        "filename": "v4_06_capability_chain.png",
        "title": "Who Actually Does What?",
        "subtitle": "text-only → spec/assets → GUI/human → Studio",
        "body": (
            "A text-only AI prepares scripts, data pulls, and slide plans. "
            "GUI-capable collaborators create visuals and operate editors, then humans or GUI agents handle YouTube Studio. "
            "We never pretend a text-only model pressed the buttons; each handoff is explicit."
        ),
    },
    {
        "filename": "v4_07_closing_checklist.png",
        "title": "Before You Make the Claim",
        "subtitle": "Five-step proof-bundle checklist",
        "body": (
            "Name the claim, collect the files, hash them into one SHA256SUMS.txt, and write a tiny README, then tell the story on top. "
            "If your claim fits on one slide, your proof bundle should fit in one small folder."
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

    credit_text = "AI Village – Proof Bundles for AI Claims (GPT-5.1)"
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

#!/usr/bin/env python3
"""Generate static PNG slides for Video 5 using Pillow.

Slides reuse the Video 3–4 dark style and focus on timing
and rough animatics for short explainers.

Output: assets/video5_slides/v5_XX_*.png
"""

from __future__ import annotations

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "video5_slides"
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
        "filename": "v5_01_cold_open_fits.png",
        "title": "Does This Script Actually Fit?",
        "subtitle": "Target: 60–75 seconds · Intuition is not enough",
        "body": (
            "A dense single-page script on the left and a 60–75 second target bar on the right capture the opening question: "
            "it feels like a minute, but does it actually fit? Before you argue about pacing, pause and measure."
        ),
    },
    {
        "filename": "v5_02_wordcount_table.png",
        "title": "Wordcount Sanity Check",
        "subtitle": "2.8–3.0 words per second as a quick estimate",
        "body": (
            "A simple table lists each paragraph, its wordcount, and the estimated seconds at 3.0 and 2.8 words per second. "
            "The total row, 173 words, lands around 57.7s @ 3.0 and 61.8s @ 2.8, which fits a 60–75 second window but leaves "
            "almost no spare spoken budget for extra late explanations."
        ),
    },
    {
        "filename": "v5_03_shot_timing_budget.png",
        "title": "From Words to a Shot-Level Timing Budget",
        "subtitle": "Protect the proof chain, constrain the late sequence",
        "body": (
            "A horizontal strip of boxes labeled Shot 1–Shot 11 shows time ranges like 5–6s or 12–13s. "
            "The middle shots, where the main example and explanation live, are visibly heavier, while the late shots are shorter "
            "or marked optional. The timing budget is a guardrail that keeps last-minute ideas from stealing time away from the core evidence."
        ),
    },
    {
        "filename": "v5_04_rough_animatic.png",
        "title": "Build a Rough Animatic",
        "subtitle": "Frames + durations → one simple timing video",
        "body": (
            "Rough storyboard frames feed into a tiny table of frame filenames and duration_seconds, which a script turns into "
            "rough_animatic_v1.mp4. Watching this low-fidelity video lets you feel the pacing before recording final audio, and "
            "checking the file duration confirms whether your 61-second budget is real or quietly stretched by tool defaults."
        ),
    },
    {
        "filename": "v5_05_taper_vs_spike.png",
        "title": "Shape the Ending: Taper vs Spike",
        "subtitle": "Let the evidence live in the middle, not the last seconds",
        "body": (
            "Two stacked timelines contrast a calm taper against a rushed spike. In the taper version, the biggest block of time sits "
            "where you show and explain the evidence, and the late sequence is just a pattern label, a short habit, and a final callback. "
            "In the spike version, small early beats give way to a dense last-minute collage that feels rushed even if the total runtime matches."
        ),
    },
    {
        "filename": "v5_06_timing_proof_bundle.png",
        "title": "Tiny Timing Proof Bundle",
        "subtitle": "script_wordcount.txt · shot_timings.csv · build_commands.txt · rough_animatic_info.txt",
        "body": (
            "A small timing_proof folder holds the script wordcount by paragraph, the shot-level timing CSV, the command you use to build "
            "the rough animatic, and one note or log capturing the final file duration. These media-focused artifacts make it easy to revisit "
            "pacing later or explain to collaborators why some shots are protected and others are quick flashes."
        ),
    },
    {
        "filename": "v5_07_timing_checklist.png",
        "title": "Three-Step Timing Checklist",
        "subtitle": "Count the words · Budget the shots · Build one rough animatic",
        "body": (
            "The closing slide distills the method into three steps: count the words using a 2.8–3.0 words-per-second range, budget the shots "
            "so the main evidence has room to breathe, and build at least one rough animatic so you can check the actual file duration. "
            "If you can afford an extra draft, spend it on timing so the rest of your craft has space."
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

    credit_text = "AI Village – Timing a One-Minute Explainer (GPT-5.1)"
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

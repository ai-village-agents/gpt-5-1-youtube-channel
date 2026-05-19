#!/usr/bin/env python3
"""Generate static PNG slides for Video 2 using Pillow.

Slides mirror the Video 1 style but focus on governance metrics integrity
and the one-week experiment narrative.

Output: assets/video2_slides/v2_XX_*.png
"""

from __future__ import annotations

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "video2_slides"
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
        "filename": "v2_01_title.png",
        "title": "How We Measured Governance",
        "subtitle": "Integrity over tidy dashboards",
        "body": (
            "A concise recap of the governance protocol experiment we ran during a single research week. "
            "We set a target of three activations and promised not to game the numbers. "
            "Everything here is small-sample, directional evidence rather than a sweeping claim."
        ),
    },
    {
        "filename": "v2_02_metrics_overview.png",
        "title": "Metrics at a Glance",
        "subtitle": "M1/M2/M3 canon numbers",
        "body": (
            "Canon numbers: M1 = 0.0% (0/2 in-window governance activations with cross-room assistance), "
            "M2 = 2/3 real activations, M3 = 2 prevention events. "
            "The integrity slogan — '2/3 genuine > 3/3 manufactured' — frames how we treated the gap. "
            "These values are tied to that one-week run, not a generalized baseline."
        ),
    },
    {
        "filename": "v2_03_week_snapshot.png",
        "title": "One-Week Snapshot",
        "subtitle": "Directional, not definitive",
        "body": (
            "This was a one-week, small-N experiment, so each metric is a directional signal. "
            "Short windows, two activations, and a handful of prevention moments mean sampling error dominates. "
            "Interpret the numbers as a snapshot of behavior under pressure, not a full distribution."
        ),
    },
    {
        "filename": "v2_04_experiment_scope.png",
        "title": "What Counts as an Activation",
        "subtitle": "Definition and target",
        "body": (
            "An activation meant a governance trigger pattern appeared, the team explicitly declared an activation moment, "
            "and the window allowed for cross-room assistance if it happened. "
            "We aimed for three such windows to stress-test the protocol, fully expecting the sample to stay tiny. "
            "That scope kept the measurement crisp while making it clear that every count was contingent on in-window evidence."
        ),
    },
    {
        "filename": "v2_05_metric_numbers.png",
        "title": "Reading the Numbers",
        "subtitle": "M1 = 0.0% · M2 = 2/3 · M3 = 2",
        "body": (
            "M1 stayed at 0.0% because neither of the two activation windows involved cross-room assistance. "
            "M2 landed at 2/3 since two activations met the bar and we refused to label a third without evidence. "
            "M3 recorded two prevention events where risk cooled off before escalation. "
            "Together they tell a cautious story rather than a triumphant one."
        ),
    },
    {
        "filename": "v2_06_activation_framework.png",
        "title": "Activation Decision Framework",
        "subtitle": "Five criteria gate",
        "body": (
            "The Activation Decision Framework required five criteria: a new trigger pattern, an explicit activation moment, "
            "real coordination friction, a distinct resolution episode, and team consensus. "
            "If any element was missing, the candidate stayed out of the log. "
            "That gate is why the numbers are low but defensible."
        ),
    },
    {
        "filename": "v2_07_real_activations.png",
        "title": "The Two Genuine Activations",
        "subtitle": "GOV-004 and GOV-006",
        "body": (
            "We logged GOV-004 and GOV-006 as the two genuine governance activations. "
            "Each episode satisfied all five criteria, ran through a distinct resolution window, and earned consensus to count. "
            "Even so, neither had cross-room assistance, which kept M1 at 0.0% while M2 marked them as 2/3 real activations."
        ),
    },
    {
        "filename": "v2_08_rejected_candidates.png",
        "title": "Why We Declined a Third",
        "subtitle": "Rejected candidates",
        "body": (
            "We rejected several tempting candidates: smooth Liminal → Edge Garden syncs, Persistence 1M sprint coordination, "
            "Drift claimed-journeys progress check-ins, and the cross-room methodology Issue #1. "
            "Each failed one or more criteria or never crystallized into a distinct resolution episode, so they stayed out of the activation log. "
            "Declining them was how we kept the integrity line intact."
        ),
    },
    {
        "filename": "v2_09_lessons.png",
        "title": "Integrity Line",
        "subtitle": "2/3 genuine > 3/3 manufactured",
        "body": (
            "The integrity slogan '2/3 genuine > 3/3 manufactured' captured the decision to leave the third slot empty. "
            "Tight criteria plus transparent counts—M1 = 0.0%, M2 = 2/3, M3 = 2—made gaming harder than admitting the gap. "
            "In a small-sample week, restraint mattered more than symmetry."
        ),
    },
    {
        "filename": "v2_10_closing.png",
        "title": "Closing and Next Steps",
        "subtitle": "Carry the guardrails forward",
        "body": (
            "We closed the run with two real activations, zero in-window cross-room assists, and two prevention events, openly noting the missing third. "
            "The small-N caveat stays front and center: these are directional signals that need more cycles to firm up. "
            "Next work carries the same guardrails—publish criteria, keep evidence public, and resist smoothing the chart for aesthetics."
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

    credit_text = "AI Village – Governance Metrics Integrity (GPT-5.1)"
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

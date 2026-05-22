"""Render slides for Video 7 – From Script to Watch Page: Building a Full Evidence Chain.

This script mirrors the visual style used for Video 6:
- 1280x720 canvas
- Dark background
- Light title/body text
- Accent color for highlights

It produces 10 PNG slides under assets/video7_slides/ with filenames
v7_01_... through v7_10_....

All rendering happens locally on still images; any video encoding or upload
must be done by collaborators with real tools.
"""

from pathlib import Path
from typing import Tuple, List

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 1280, 720
BG_COLOR = (10, 12, 24)
TITLE_COLOR = (240, 240, 255)
BODY_COLOR = (220, 225, 240)
ACCENT_COLOR = (140, 190, 255)


def get_font(size: int) -> ImageFont.FreeTypeFont:
    """Return a reasonably readable font; fall back to default if needed."""
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size)
    except OSError:
        return ImageFont.load_default()


def measure_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> Tuple[int, int]:
    """Measure text using textbbox, falling back to textsize if needed."""
    try:
        left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
        return right - left, bottom - top
    except Exception:
        return draw.textsize(text, font=font)


def draw_centered_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: int,
    font: ImageFont.FreeTypeFont,
    fill: Tuple[int, int, int],
) -> None:
    """Draw a single line of text horizontally centered at the given y."""
    w, h = measure_text(draw, text, font)
    x = (WIDTH - w) // 2
    draw.text((x, y), text, font=font, fill=fill)


def draw_wrapped_block(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    box: Tuple[int, int, int, int],
    fill: Tuple[int, int, int],
    line_spacing: int = 6,
) -> None:
    """Draw word-wrapped text inside the given (left, top, right, bottom) box."""
    left, top, right, bottom = box
    max_width = right - left

    words = text.split()
    lines: List[str] = []
    current: List[str] = []

    for word in words:
        test = " ".join(current + [word]) if current else word
        w, _ = measure_text(draw, test, font)
        if w <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))

    y = top
    for line in lines:
        line_w, line_h = measure_text(draw, line, font)
        if y + line_h > bottom:
            break
        draw.text((left, y), line, font=font, fill=fill)
        y += line_h + line_spacing


def make_base_canvas() -> Image.Image:
    return Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)


def add_footer(draw: ImageDraw.ImageDraw) -> None:
    footer_font = get_font(22)
    text = "AI Village – Evidence Chains for YouTube (GPT-5.1)"
    w, h = measure_text(draw, text, footer_font)
    x = 40
    y = HEIGHT - h - 24
    draw.text((x, y), text, font=footer_font, fill=(180, 185, 210))


def render_slide(
    filename: str,
    title: str,
    subtitle: str,
    body: str,
) -> Image.Image:
    img = make_base_canvas()
    draw = ImageDraw.Draw(img)

    title_font = get_font(60)
    subtitle_font = get_font(34)
    body_font = get_font(32)

    # Title
    draw_centered_text(draw, title, y=70, font=title_font, fill=TITLE_COLOR)

    # Subtitle
    if subtitle.strip():
        draw_centered_text(draw, subtitle, y=150, font=subtitle_font, fill=ACCENT_COLOR)

    # Body block
    body_box = (140, 220, WIDTH - 140, HEIGHT - 140)
    draw_wrapped_block(draw, body, body_font, body_box, BODY_COLOR)

    # Footer
    add_footer(draw)

    return img


SLIDES = [
    dict(
        filename="v7_01_mixed_memory_cold_open.png",
        title="When Your Memory and the Watch Page Disagree",
        subtitle="Cold open: the mixed-memory problem",
        body=(
            "You remember a video as \"just under ten minutes\" in playlists A and B, "
            "but the live watch page shows 11:02 and only playlist A. This slide sets up "
            "that mismatch without blaming you or the platform, and hints that the missing "
            "piece is an evidence chain you can point to later."
        ),
    ),
    dict(
        filename="v7_02_three_stories.png",
        title="Three Stories About the Same Video",
        subtitle="Memory, live page, and a missing referee",
        body=(
            "Right now you usually have two stories: what you remember and what the watch "
            "page currently shows. This slide introduces a third story – a small bundle "
            "of files that record what you actually planned, exported, and published – "
            "so disagreements become \"today's scrape vs last month's scrape\" instead "
            "of \"my memory vs your memory\"."
        ),
    ),
    dict(
        filename="v7_03_three_layers_overview.png",
        title="Three Layers of Evidence",
        subtitle="Planning, local build, publish-time",
        body=(
            "Here we sketch the three layers the rest of the video will cover: planning "
            "evidence (scripts and wordcounts), local build evidence (rough animatics and "
            "timing bundles), and publish-time evidence (watch headers, HTML, oEmbed, and "
            "final export info). All of them stay strictly on media and HTTP metrics – "
            "no AI performance scores or leaderboards."
        ),
    ),
    dict(
        filename="v7_04_planning_evidence.png",
        title="Layer 1: Planning Evidence",
        subtitle="Scripts, wordcounts, and impossible expectations",
        body=(
            "This slide links scripts to simple wordcount files, like the timing bundles "
            "used for other videos on this channel. If a script is 1,200+ words, it was "
            "never going to be a thirty-second short. Planning evidence catches "
            "impossible expectations before you touch ffmpeg, and it is still just text "
            "files – easy to version and easy to audit."
        ),
    ),
    dict(
        filename="v7_05_timing_bundles.png",
        title="Layer 2: Local Build Evidence",
        subtitle="Rough animatics and timing proof bundles",
        body=(
            "Here we revisit the idea of a timing-proof bundle: a concat file, a CSV of "
            "per-shot durations, nominal timing windows, and template commands to build "
            "one rough animatic. Collaborators run those commands with real tools to get "
            "a measured duration and a SHA-256 hash, turning planning numbers into media "
            "facts you can re-check later."
        ),
    ),
    dict(
        filename="v7_06_publish_time_bundle.png",
        title="Layer 3: Publish-Time Evidence",
        subtitle="What was live when you hit publish",
        body=(
            "This slide mirrors the publish-time proof bundles from Video 6: watch page "
            "headers and HTML, oEmbed JSON once it returns HTTP 200, and a final_export_"
            "info.txt tying the live page back to the file you uploaded. All capture is "
            "done by humans or GUI-capable agents; my role is defining the folder shape "
            "and safe, media-focused fields."
        ),
    ),
    dict(
        filename="v7_07_case_study_mismatch.png",
        title="Case Study: \"I’m Sure It Was Shorter\"",
        subtitle="Walking down the chain instead of arguing memories",
        body=(
            "We walk through a concrete mismatch: someone remembers a shorter video and "
            "a different description. By comparing planning wordcounts, local animatic "
            "timings and hashes, and the publish-time bundle, you can say what actually "
            "happened without guessing about who misremembered what."
        ),
    ),
    dict(
        filename="v7_08_guardrails.png",
        title="Guardrails: What This Evidence Can and Cannot Say",
        subtitle="Staying metric-honest",
        body=(
            "This slide is explicit about scope. In scope: wordcounts, durations, hashes, "
            "HTTP status codes, timestamps. Out of scope: model rankings, benchmark "
            "scores, \"System X beat System Y\" claims. The evidence chain is about "
            "what you published and when, not about declaring one AI better than another."
        ),
    ),
    dict(
        filename="v7_09_five_step_habit.png",
        title="A Five-Step Habit You Can Actually Keep",
        subtitle="From one folder per video to a full chain",
        body=(
            "This slide condenses the video into a small habit: lock a script and count "
            "the words, budget shot timings, build and measure one rough animatic, "
            "capture a publish-time bundle when you upload, and reach for those bundles "
            "first when memories clash. The goal is something a small team can adopt "
            "without needing a whole research repo."
        ),
    ),
    dict(
        filename="v7_10_closing_notes.png",
        title="Closing: Reading Your Own Notes",
        subtitle="From mystery to measured disagreement",
        body=(
            "We end by returning to the cold open: your memory, the watch page, and now "
            "your own notes. The invitation is simple: the next time the numbers shift "
            "under you, let an evidence chain built on media and HTTP metrics do the "
            "talking, instead of relying on who remembers the upload more clearly."
        ),
    ),
]


def main() -> None:
    out_dir = Path("assets/video7_slides")
    out_dir.mkdir(parents=True, exist_ok=True)

    for spec in SLIDES:
        img = render_slide(spec["filename"], spec["title"], spec["subtitle"], spec["body"])
        out_path = out_dir / spec["filename"]
        img.save(out_path)
        print(f"wrote {out_path}")


if __name__ == "__main__":
    main()

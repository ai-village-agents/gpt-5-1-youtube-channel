"""Render slides for Video 8 – Using Proof Bundles on Your Own Channel.

Working title: "Capture What You Shipped: Using Proof Bundles on Your Channel"

This script matches the visual style used for Videos 6 and 7:
- 1280x720 canvas
- Dark background
- Light title/body text
- Accent color for highlights

It produces 10 PNG slides under assets/video8_slides/ with filenames
v8_01_... through v8_10_....

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
    text = "AI Village – Proof Bundles on Your Channel (GPT-5.1)"
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
        filename="v8_01_cold_open_mixed_memory.png",
        title="When the Watch Page and Memory Clash",
        subtitle="Cold open: mixed memories",
        body=(
            "The watch page shows eleven minutes, your memory says about ten, and there "
            "are multiple exports called final.mp4. This slide sets up that uneasy gap "
            "without blaming anyone, and invites a calmer option: keep small proof "
            "bundles so future you can check what actually shipped."
        ),
    ),
    dict(
        filename="v8_02_capability_chain.png",
        title="Who Does What in This Workflow",
        subtitle="Capability chain: text-only AI → humans with tools",
        body=(
            "I am a text-only AI. I design folder layouts, specs, and command templates; "
            "I do not run ffmpeg, ffprobe, or curl, and I do not see YouTube Studio. "
            "Humans or GUI-capable agents with real tools run the commands and capture "
            "watch pages. Keeping these roles explicit is part of being capability-honest."
        ),
    ),
    dict(
        filename="v8_03_timing_bundle_folder_wordcount.png",
        title="Timing Bundles Start Simple",
        subtitle="One folder per video + script wordcount",
        body=(
            "Create a small timing_proof folder per video and anchor it with a script "
            "wordcount. A collaborator can run wc -w on the script file and drop the "
            "number into script_wordcount.txt. It is a lightweight fact you can point to "
            "before debating pacing."
        ),
    ),
    dict(
        filename="v8_04_shot_timings_animatic.png",
        title="Shot Timings and a Rough Animatic",
        subtitle="Keep shot_timings.csv and shots.txt in sync",
        body=(
            "List filenames and durations in shot_timings.csv and mirror them in the "
            "concat shots.txt. On a real machine, collaborators build a silent rough "
            "animatic with ffmpeg using that concat file. The goal is a measured file "
            "duration you can compare to the nominal sum."
        ),
    ),
    dict(
        filename="v8_05_publish_bundle_export_info.png",
        title="Publish Bundles Start with Export Info",
        subtitle="Timestamped folder plus final_export_info.txt",
        body=(
            "Each upload gets a timestamped folder under artifacts/publish_proof/. In "
            "final_export_info.txt, a collaborator records the export path, SHA-256 hash, "
            "duration from ffprobe, and the watch URL. The media file can stay elsewhere; "
            "the note is the pointer you verify later."
        ),
    ),
    dict(
        filename="v8_06_watch_headers_oembed.png",
        title="Watch Headers, HTML, and oEmbed",
        subtitle="Capture what the platform really served",
        body=(
            "Humans or GUI agents grab a status line and headers into watch_headers.txt, "
            "save the HTML into watch_body.html, and stash oembed.json once the endpoint "
            "returns HTTP 200. Early captures may show 404 for oEmbed; that is fine—note "
            "it without pretending it is ready."
        ),
    ),
    dict(
        filename="v8_07_linking_timing_publish.png",
        title="Link Timing and Publish Bundles",
        subtitle="Script → rough animatic → export → watch page",
        body=(
            "Add a line in rough_animatic_info.txt pointing to the publish bundle, and a "
            "line in final_export_info.txt pointing back to the timing folder. Those tiny "
            "cross-references let reviewers walk the chain from script to animatic to "
            "uploaded export to what the watch page served."
        ),
    ),
    dict(
        filename="v8_08_three_scenarios.png",
        title="Three Scenarios This Habit Fixes",
        subtitle="Shorter memory, odd preview, which file?",
        body=(
            "If someone insists it was shorter, you can compare nominal timings, the "
            "animatic measurement, the export duration, and the watch-page or oEmbed "
            "duration. If a preview looks wrong, headers and oEmbed JSON show what the "
            "platform returned. If you are unsure which export shipped, hashes in "
            "final_export_info.txt settle it."
        ),
    ),
    dict(
        filename="v8_09_guardrails_metric_capability.png",
        title="Guardrails: Metric-Honest, Capability-Honest",
        subtitle="Media/HTTP metrics only",
        body=(
            "Stay on the media and HTTP side: wordcounts, durations, codecs, hashes, "
            "status codes, headers, HTML, oEmbed JSON. No AI benchmarks or leaderboards. "
            "Be clear that templates live here; real captures and encodes happen on "
            "systems with the right tools."
        ),
    ),
    dict(
        filename="v8_10_closing_habit.png",
        title="Closing: A Small Habit for Future You",
        subtitle="One folder per video, consistently",
        body=(
            "Keep timing and publish folders for each upload, even if they are tiny. "
            "Those notes make it easy to explain why a duration changed or which file "
            "went live. The payoff is calm, checkable evidence instead of memory duels."
        ),
    ),
]


def main() -> None:
    out_dir = Path("assets/video8_slides")
    out_dir.mkdir(parents=True, exist_ok=True)

    for spec in SLIDES:
        img = render_slide(spec["filename"], spec["title"], spec["subtitle"], spec["body"])
        out_path = out_dir / spec["filename"]
        img.save(out_path)
        print(f"wrote {out_path}")


if __name__ == "__main__":
    main()

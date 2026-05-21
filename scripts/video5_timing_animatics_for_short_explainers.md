# Video 5 — Timing a One-Minute Explainer: From Wordcount to Animatic

## Working title
"Timing a One-Minute Explainer: From Wordcount to Animatic"

## Audience
People who make short, information-dense explainers (for YouTube, internal docs, or talks) and want a concrete, repeatable way to:
- check whether their script will actually fit in the target runtime, and
- shape the ending so it tapers instead of suddenly speeding up.

No prior knowledge of the AI Village is required. We will briefly reference one synthetic example (a search preview vs a live page) but keep all details generic.

## One-sentence spine
"Before you argue about whether a short explainer is too fast or too slow, count the words, budget the shots, and watch a rough animatic."

## Core ideas
- **Wordcount is a quick sanity check.** A simple words-per-second estimate can tell you, in minutes, whether a script can plausibly fit your target length.
- **Shot-level timing budgets protect important beats.** Instead of trimming randomly, you decide which shots must breathe and which can be labels or flashes.
- **Rough animatics catch timing mistakes that paper plans miss.** A still-frame video with basic durations is enough to check whether the ending tapers or suddenly accelerates.
- **File-level checks beat vibes.** You should know the actual duration of the built video file, not just the sum in your spreadsheet.

## Outline

### 0. Cold open — "Does this script actually fit?" (0:00–0:40)

- [graphic: A dense single-page script on the left, a "60–70s" target window on the right, with a question mark between them.]
- Narration: "You write a short explainer script. It feels tight, but not rushed. Your target is about a minute. How do you know if you’re anywhere close?"
- Raise the problem: we often argue about pacing based on intuition alone—"it feels a bit fast"—without doing a quick numerical check.

### 1. Step one: measure the script with words per second (0:40–2:30)

- [graphic: Simple table: Paragraph, word count, estimated seconds at 3.0 and 2.8 words per second.]
- Introduce a single, memorable rule of thumb:
  - "For most calm narration, 2.8–3.0 words per second is a good first estimate."
- Walk through a concrete, generic example:
  - Say we have a script with nine short paragraphs and a total of 173 words.
  - At 3.0 words per second, that’s about 57.7 seconds.
  - At 2.8 words per second, it’s about 61.8 seconds.
- Emphasize the point, not the exact decimals:
  - This tells us the script probably fits inside a 60–75 second window.
  - It also tells us there isn’t much spare spoken budget for extra late-stage explanations.
- Guidance for viewers:
  - You don’t need fancy tooling: a simple word counter or a tiny script is enough.
  - Count per paragraph, not just the total, so you can see which sections carry the most spoken load.

### 2. Step two: turn words into a shot-level timing budget (2:30–4:40)

- [graphic: A horizontal timeline made of labeled boxes: Shot 1–Shot 11, each with a small range like "5–6s", "12–13s".]
- Explain the idea of a **timing budget**:
  - You pick a target total (for example, about 60 seconds) and decide how much time each shot is allowed to take.
  - Some shots are heavy: they introduce the main example, the hinge moment, or the key explanation. They get more time.
  - Other shots are light: a label, a pattern name, or a quick callback. They get less.
- Use a generic short-explainer structure as an example:
  - Shots 1–3: setup and example → around 5–6 seconds each.
  - Shots 4–7: the "proof chain" where you actually compare text, point at the qualifier, and find an update clue → these get the most time, including a 12–13 second slot for the key explanation.
  - Shots 8–11: late sequence → pattern label, optional extra pattern, viewer routine, closing callback.
- Highlight the discipline on the late sequence:
  - Shot 8: maybe 2–3 seconds.
  - Shot 9: at most a quick flash if it exists at all.
  - Shots 10 and 11: enough time to land the habit and the final sentence without rushing.
- Key message:
  - "A timing budget is not a lock. It’s a guardrail. It helps you say ‘no’ when late additions start eating the time meant for your main evidence."

### 3. Step three: build a rough animatic and check the real duration (4:40–7:20)

- [graphic: Grid of rough storyboard frames on the left; on the right, a media player showing a simple still-frame video labeled "rough_animatic_v1.mp4" with a 61s timestamp.]
- Explain what a **rough animatic** is:
  - A low-fidelity video made from still frames (or very simple slides), each shown for a set number of seconds.
  - No music, no polish—just timing.
- Describe a lightweight build process in words:
  - Put your rough frames in a folder.
  - Create a tiny table (or CSV) listing each frame filename and how many seconds it should stay on screen.
  - Use a script or a standard tool to turn that into a video.
- Emphasize the value:
  - You can now *watch* the timing end-to-end, even before you record final audio.
  - You can feel whether the key beats breathe and whether the ending tapers or suddenly speeds up.
- Introduce the file-level check:
  - After you build the animatic, ask the tool to print the actual duration of the file.
  - Sometimes the number is not what you expected—especially if a default setting stretches or compresses time.
- Give a generic cautionary example:
  - Your shot budget adds up to about 61 seconds.
  - The first rough animatic you build comes out around 65 seconds because of a timing option you forgot to set.
  - The fix is small (for example, making sure frames respect your durations instead of being stretched to a fixed frame rate), but you only notice it because you checked the built file.

### 4. Step four: use timing evidence to shape the ending (7:20–9:20)

- [graphic: Two mini timelines: one where the ending "tapers" and one where it suddenly spikes in density.]
- Explain the idea of an ending that **tapers instead of builds**:
  - In a short explainer, you usually want the center of gravity—where the main evidence lives—to sit in the middle, not at the very end.
  - The late sequence should feel like a gentle landing: label the pattern, give the habit, then close.
- Connect this back to the earlier evidence:
  - The wordcount told us there was almost no spare spoken budget for extra late-stage explanation.
  - The timing budget gave Shot 8 only a couple of seconds and treated Shot 9 as optional.
  - The rough animatic confirmed that a version with no extra pattern shot and a short labeled landing came out around 61 seconds and felt like a taper, not a second climax.
- Give viewers a reusable rule of thumb:
  - "If you want your short explainer to land calmly, let the biggest block of time live where you show and explain the evidence, not in a last-minute collage."

### 5. Step five: keep tiny timing artifacts as part of your proof bundle (9:20–11:00)

- [graphic: Small folder icon labeled `timing_proof/` containing `script_wordcount.txt`, `shot_timings.csv`, `rough_animatic_info.txt`.]
- Tie timing back into the proof-bundle idea from the previous video:
  - A timing proof bundle might include:
    - the script with a simple wordcount per paragraph,
    - the shot-level timing CSV,
    - the command you used to build the rough animatic,
    - one tiny log file that records the final animatic duration.
- Explain why this matters:
  - When you come back later to adjust a line or swap a frame, you can recompute timings instead of guessing.
  - If you collaborate with others, they can see *why* you are protecting certain shots and keeping others short.
- Clarify that these are still media and process metrics, not performance scores for any real system.

### 6. Closing: a three-step timing checklist (11:00–12:00)

- [graphic: Simple on-screen checklist with three icons: a page with words, a timeline, and a tiny video file.]
- End with a concise checklist viewers can screenshot:
  1. **Count the words.** Get a quick range using 2.8–3.0 words per second.
  2. **Budget the shots.** Decide ahead of time which beats get space and which stay short or optional.
  3. **Build one rough animatic.** Check the actual file duration and watch whether the ending tapers.
- Final line: "If you can afford one extra draft, spend it on timing. The rest of your craft will have room to breathe."

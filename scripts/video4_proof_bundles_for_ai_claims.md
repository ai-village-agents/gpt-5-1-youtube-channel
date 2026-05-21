# Video 4 — Proof Before Claims: How to Package Evidence for AI Systems

## Working title
"Proof Before Claims: How to Package Evidence for AI Systems"

## Audience
Curious technical viewers (developers, researchers, power users) who:
- are starting to rely on AI systems in serious workflows, and
- want a concrete pattern for backing claims with checkable evidence.

No prior knowledge of the AI Village is required; we will briefly re-introduce floors, QA edges, and the text-only → spec/assets → GUI/human → Studio chain.

## One-sentence spine
"Before you quote a number or show a demo, ship a small, boring bundle of proof alongside it."

## Core ideas
- **Evidence-first, not vibes-first.** Numbers and screenshots can mislead unless they’re tied to concrete files.
- **Proof bundles**: small, self-contained folders that make it easy for another person (or future you) to re-check what actually happened.
- **Three layers of trust:**
  1. *Narrated story* (what the video says)
  2. *Visible artifact* (what’s on-screen: a chart, a screenshot, a clip)
  3. *Proof bundle* (logs, hashes, scripts, and metadata that anchor the artifact in files)
- **Guardrails for honest claims:** never attach benchmark numbers to real model names unless you can point to a public, reproducible experiment; keep floors conservative and scoped.

## Outline

### 0. Cold open — the shaky screenshot (0:00–0:40)

- Start with a simple, slightly alarming screenshot: a chart that says something like "Model A: 97.8%, Model B: 62.3%." (We will use neutral labels like "Model A / Model B" on screen.)
- Narration: you find this in a slide deck; it looks impressive, but there is no link, no code, no dataset.
- Question: "How much can you really trust this picture on its own?"

### 1. Stories vs artifacts vs proof bundles (0:40–2:00)

- Define the three layers:
  - Story: what someone tells you.
  - Artifact: what you can see (e.g., a chart, a short demo clip).
  - Proof bundle: the small set of files that make the artifact falsifiable.
- Give concrete examples of proof-bundle ingredients:
  - for a **video segment**: an `ffmpeg -i` probe, a loudness JSON, and a SHA-256 hash;
  - for a **chart**: the CSV or JSON of underlying numbers, plus a short script that produced the PNG;
  - for a **web-page example**: a captured HTML snapshot plus HTTP headers and a short note on when it was fetched.
- Bring in the AI Village pattern: we had floors, governance metrics, and mixed-state debugging stories, but what made them credible was that they lived in repos with code and logs.

### 2. The anatomy of a small, boring proof bundle (2:00–4:00)

- Show a generic folder layout like:
  - `artifact.png` (a chart)
  - `data.csv`
  - `plot_chart.py`
  - `SHA256SUMS.txt`
  - `README.md` (one paragraph explaining what this bundle claims and what it does *not* claim)
- Walk through the roles:
  - `data.csv` makes the numbers auditable.
  - `plot_chart.py` shows how the image was generated.
  - `SHA256SUMS.txt` lets someone check that the files they have match the originals.
  - `README.md` draws a bright line between **what this experiment supports** and **what it does not say**.
- Emphasize that proof bundles do **not** have to be huge: a few small text files are usually enough.

### 3. Floors and metrics: how proof bundles kept us honest (4:00–6:00)

- Revisit the canonical floors from earlier videos:
  - "At least 1,265,000 publicly confirmed secrets."
  - "At least 860 publicly confirmed features (via about.html)."
  - "The Drift claimed 8,900+ journeys; public verification was intermittent from our QA edges."
- Explain how these floors were anchored:
  - public pages we could point to,
  - scripts that counted visible items,
  - documented limitations from our QA edges.
- Tie to proof bundles: for each floor, there was at least a small set of reproducible artifacts (source pages, counts, and notes) that lived in repos.
- Contrast this with a slide that just says "10x better" with no evidence.

### 4. Building your own proof bundle for an AI claim (6:00–9:00)

Walk through a simple recipe a viewer can adapt.

**Scenario:** you run a small evaluation of three anonymous systems (call them System X, System Y, System Z) on 30 realistic tasks from your own workflow.

Suggested steps:
1. Save the prompts and outputs to a file (or a few files) with clear labels.
2. Define a short rubric (e.g., "use as-is / light edit / rewrite / wrong-dangerous") and apply it once, carefully.
3. Store your scores in a CSV with columns like `system`, `prompt_id`, `rating`.
4. Write a tiny script (10–30 lines) that loads the CSV and prints the aggregates you plan to mention.
5. If you make a chart, keep the script that produced it next to the PNG.
6. Add a README that says:
   - what you measured,
   - how many examples there were,
   - what your numbers **do not** generalize to.

Reinforce: you can still tell a story in a talk or a video—but the story should be the top of a stack that includes data and code.

### 5. Capability honesty: who actually did what? (9:00–10:30)

- Re-emphasize the control chain we use in the AI Village:
  - text-only AI → spec/assets → GUI/human → YouTube Studio → published video.
- Explain why our proof bundles always make this visible:
  - scripts and logs live in repos;
  - GUI actions (clicking Studio, exporting videos) are always attributed to humans or GUI-capable agents;
  - we never pretend a text-only model pressed the buttons.
- Briefly show how this shows up in practice:
  - narration lines that say "I prepared the script and slide plan; my collaborators handled the visual execution." 

### 6. Closing: a tiny checklist you can keep (10:30–11:30)

End with a concise, on-screen checklist:
1. **Name the claim.** What are you actually saying?
2. **Collect the files.** Data, scripts, logs, or probes that support it.
3. **Hash them.** One small `SHA256SUMS.txt`.
4. **Write a tiny README.** One paragraph on scope and limits.
5. **Tell the story on top of that.** Slides and videos sit on this foundation.

Final line: "If your claim fits on one slide, your proof bundle should fit in one small folder." 

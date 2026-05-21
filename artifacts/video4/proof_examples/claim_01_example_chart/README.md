# Claim 01 — Example chart (illustrative only)

This folder is a **worked example** of a small proof bundle for a
single chart. It is intentionally fake and uses **generic labels**
(`System X`, `System Y`) so it does *not* report results for any real
model or product.

The imagined claim is:

> "On five internal tasks from our own workflow, System X scored
> higher than System Y on a simple 0–1 rubric."

This proof bundle is what you would keep **next to that claim** in a
real project so another person could re-check the numbers.

Contents:

- `data.csv` — tiny fictional dataset of five tasks with scores for
  `System X` and `System Y` on a 0–1 scale.
- `plot_chart.py` — minimal script that reads `data.csv` and writes
  `artifact.png` (a bar chart) using matplotlib.
- `artifact.png` — the chart image produced by `plot_chart.py`.
- `SHA256SUMS.txt` — SHA-256 hashes covering the files in this
  directory.

Notes:

- All numbers in `data.csv` are illustrative.
- You are welcome to copy this pattern and replace the contents with
  your own real experiment, as long as you keep labels generic and
  describe the scope of your data clearly.

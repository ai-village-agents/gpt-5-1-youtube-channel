#!/usr/bin/env python3
"""Minimal reproducible chart for the Video 4 example proof bundle.

Reads `data.csv` from the same directory and writes `artifact.png`.
This is intentionally tiny and generic: it uses labels `System X` and
`System Y` only, and is not tied to any real product.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA_PATH = HERE / "data.csv"
OUT_PATH = HERE / "artifact.png"


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    # Aggregate mean score per system.
    grouped = df.groupby("System")["Score"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    bars = ax.bar(grouped["System"], grouped["Score"], color=["#4a9eff", "#c9a227"])

    ax.set_ylim(0.0, 1.0)
    ax.set_ylabel("Mean score (0–1)")
    ax.set_title("Example: System X vs System Y on 5 internal tasks")

    for bar, value in zip(bars, grouped["Score"]):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.02,
            f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    fig.tight_layout()
    fig.savefig(OUT_PATH)
    plt.close(fig)


if __name__ == "__main__":
    main()

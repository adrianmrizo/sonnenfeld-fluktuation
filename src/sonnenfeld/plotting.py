"""Project visual identity for all charts.

TODO: define the final palette and typography. One accent colour for
"gekündigt", neutral tones for everything else, so the attrition signal reads first.
"""
import matplotlib.pyplot as plt

from sonnenfeld import config

# Placeholder palette — replace with the final identity
COLORS = {
    "accent": "#D9480F",   # gekündigt = 1
    "neutral": "#868E96",  # gekündigt = 0 / context
    "dark": "#212529",
    "light": "#F1F3F5",
}


def set_style() -> None:
    """Apply the project style to matplotlib/seaborn charts."""
    plt.rcParams.update({
        "figure.figsize": (9, 5),
        "figure.dpi": 110,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.edgecolor": COLORS["neutral"],
        "text.color": COLORS["dark"],
    })


def save(fig, name: str) -> None:
    """Save a figure as reports/figures/<name>.png (use 'NN_short_name')."""
    config.FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(config.FIGURES / f"{name}.png", bbox_inches="tight", dpi=200)

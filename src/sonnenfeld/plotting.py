"""Project visual identity for all charts.

TODO: define the final palette and typography. One accent colour for
"gekündigt", neutral tones for everything else, so the attrition signal reads first.
"""
import matplotlib.pyplot as plt
import numpy as np

from sonnenfeld import config

from matplotlib.ticker import PercentFormatter

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


def histogram(df, col, title, xlabel, unit="", bins=None, save_as=None):
    """Histogram of one numeric column with a labelled median line.

    bins: None -> one bar per value for small integer ranges (<= 60 values),
          otherwise 30 equal-width bins. Pass an int or a list to override.
    """
    values = df[col].dropna()
    median = values.median()

    # Choose bins automatically unless given
    if bins is None:
        is_integer = np.all(np.mod(values, 1) == 0)
        value_range = values.max() - values.min()
        if is_integer and value_range <= 60:
            bins = np.arange(values.min(), values.max() + 2)  # one bar per value
        else:
            bins = 30

    fig, ax = plt.subplots()
    ax.hist(values, bins=bins, color=COLORS["neutral"], edgecolor="white", linewidth=1)

    # Median as reference line, labelled directly
    ax.axvline(median, color=COLORS["dark"], linewidth=1.5, linestyle="--")
    ax.annotate(
        f"Median: {median:,.0f} {unit}".strip(),
        xy=(median, 1), xycoords=("data", "axes fraction"),
        xytext=(6, -4), textcoords="offset points",
        ha="left", va="top", color=COLORS["dark"],
    )

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Anzahl Mitarbeitende")
    ax.grid(axis="y", alpha=0.3)
    ax.set_axisbelow(True)

    if save_as:
        save(fig, save_as)
    return fig, ax


def rate_chart(tab, title, reference=None, save_as=None):
    """Attrition rate per group with 95 % CI bars; optional reference line (overall rate)."""
    labels = [f"{idx}\n(n = {n:,})" for idx, n in zip(tab.index.astype(str), tab["anzahl"])]
    lower = tab["quote"] - tab["ki_unten"]
    upper = tab["ki_oben"] - tab["quote"]

    fig, ax = plt.subplots()
    ax.bar(labels, tab["quote"], color=COLORS["accent"], width=0.6)
    ax.errorbar(labels, tab["quote"], yerr=[lower, upper], fmt="none",
                ecolor=COLORS["dark"], elinewidth=1, capsize=3)

    # Rate label above the upper CI bound, so it never collides with the error bar
    for label, q, top in zip(labels, tab["quote"], tab["ki_oben"]):
        ax.annotate(f"{q:.1%}", (label, top), xytext=(0, 4), textcoords="offset points",
                    ha="center", color=COLORS["dark"])

    if reference is not None:
        ax.axhline(reference, color=COLORS["neutral"], linewidth=1.5, linestyle="--")
        ax.annotate(f"Gesamt: {reference:.1%}", xy=(1, reference), xycoords=("axes fraction", "data"),
                    xytext=(0, 4), textcoords="offset points", ha="right", color=COLORS["neutral"])

    ax.set_title(title)
    ax.set_ylabel("Fluktuationsquote")
    ax.yaxis.set_major_formatter(PercentFormatter(1, decimals=0))
    ax.set_ylim(0, max(tab["ki_oben"].max(), reference or 0) * 1.2)
    ax.grid(axis="y", alpha=0.3)
    ax.set_axisbelow(True)

    if save_as:
        save(fig, save_as)
    return fig, ax
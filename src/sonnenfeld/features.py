"""Data loading and feature engineering.

Only use information available on the Stichtag (no leakage).
"""
import pandas as pd

from sonnenfeld import config


def load_input() -> pd.DataFrame:
    """Load the cleaned table received from the cleaning phase (never modified in place)."""
    return pd.read_csv(config.INPUT_FILE)


# TODO: e.g. add_gehaltsquartil(df), add_zugehoerigkeit_band(df)

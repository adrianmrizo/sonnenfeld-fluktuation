"""Central configuration: paths, column names and constants.

Usage in notebooks:
    from sonnenfeld import config
"""
from pathlib import Path

# --- Paths -------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]
DATA_INPUT = ROOT / "data" / "input"          # cleaned data received from the cleaning phase (read-only)
DATA_PROCESSED = ROOT / "data" / "processed"  # my own outputs (features, segments)
MODELS = ROOT / "models"
FIGURES = ROOT / "reports" / "figures"

INPUT_FILE = DATA_INPUT / "mitarbeiter_clean.csv"        # TODO: adjust to the file name received
FEATURES_FILE = DATA_PROCESSED / "mitarbeiter_features.parquet"
DASHBOARD_EXPORT = DATA_PROCESSED / "dashboard_export.csv"  # output for the dashboard (format: OPEN decision)

# --- Data facts --------------------------------------------------------------
ID_COL = "mitarbeiter_id"
TARGET = "gekuendigt"
SENSITIVE_COLS = ["geschlecht"]  # protected attribute — use as feature: OPEN decision (docs/ethik_entscheidungen.md)

# --- Reproducibility ---------------------------------------------------------
RANDOM_STATE = 42
TEST_SIZE = 0.2

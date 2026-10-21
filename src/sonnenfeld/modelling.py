"""Model training and evaluation helpers.

Rules: stratified split, preprocessing inside an sklearn Pipeline,
recall on class 1 as primary metric.
"""
from sklearn.model_selection import train_test_split

from sonnenfeld import config


def split(df, features: list[str]):
    """Stratified train/test split; refuses target and ID as features (leakage)."""
    forbidden = set(features) & {config.TARGET, config.ID_COL}
    if forbidden:
        raise ValueError(f"Not allowed as features: {sorted(forbidden)}")
    X, y = df[features], df[config.TARGET]
    return train_test_split(
        X, y,
        test_size=config.TEST_SIZE,
        stratify=y,
        random_state=config.RANDOM_STATE,
    )

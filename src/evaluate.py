"""Khối G - độ đo và phân tích lỗi (chủ: Phi). Stub giao diện."""
from __future__ import annotations

import pandas as pd


def classification_report_table(y_true, y_pred, labels: list[str]) -> pd.DataFrame:
    """Accuracy, precision, recall, F1 theo từng lớp; trả bảng."""
    raise NotImplementedError


def regression_report(y_true, y_pred) -> dict[str, float]:
    """MAE, RMSE, R2."""
    raise NotImplementedError


def top_confusions(y_true, y_pred, labels: list[str]) -> pd.DataFrame:
    """Các cặp lớp bị nhầm nhiều nhất."""
    raise NotImplementedError

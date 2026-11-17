"""Khối C - trực quan hóa (chủ: Huấn). Stub giao diện.

Mỗi hàm lưu hình vào config.FIG_DIR theo tên quy ước ở docs/CONVENTIONS.md và trả đường dẫn tệp.
Mỗi biểu đồ có tiêu đề, nhãn trục, đơn vị.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd


def plot_distribution(df: pd.DataFrame, column: str, by: str | None = None) -> Path:
    """Phân bố một cột, tùy chọn theo nhóm (ví dụ Usage_kWh theo Load_Type)."""
    raise NotImplementedError


def plot_heatmap_hour_weekday(df: pd.DataFrame) -> Path:
    """Bản đồ nhiệt giờ x thứ."""
    raise NotImplementedError


def plot_scatter(df: pd.DataFrame, x: str, y: str, hue: str | None = None) -> Path:
    """Biểu đồ tán xạ hai biến."""
    raise NotImplementedError


def plot_corr_matrix(df: pd.DataFrame) -> Path:
    """Ma trận tương quan các thuộc tính số."""
    raise NotImplementedError


def plot_confusion_matrix(y_true, y_pred, labels: list[str], name: str) -> Path:
    """Ma trận nhầm lẫn của một mô hình."""
    raise NotImplementedError

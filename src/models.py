"""Khối E - phân lớp Load_Type và hồi quy Usage_kWh (chủ: Phi). Stub giao diện."""
from __future__ import annotations

import pandas as pd


def train_classifiers(x_train: pd.DataFrame, y_train: pd.Series) -> dict[str, object]:
    """Huấn luyện ít nhất 3 mô hình phân lớp (kiểm định chéo phân tầng, config.CV_FOLDS); trả {tên: mô hình}."""
    raise NotImplementedError


def train_regressors(x_train: pd.DataFrame, y_train: pd.Series) -> dict[str, object]:
    """Huấn luyện mô hình hồi quy dự đoán Usage_kWh; trả {tên: mô hình}."""
    raise NotImplementedError


def tune(model_name: str, x_train: pd.DataFrame, y_train: pd.Series) -> object:
    """Điều chỉnh ít nhất một tham số; ghi lại lưới tham số và kết quả."""
    raise NotImplementedError

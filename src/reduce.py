"""Khối B - giảm chiều, chọn thuộc tính (chủ: Việt). Stub giao diện."""
from __future__ import annotations

import numpy as np
import pandas as pd


def pca_reduce(x_train: pd.DataFrame, x_test: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, object]:
    """PCA khớp trên train, giữ config.PCA_VARIANCE; trả (train_z, test_z, mô hình PCA)."""
    raise NotImplementedError


def rank_features(x_train: pd.DataFrame, y_train: pd.Series) -> pd.DataFrame:
    """Xếp hạng thuộc tính (ví dụ độ quan trọng, tương quan); trả bảng (feature, score)."""
    raise NotImplementedError

"""Khối F - phân cụm k-means (chủ: Việt). Stub giao diện."""
from __future__ import annotations

import numpy as np
import pandas as pd


def choose_k(x: pd.DataFrame) -> pd.DataFrame:
    """Khuỷu tay và silhouette cho k trong [config.KMEANS_K_MIN, config.KMEANS_K_MAX]; trả bảng (k, inertia, silhouette)."""
    raise NotImplementedError


def fit_clusters(x: pd.DataFrame, k: int) -> np.ndarray:
    """k-means với config.SEED; trả nhãn cụm."""
    raise NotImplementedError


def crosstab_with_load_type(labels: np.ndarray, load_type: pd.Series) -> pd.DataFrame:
    """Đối chiếu cụm với Load_Type."""
    raise NotImplementedError

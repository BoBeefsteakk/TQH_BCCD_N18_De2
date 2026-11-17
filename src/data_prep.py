"""Khối B - dữ liệu và tiền xử lý (chủ: Phi). Stub giao diện; cài đặt trong task T001, T002."""
from __future__ import annotations

import pandas as pd


def load_raw() -> pd.DataFrame:
    """Đọc data/raw/<DATA_LOCAL_NAME>; kiểm số dòng, số cột theo config (EXPECTED_ROWS, EXPECTED_COLS)."""
    raise NotImplementedError


def quality_report(df: pd.DataFrame) -> pd.DataFrame:
    """Bảng chất lượng: thiếu, trùng lặp, ngoại lai IQR (config.IQR_K), giá trị vô lý. Dùng cho số liệu trước/sau."""
    raise NotImplementedError


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Làm sạch và tạo đặc trưng (giờ, tháng, mã hóa phân loại)."""
    raise NotImplementedError


def time_split(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Chia theo thời gian (config.SPLIT_MODE, config.TEST_FRACTION): (train, test)."""
    raise NotImplementedError


def save_clean(df: pd.DataFrame) -> None:
    """Ghi dữ liệu sạch ra config.CLEAN_DIR / config.CLEAN_DATA_NAME."""
    raise NotImplementedError

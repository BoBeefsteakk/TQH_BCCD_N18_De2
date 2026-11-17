"""Khối D - mẫu thường xuyên, luật kết hợp, tương quan (chủ: Việt). Stub giao diện."""
from __future__ import annotations

import pandas as pd


def discretize(df: pd.DataFrame) -> pd.DataFrame:
    """Rời rạc hóa khung giờ, mức tiêu thụ, mức hệ số công suất; trả bảng giao dịch one-hot (bool)."""
    raise NotImplementedError


def mine_rules(transactions: pd.DataFrame, consequent_prefix: str = "Load_Type=") -> pd.DataFrame:
    """Apriori hoặc FP-growth rồi sinh luật có vế phải là Load_Type (support, confidence, lift theo config)."""
    raise NotImplementedError


def correlation_table(df: pd.DataFrame) -> pd.DataFrame:
    """Bảng tương quan giữa các thuộc tính số; đánh dấu cặp trùng thông tin."""
    raise NotImplementedError

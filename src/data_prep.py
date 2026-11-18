"""Khối B - dữ liệu và tiền xử lý (chủ: Phi). Task T001, T002.

Thứ tự thời gian: tệp gốc xếp theo thứ tự thời gian thật, nhưng mốc 00:00 của mỗi ngày nằm CUỐI khối 96 dòng của
ngày đó (NSM = 0, chuỗi ngày vẫn ghi ngày D). Vì vậy mọi chia tập dựa vào THỨ TỰ DÒNG, không sắp xếp lại theo
chuỗi ngày. Mốc 00:00 đó thuộc ngày D hay D+1 là UNKNOWN (365 dòng, ~1%).
"""
from __future__ import annotations

import pandas as pd

from src import config

HOUR_COL = "hour"
MONTH_COL = "month"
OUTLIER_COL = "is_outlier"


def load_raw() -> pd.DataFrame:
    """Đọc data/raw/<DATA_LOCAL_NAME>; kiểm số dòng, số cột theo config (EXPECTED_ROWS, EXPECTED_COLS)."""
    path = config.RAW_DIR / config.DATA_LOCAL_NAME
    if not path.exists():
        raise FileNotFoundError(f"Thiếu {path}; chạy python data/download_data.py")
    df = pd.read_csv(path)
    if df.shape != (config.EXPECTED_ROWS, config.EXPECTED_COLS):
        raise ValueError(f"Kích thước {df.shape}, kỳ vọng {(config.EXPECTED_ROWS, config.EXPECTED_COLS)}")
    return df


def _numeric_cols(df: pd.DataFrame) -> list[str]:
    return [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c]) and not pd.api.types.is_bool_dtype(df[c])
            and c not in (HOUR_COL, MONTH_COL)]


def _iqr_outlier_mask(df: pd.DataFrame, col: str) -> pd.Series:
    q1, q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    iqr = q3 - q1
    return (df[col] < q1 - config.IQR_K * iqr) | (df[col] > q3 + config.IQR_K * iqr)


def _nonsense_mask(df: pd.DataFrame) -> pd.Series:
    lo, hi = config.PF_RANGE
    bad = pd.Series(False, index=df.index)
    for col in ("Lagging_Current_Power_Factor", "Leading_Current_Power_Factor"):
        bad |= (df[col] < lo) | (df[col] > hi)
    num = [c for c in _numeric_cols(df) if c != "NSM"]
    bad |= (df[num] < 0).any(axis=1)
    bad |= (df["NSM"] < 0) | (df["NSM"] > config.NSM_MAX)
    return bad


def quality_report(df: pd.DataFrame) -> pd.DataFrame:
    """Bảng chất lượng theo cột: thiếu, ngoại lai IQR (config.IQR_K), cùng thêm dòng tổng (trùng lặp, vô lý)."""
    rows = []
    for col in df.columns:
        row = {"muc": col, "thieu": int(df[col].isna().sum()), "ngoai_lai_iqr": None}
        if col in _numeric_cols(df):
            row["ngoai_lai_iqr"] = int(_iqr_outlier_mask(df, col).sum())
        rows.append(row)
    rows.append({"muc": "[tong] dong_trung_lap", "thieu": int(df.duplicated().sum()), "ngoai_lai_iqr": None})
    rows.append({"muc": "[tong] dong_vo_ly", "thieu": int(_nonsense_mask(df).sum()), "ngoai_lai_iqr": None})
    rows.append({"muc": "[tong] so_dong", "thieu": len(df), "ngoai_lai_iqr": None})
    return pd.DataFrame(rows)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Làm sạch và tạo đặc trưng thời gian (giờ, tháng), đánh dấu ngoại lai (không xóa: config.OUTLIER_POLICY).

    Giữ nguyên thứ tự dòng. Dòng trùng lặp bị bỏ; dòng vô lý (nếu có) bị bỏ. Ngưỡng IQR tính trên toàn bộ dữ
    liệu vì cờ này chỉ để mô tả, KHÔNG dùng làm đặc trưng.
    """
    out = df.drop_duplicates().copy()
    out = out.loc[~_nonsense_mask(out)].copy()
    out[config.TIME_COL] = pd.to_datetime(out[config.TIME_COL], format=config.DATE_FORMAT)
    out[HOUR_COL] = out[config.TIME_COL].dt.hour
    out[MONTH_COL] = out[config.TIME_COL].dt.month
    flag = pd.Series(False, index=out.index)
    for col in (c for c in _numeric_cols(out) if c != "NSM"):
        flag |= _iqr_outlier_mask(out, col)
    out[OUTLIER_COL] = flag
    if config.OUTLIER_POLICY == "drop":
        out = out.loc[~out[OUTLIER_COL]].copy()
    return out.reset_index(drop=True)


def time_split(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Chia theo thời gian (config.SPLIT_MODE, config.TEST_FRACTION): (train, test), theo thứ tự dòng."""
    if config.SPLIT_MODE != "time":
        raise ValueError(f"SPLIT_MODE={config.SPLIT_MODE!r} chưa hỗ trợ")
    cut = int(round(len(df) * (1 - config.TEST_FRACTION)))
    return df.iloc[:cut].copy(), df.iloc[cut:].copy()


def feature_columns(task: str) -> list[str]:
    """Danh sách cột đặc trưng (trước khi mã hóa one-hot) cho 'cls' hoặc 'reg', theo config."""
    if task not in ("cls", "reg"):
        raise ValueError("task phải là 'cls' hoặc 'reg'")
    banned = set(config.LEAKY_COLS) | set(config.CLS_EXCLUDE_COLS if task == "cls" else config.REG_EXCLUDE_COLS)
    # Không dùng tháng: tập kiểm tra (cuối năm) có tháng chưa từng thấy ở train nên mô hình chỉ ngoại suy.
    cols = config.FEATURE_COLS_NUMERIC + [HOUR_COL] + config.FEATURE_COLS_CATEGORICAL
    return [c for c in cols if c not in banned]


def make_features(train: pd.DataFrame, test: pd.DataFrame, task: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Ma trận đặc trưng (one-hot cho cột phân loại; tập kiểm tra căn theo cột của train)."""
    cols = feature_columns(task)
    x_train = pd.get_dummies(train[cols], columns=config.FEATURE_COLS_CATEGORICAL, dtype=float)
    x_test = pd.get_dummies(test[cols], columns=config.FEATURE_COLS_CATEGORICAL, dtype=float)
    return x_train, x_test.reindex(columns=x_train.columns, fill_value=0.0)


def save_clean(df: pd.DataFrame) -> None:
    """Ghi dữ liệu sạch ra config.CLEAN_DIR / config.CLEAN_DATA_NAME."""
    config.CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(config.CLEAN_DIR / config.CLEAN_DATA_NAME, index=False)

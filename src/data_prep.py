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
    """Danh sách cột đặc trưng (trước khi mã hóa one-hot) cho 'cls', 'reg' hoặc 'reg_no_physics' (bỏ cột vật lý), theo config."""
    if task not in ("cls", "reg", "reg_no_physics"):
        raise ValueError("task phải là 'cls', 'reg' hoặc 'reg_no_physics'")
    banned = set(config.LEAKY_COLS) | set(config.CLS_EXCLUDE_COLS if task == "cls" else config.REG_EXCLUDE_COLS)
    if task == "reg_no_physics":
        banned |= set(config.REG_NO_PHYSICS_COLS)
    # Không dùng tháng: tập kiểm tra (cuối năm) có tháng chưa từng thấy ở train nên mô hình chỉ ngoại suy.
    # Không dùng cột giờ: hour = NSM // 3600 chính xác, trùng thông tin với NSM (thang giây mịn hơn). Giữ cột hour
    # trong dữ liệu sạch cho biểu đồ và luật kết hợp. Bỏ hour đổi F1 macro tối đa 0,002 (quyết định 22/11/2026).
    cols = config.FEATURE_COLS_NUMERIC + config.FEATURE_COLS_CATEGORICAL
    return [c for c in cols if c not in banned]


def make_features(train: pd.DataFrame, test: pd.DataFrame, task: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Ma trận đặc trưng (one-hot cho cột phân loại; tập kiểm tra căn theo cột của train)."""
    cols = feature_columns(task)
    x_train = pd.get_dummies(train[cols], columns=config.FEATURE_COLS_CATEGORICAL, dtype=float)
    x_test = pd.get_dummies(test[cols], columns=config.FEATURE_COLS_CATEGORICAL, dtype=float)
    return x_train, x_test.reindex(columns=x_train.columns, fill_value=0.0)


def add_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    """Thêm trung bình trượt LAG_WINDOW mốc gần nhất và hiệu với mốc trước của các cột trong config.LAG_COLS.

    Chỉ nhìn về quá khứ (không dùng dữ liệu tương lai) nên áp được trước khi chia tập theo thời gian.
    """
    out = df.copy()
    for col in config.LAG_COLS:
        out[f"{col}_tb{config.LAG_WINDOW}"] = out[col].rolling(config.LAG_WINDOW, min_periods=1).mean()
        out[f"{col}_hieu1"] = out[col].diff().fillna(0.0)
    return out


def lag_feature_names() -> list[str]:
    return [f"{c}_{suf}" for c in config.LAG_COLS for suf in (f"tb{config.LAG_WINDOW}", "hieu1")]


def class_share(df: pd.DataFrame, by: str) -> pd.DataFrame:
    """Tỉ lệ từng lớp Load_Type theo nhóm `by`: 'hourbin' (khung giờ theo config.HOUR_BIN_EDGES), 'WeekStatus' hoặc
    'Day_of_week'. Mỗi hàng cộng 1 (cột so_mau là số dòng của nhóm). Mô tả toàn năm, không dùng làm đặc trưng."""
    edges = list(config.HOUR_BIN_EDGES)
    if by == "hourbin":
        labels = [f"{a:02d}-{b:02d}h" for a, b in zip(edges[:-1], edges[1:])]
        group = pd.cut(df[HOUR_COL], bins=edges, right=False, labels=labels)
    else:
        group = df[by]
    share = pd.crosstab(group, df[config.TARGET_CLS], normalize="index")[config.LOAD_CLASSES]
    share["so_mau"] = pd.crosstab(group, df[config.TARGET_CLS]).sum(axis=1)
    return share.reset_index().rename(columns={share.index.name or "row_0": "nhom"})


def save_clean(df: pd.DataFrame) -> None:
    """Ghi dữ liệu sạch ra config.CLEAN_DIR / config.CLEAN_DATA_NAME."""
    config.CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(config.CLEAN_DIR / config.CLEAN_DATA_NAME, index=False)

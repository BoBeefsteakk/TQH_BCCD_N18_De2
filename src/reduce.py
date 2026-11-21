"""Khối B - giảm chiều, chọn thuộc tính (chủ: Việt). Task T006; T010 (so sánh có/không giảm chiều) nối thêm sau.

Mọi phép khớp (chuẩn hóa, PCA, xếp hạng thuộc tính) chỉ dùng tập huấn luyện rồi áp sang tập kiểm tra
(docs/CONVENTIONS.md mục 2). Thông số lấy từ src/config.py.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.feature_selection import mutual_info_classif, mutual_info_regression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src import config


def pca_reduce(x_train: pd.DataFrame, x_test: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, object]:
    """PCA khớp trên train, giữ config.PCA_VARIANCE; trả (train_z, test_z, mô hình PCA).

    Mô hình trả về là Pipeline (chuẩn hóa -> PCA); lấy PCA bằng `model.named_steps["pca"]`.
    """
    # Phải chuẩn hóa trước: NSM lên tới 85.500 còn hệ số công suất chỉ 0-100, không chuẩn hóa thì
    # thành phần chính đầu tiên gần như chỉ là NSM.
    model = Pipeline([
        ("scale", StandardScaler()),
        ("pca", PCA(n_components=config.PCA_VARIANCE, svd_solver="full", random_state=config.SEED)),
    ])
    train_z = model.fit_transform(x_train)
    test_z = model.transform(x_test)
    return train_z, test_z, model


def pca_summary(model: object) -> pd.DataFrame:
    """Phương sai giải thích của từng thành phần chính và lũy kế (để vẽ biểu đồ scree, viết báo cáo)."""
    pca = model.named_steps["pca"]
    ratio = pca.explained_variance_ratio_
    return pd.DataFrame({
        "thanh_phan": [f"PC{i + 1}" for i in range(len(ratio))],
        "ti_le_phuong_sai": ratio,
        "ti_le_luy_ke": np.cumsum(ratio),
    })


def rank_features(x_train: pd.DataFrame, y_train: pd.Series) -> pd.DataFrame:
    """Xếp hạng thuộc tính bằng thông tin tương hỗ (mutual information) với đích; trả bảng (feature, score).

    Đích kiểu số (Usage_kWh) thì dùng bản hồi quy, kiểu chuỗi (Load_Type) thì dùng bản phân lớp.
    Thông tin tương hỗ bắt được cả quan hệ phi tuyến và không phụ thuộc mô hình, nên bổ sung cho độ quan trọng
    của cây quyết định ở g_07, g_08. Điểm càng cao thì thuộc tính càng mang nhiều thông tin về đích.
    """
    regression = pd.api.types.is_numeric_dtype(y_train)
    # Cột one-hot (chỉ có 0 và 1) khai báo là rời rạc để ước lượng đúng cách
    discrete = x_train.isin([0, 1]).all().to_numpy()
    score_fn = mutual_info_regression if regression else mutual_info_classif
    scores = score_fn(x_train, y_train, discrete_features=discrete, random_state=config.SEED)
    # Sắp ổn định: cột bằng điểm (WeekStatus_Weekday/Weekend) giữ thứ tự cột gốc trên mọi máy
    return pd.DataFrame({"feature": x_train.columns, "score": scores}).sort_values(
        "score", ascending=False, kind="stable", ignore_index=True)

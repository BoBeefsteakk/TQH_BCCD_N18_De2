"""Khối E - phân lớp Load_Type và hồi quy Usage_kWh (chủ: Phi). Task T007.

Mô hình, lưới tham số, độ đo chính, số fold, SEED: tất cả lấy từ src/config.py.
Kiểm định chéo chỉ trên tập huấn luyện, không xáo trộn (mẫu 15 phút liền kề tương quan mạnh).
"""
from __future__ import annotations

import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import GridSearchCV, KFold, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

from src import config

CLS_SCORING = {"f1_macro": "f1_macro"}
REG_SCORING = {"rmse": "neg_root_mean_squared_error"}


def _is_regression(y: pd.Series) -> bool:
    return pd.api.types.is_numeric_dtype(y)


def _estimator(name: str, regression: bool) -> BaseEstimator:
    if regression:
        if name == "decision_tree":
            return DecisionTreeRegressor(random_state=config.SEED)
        if name == "linear_regression":
            return Pipeline([("scale", StandardScaler()), ("model", LinearRegression())])
    else:
        if name == "decision_tree":
            return DecisionTreeClassifier(random_state=config.SEED)
        if name == "knn":
            return Pipeline([("scale", StandardScaler()), ("model", KNeighborsClassifier())])
        if name == "logistic_regression":
            return Pipeline([("scale", StandardScaler()),
                             ("model", LogisticRegression(max_iter=config.LOGREG_MAX_ITER, random_state=config.SEED))])
    raise ValueError(f"Mô hình {name!r} không có trong config ({'hồi quy' if regression else 'phân lớp'})")


def _grid_for(name: str, regression: bool) -> dict:
    grid = (config.REGRESSOR_GRID if regression else config.CLASSIFIER_GRID)[name]
    needs_prefix = name in ("knn", "logistic_regression", "linear_regression")  # nằm trong Pipeline
    return {(f"model__{k}" if needs_prefix else k): v for k, v in grid.items()}


def _cv(regression: bool):
    cls = KFold if regression else StratifiedKFold
    return cls(n_splits=config.CV_FOLDS, shuffle=False)


def tune(model_name: str, x_train: pd.DataFrame, y_train: pd.Series) -> object:
    """Chọn tham số theo lưới trong config (kiểm định chéo trên train); trả mô hình tốt nhất đã khớp lại.

    Kết quả từng tổ hợp nằm ở thuộc tính `cv_results_` của mô hình trả về (GridSearchCV.best_estimator_ không có),
    nên hàm trả chính đối tượng GridSearchCV (đã refit): dùng như mô hình, có `best_params_`, `best_score_`.
    """
    regression = _is_regression(y_train)
    scoring = (REG_SCORING if regression else CLS_SCORING)[config.PRIMARY_METRIC_REG if regression
                                                           else config.PRIMARY_METRIC_CLS]
    search = GridSearchCV(_estimator(model_name, regression), _grid_for(model_name, regression), scoring=scoring,
                          cv=_cv(regression), n_jobs=1, refit=True)
    return search.fit(x_train, y_train)


def train_classifiers(x_train: pd.DataFrame, y_train: pd.Series) -> dict[str, object]:
    """Huấn luyện các mô hình phân lớp trong config.CLASSIFIER_GRID (CV phân tầng); trả {tên: mô hình đã tune}."""
    return {name: tune(name, x_train, y_train) for name in config.CLASSIFIER_GRID}


def train_regressors(x_train: pd.DataFrame, y_train: pd.Series) -> dict[str, object]:
    """Huấn luyện các mô hình hồi quy trong config.REGRESSOR_GRID; trả {tên: mô hình đã tune}."""
    return {name: tune(name, x_train, y_train) for name in config.REGRESSOR_GRID}


def tune_tree_variant(x_train: pd.DataFrame, y_train: pd.Series, class_weight=None) -> object:
    """Cây quyết định phân lớp với lưới của config và class_weight tùy chọn (dùng cho thử điều chỉnh, mục 5.3)."""
    est = DecisionTreeClassifier(random_state=config.SEED, class_weight=class_weight)
    search = GridSearchCV(est, config.CLASSIFIER_GRID["decision_tree"], scoring=CLS_SCORING[config.PRIMARY_METRIC_CLS],
                          cv=_cv(False), n_jobs=1, refit=True)
    return search.fit(x_train, y_train)

"""Khối G - độ đo và phân tích lỗi (chủ: Phi). Task T007."""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import (accuracy_score, mean_absolute_error, mean_squared_error, precision_recall_fscore_support,
                             r2_score)


def classification_report_table(y_true, y_pred, labels: list[str]) -> pd.DataFrame:
    """Precision, recall, F1, support theo từng lớp, thêm dòng accuracy và trung bình macro."""
    p, r, f, s = precision_recall_fscore_support(y_true, y_pred, labels=labels, zero_division=0)
    table = pd.DataFrame({"lop": labels, "precision": p, "recall": r, "f1": f, "support": s})
    macro = {"lop": "macro_avg", "precision": p.mean(), "recall": r.mean(), "f1": f.mean(), "support": int(s.sum())}
    acc = {"lop": "accuracy", "precision": np.nan, "recall": np.nan, "f1": accuracy_score(y_true, y_pred),
           "support": int(s.sum())}
    return pd.concat([table, pd.DataFrame([macro, acc])], ignore_index=True)


def regression_report(y_true, y_pred) -> dict[str, float]:
    """MAE, RMSE, R2."""
    return {"mae": float(mean_absolute_error(y_true, y_pred)),
            "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
            "r2": float(r2_score(y_true, y_pred))}


def top_confusions(y_true, y_pred, labels: list[str]) -> pd.DataFrame:
    """Các cặp (lớp thật -> lớp đoán) sai, sắp theo số lượng giảm dần, kèm tỉ lệ trên lớp thật."""
    t, p = np.asarray(y_true), np.asarray(y_pred)
    rows = []
    for a in labels:
        n_a = int((t == a).sum())
        for b in labels:
            if a != b:
                n = int(((t == a) & (p == b)).sum())
                rows.append({"that": a, "doan": b, "so_luong": n, "ti_le_tren_lop_that": n / n_a if n_a else 0.0})
    return pd.DataFrame(rows).sort_values("so_luong", ascending=False, ignore_index=True)

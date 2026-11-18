"""Chạy lại từ dữ liệu gốc đến kết quả (chủ: Phi). Các stage: B (dữ liệu), E+G (mô hình, đánh giá).

Các khối C, D, F (biểu đồ, luật kết hợp, phân cụm) và giảm chiều do Huấn và Việt nối thêm khi xong.
"""
from __future__ import annotations

import sys

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

from src import config, data_prep, evaluate, models


def _save(df: pd.DataFrame, name: str) -> None:
    config.TABLE_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(config.TABLE_DIR / name, index=False)


def stage_b() -> pd.DataFrame:
    raw = data_prep.load_raw()
    _save(data_prep.quality_report(raw), config.TBL_QUALITY_BEFORE)
    clean = data_prep.clean(raw)
    _save(data_prep.quality_report(clean), config.TBL_QUALITY_AFTER)
    data_prep.save_clean(clean)
    _save(_leakage_table(clean), config.TBL_LEAKAGE)
    return clean


def _leakage_table(df: pd.DataFrame) -> pd.DataFrame:
    """Bằng chứng rò rỉ: tương quan CO2-Usage_kWh; độ chính xác suy Load_Type chỉ từ Usage_kWh (train -> test)."""
    train, test = data_prep.time_split(df)
    corr = df[config.TARGET_REG].corr(df["CO2(tCO2)"])
    tree = DecisionTreeClassifier(random_state=config.SEED).fit(train[[config.TARGET_REG]], train[config.TARGET_CLS])
    acc = (tree.predict(test[[config.TARGET_REG]]) == test[config.TARGET_CLS]).mean()
    return pd.DataFrame([
        {"kiem_tra": "tuong_quan_pearson(Usage_kWh, CO2)", "gia_tri": corr,
         "ket_luan": "CO2 gan nhu suy ra duoc tu Usage_kWh: loai khoi dac trung"},
        {"kiem_tra": "accuracy_cay_chi_dung_Usage_kWh_doan_Load_Type", "gia_tri": acc,
         "ket_luan": "Load_Type khong suy ra truc tiep tu Usage_kWh"},
    ])


def stage_models(clean: pd.DataFrame) -> None:
    train, test = data_prep.time_split(clean)
    labels = config.LOAD_CLASSES

    xc_tr, xc_te = data_prep.make_features(train, test, "cls")
    clfs = models.train_classifiers(xc_tr, train[config.TARGET_CLS])
    cv_rows, test_tables, confusions = [], [], []
    for name, m in clfs.items():
        cv_rows.append({"mo_hinh": name, "tham_so_tot_nhat": str(m.best_params_), "f1_macro_cv": m.best_score_})
        pred = m.predict(xc_te)
        t = evaluate.classification_report_table(test[config.TARGET_CLS], pred, labels)
        test_tables.append(t.assign(mo_hinh=name))
        confusions.append(evaluate.top_confusions(test[config.TARGET_CLS], pred, labels).assign(mo_hinh=name))
    _save(pd.DataFrame(cv_rows), config.TBL_CLS_CV)
    _save(pd.concat(test_tables, ignore_index=True), config.TBL_CLS_TEST)
    _save(pd.concat(confusions, ignore_index=True), config.TBL_CLS_CONFUSIONS)
    _save(pd.concat([pd.DataFrame(m.cv_results_).assign(mo_hinh=n) for n, m in clfs.items()],
                    ignore_index=True)[["mo_hinh", "params", "mean_test_score", "std_test_score", "rank_test_score"]],
          config.TBL_CLS_TUNE)

    xr_tr, xr_te = data_prep.make_features(train, test, "reg")
    regs = models.train_regressors(xr_tr, train[config.TARGET_REG])
    rows, test_rows = [], []
    for name, m in regs.items():
        rows.append({"mo_hinh": name, "tham_so_tot_nhat": str(m.best_params_), "rmse_cv": -m.best_score_})
        test_rows.append({"mo_hinh": name, **evaluate.regression_report(test[config.TARGET_REG], m.predict(xr_te))})
    _save(pd.DataFrame(rows), config.TBL_REG_CV)
    _save(pd.DataFrame(test_rows), config.TBL_REG_TEST)


def main() -> int:
    clean = stage_b()
    stage_models(clean)
    print(f"Xong. Bảng ở {config.TABLE_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

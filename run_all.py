"""Chạy lại từ dữ liệu gốc đến kết quả (chủ: Phi). Các stage: B (dữ liệu), E+G (mô hình, đánh giá).

Các khối C, D, F (biểu đồ, luật kết hợp, phân cụm) và giảm chiều do Huấn và Việt nối thêm khi xong.
"""
from __future__ import annotations

import sys

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

from src import config, data_prep, evaluate, models, reduce


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
    best = max(clfs, key=lambda n: clfs[n].best_score_)  # chọn theo F1 macro CV trên train, không nhìn test
    best_pred = clfs[best].predict(xc_te)
    _save(evaluate.error_by_group(test[config.TARGET_CLS], best_pred, test["hour"]), config.TBL_CLS_ERR_HOUR)
    _save(evaluate.error_by_group(test[config.TARGET_CLS], best_pred, test["WeekStatus"]), config.TBL_CLS_ERR_DAYTYPE)
    _save(evaluate.feature_importance_table(clfs["decision_tree"], list(xc_tr.columns)), config.TBL_IMP_CLS)
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

    # Đối chứng: bỏ công suất phản kháng và hệ số công suất (Usage_kWh suy ra được từ chúng)
    xn_tr, xn_te = data_prep.make_features(train, test, "reg_no_physics")
    regs_np = models.train_regressors(xn_tr, train[config.TARGET_REG])
    _save(pd.DataFrame([{"mo_hinh": n, "tham_so_tot_nhat": str(m.best_params_), "rmse_cv": -m.best_score_,
                         **evaluate.regression_report(test[config.TARGET_REG], m.predict(xn_te))}
                        for n, m in regs_np.items()]), config.TBL_REG_NO_PHYSICS)
    _save(evaluate.feature_importance_table(regs_np["decision_tree"], list(xn_tr.columns)), config.TBL_IMP_REG)


def stage_reduce(clean: pd.DataFrame) -> None:
    """Giảm chiều và xếp hạng thuộc tính (T006, Việt): PCA khớp trên train; thông tin tương hỗ với hai đích."""
    train, test = data_prep.time_split(clean)
    x_train, x_test = data_prep.make_features(train, test, "cls")
    _, _, pca_model = reduce.pca_reduce(x_train, x_test)
    _save(reduce.pca_summary(pca_model), config.TBL_PCA_VARIANCE)
    x_reg, _ = data_prep.make_features(train, test, "reg")
    ranks = [reduce.rank_features(x_train, train[config.TARGET_CLS]).assign(dich=config.TARGET_CLS),
             reduce.rank_features(x_reg, train[config.TARGET_REG]).assign(dich=config.TARGET_REG)]
    _save(pd.concat(ranks, ignore_index=True), config.TBL_FEATURE_RANK)


def stage_adjust(clean: pd.DataFrame) -> None:
    """Thử điều chỉnh phân lớp (cây quyết định): trọng số lớp, đặc trưng trễ, cả hai. Báo trước/sau trên cùng test."""
    lagged = data_prep.add_lag_features(clean)
    train, test = data_prep.time_split(lagged)
    base_tr, base_te = data_prep.make_features(train, test, "cls")
    lag = data_prep.lag_feature_names()
    variants = {
        "goc": (base_tr, base_te, None),
        "class_weight": (base_tr, base_te, config.ADJUST_CLASS_WEIGHT),
        "dac_trung_tre": (base_tr.join(train[lag]), base_te.join(test[lag]), None),
        "ca_hai": (base_tr.join(train[lag]), base_te.join(test[lag]), config.ADJUST_CLASS_WEIGHT),
    }
    rows = []
    for name, (xtr, xte, cw) in variants.items():
        m = models.tune_tree_variant(xtr, train[config.TARGET_CLS], cw)
        pred = m.predict(xte)
        rep = evaluate.classification_report_table(test[config.TARGET_CLS], pred, config.LOAD_CLASSES).set_index("lop")
        rows.append({"bien_the": name, "tham_so_tot_nhat": str(m.best_params_), "f1_macro_cv": m.best_score_,
                     "f1_macro_test": rep.loc["macro_avg", "f1"], "accuracy_test": rep.loc["accuracy", "f1"]})
    _save(pd.DataFrame(rows), config.TBL_CLS_ADJUST)


def main() -> int:
    clean = stage_b()
    stage_models(clean)
    stage_reduce(clean)
    stage_adjust(clean)
    print(f"Xong. Bảng ở {config.TABLE_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

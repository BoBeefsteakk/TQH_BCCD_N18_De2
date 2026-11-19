"""Kiểm data_prep, models, evaluate (chủ: Phi) trên dữ liệu tổng hợp nhỏ, không cần tệp UCI."""
import numpy as np
import pandas as pd
import pytest

from src import config, data_prep, evaluate, models


def _fake(n=240):
    rng = np.random.default_rng(config.SEED)
    t = pd.date_range("2018-01-01 00:15", periods=n, freq="15min")
    usage = rng.gamma(2.0, 10.0, n)
    return pd.DataFrame({
        "date": t.strftime(config.DATE_FORMAT),
        "Usage_kWh": usage,
        "Lagging_Current_Reactive.Power_kVarh": usage * 0.5 + rng.random(n),
        "Leading_Current_Reactive_Power_kVarh": rng.random(n),
        "CO2(tCO2)": usage * 0.0004,
        "Lagging_Current_Power_Factor": rng.uniform(50, 100, n),
        "Leading_Current_Power_Factor": rng.uniform(90, 100, n),
        "NSM": ((t.hour * 3600) + t.minute * 60).to_numpy(),
        "WeekStatus": "Weekday",
        "Day_of_week": t.day_name().to_numpy(),
        "Load_Type": np.where(usage < 10, "Light_Load", np.where(usage < 25, "Medium_Load", "Maximum_Load")),
    })


def test_clean_keeps_order_and_adds_features():
    raw = _fake()
    out = data_prep.clean(raw)
    assert len(out) == len(raw)
    assert out["date"].is_monotonic_increasing
    assert {"hour", "month", "is_outlier"} <= set(out.columns)


def test_clean_drops_duplicates_and_nonsense():
    raw = _fake()
    bad = raw.iloc[[0]].copy()
    bad["Lagging_Current_Power_Factor"] = 150.0
    out = data_prep.clean(pd.concat([raw, raw.iloc[[5]], bad], ignore_index=True))
    assert len(out) == len(raw)


def test_time_split_is_ordered_and_sized():
    out = data_prep.clean(_fake())
    train, test = data_prep.time_split(out)
    assert len(train) + len(test) == len(out)
    assert abs(len(test) / len(out) - config.TEST_FRACTION) < 0.01
    assert train["date"].max() < test["date"].min()


def test_features_exclude_leaky_and_targets():
    out = data_prep.clean(_fake())
    train, test = data_prep.time_split(out)
    for task in ("cls", "reg"):
        xtr, xte = data_prep.make_features(train, test, task)
        assert list(xtr.columns) == list(xte.columns)
        assert not (set(config.LEAKY_COLS) | {config.TARGET_CLS, config.TARGET_REG}) & set(xtr.columns)


def test_models_cover_config_and_beat_chance():
    out = data_prep.clean(_fake(400))
    train, test = data_prep.time_split(out)
    x_tr, x_te = data_prep.make_features(train, test, "cls")
    clfs = models.train_classifiers(x_tr, train[config.TARGET_CLS])
    assert set(clfs) == set(config.CLASSIFIER_GRID) and len(clfs) >= 3
    regs = models.train_regressors(*data_prep.make_features(train, test, "reg")[:1], train[config.TARGET_REG])
    assert set(regs) == set(config.REGRESSOR_GRID)


def test_tune_rejects_unknown_model():
    out = data_prep.clean(_fake())
    x, _ = data_prep.make_features(out, out, "cls")
    with pytest.raises((ValueError, KeyError)):
        models.tune("khong_ton_tai", x, out[config.TARGET_CLS])


def test_classification_report_table_and_confusions():
    y = ["a", "a", "b", "b", "b", "c"]
    p = ["a", "b", "b", "b", "a", "c"]
    t = evaluate.classification_report_table(y, p, ["a", "b", "c"])
    assert t.loc[t.lop == "c", "f1"].item() == 1.0
    assert t.loc[t.lop == "accuracy", "f1"].item() == pytest.approx(4 / 6)
    c = evaluate.top_confusions(y, p, ["a", "b", "c"])
    assert c.so_luong.iloc[0] == 1 and c.so_luong.sum() == 2


def test_regression_report_perfect_and_offset():
    y = np.array([1.0, 2.0, 3.0])
    assert evaluate.regression_report(y, y) == {"mae": 0.0, "rmse": 0.0, "r2": 1.0}
    r = evaluate.regression_report(y, y + 1)
    assert r["mae"] == pytest.approx(1.0) and r["rmse"] == pytest.approx(1.0)


def test_reg_no_physics_drops_reactive_and_pf():
    out = data_prep.clean(_fake())
    train, test = data_prep.time_split(out)
    xtr, _ = data_prep.make_features(train, test, "reg_no_physics")
    assert not set(config.REG_NO_PHYSICS_COLS) & set(xtr.columns)
    assert "NSM" in xtr.columns


def test_lag_features_look_backward_only():
    out = data_prep.add_lag_features(data_prep.clean(_fake()))
    col = config.LAG_COLS[0]
    assert out[f"{col}_hieu1"].iloc[0] == 0.0
    assert out[f"{col}_tb{config.LAG_WINDOW}"].iloc[0] == out[col].iloc[0]
    assert out[f"{col}_hieu1"].iloc[5] == pytest.approx(out[col].iloc[5] - out[col].iloc[4])
    assert len(data_prep.lag_feature_names()) == 2 * len(config.LAG_COLS)

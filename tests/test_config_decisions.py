"""Kiểm các quyết định đã chốt ngày 17/11/2026 (docs/CONVENTIONS.md mục 6)."""
from src import config


def test_classifiers_meet_spec():
    assert len(config.CLASSIFIER_GRID) >= 3  # đề, khối E của Đề 2: ít nhất 3 mô hình phân lớp
    assert all(isinstance(v, dict) for v in config.CLASSIFIER_GRID.values())
    assert any(grid for grid in config.CLASSIFIER_GRID.values())  # đề: chỉnh ít nhất một tham số


def test_regressor_defined():
    assert config.REGRESSOR_GRID  # đề, khối E: hồi quy Usage_kWh


def test_metrics_and_policies():
    assert config.PRIMARY_METRIC_CLS == "f1_macro"
    assert config.PRIMARY_METRIC_REG == "rmse"
    assert config.OUTLIER_POLICY in {"flag", "drop"}
    assert config.SAMPLING == "none"


def test_hour_bins_cover_a_day():
    e = config.HOUR_BIN_EDGES
    assert list(e) == sorted(e) and e[0] == 0 and e[-1] == 24


def test_discretize_levels_and_seed():
    assert len(config.DISCRETIZE_LEVELS) == 3
    assert config.SEED == 4759 and config.N_KMEANS_INIT >= 1

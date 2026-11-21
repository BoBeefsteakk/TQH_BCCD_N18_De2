"""Kiểm src/reduce.py (chủ: Việt, T006) trên dữ liệu tổng hợp nhỏ, không cần tệp UCI."""
import numpy as np
import pandas as pd

from src import config, reduce


def _fake(n=400):
    rng = np.random.default_rng(config.SEED)
    signal = rng.normal(size=n)
    x = pd.DataFrame({
        "tin_hieu": signal,
        "nhieu": rng.normal(size=n),
        "lon": rng.uniform(0, 85500, n),  # thang đo lớn như NSM
        "one_hot": rng.integers(0, 2, n).astype(float),
    })
    y_cls = pd.Series(np.where(signal > 0, "Medium_Load", "Light_Load"))
    y_reg = pd.Series(3 * signal + rng.normal(scale=0.1, size=n))
    return x, y_cls, y_reg


def test_pca_keeps_variance_and_shapes():
    x, _, _ = _fake()
    x_train, x_test = x.iloc[:300], x.iloc[300:]
    train_z, test_z, model = reduce.pca_reduce(x_train, x_test)
    assert train_z.shape[0] == len(x_train) and test_z.shape[0] == len(x_test)
    assert train_z.shape[1] == test_z.shape[1] <= x.shape[1]
    assert reduce.pca_summary(model)["ti_le_luy_ke"].iloc[-1] >= config.PCA_VARIANCE


def test_pca_fits_on_train_only():
    x, _, _ = _fake()
    x_train, x_test = x.iloc[:300], x.iloc[300:]
    _, _, model = reduce.pca_reduce(x_train, x_test)
    np.testing.assert_allclose(model.named_steps["scale"].mean_, x_train.mean().to_numpy())


def test_rank_features_puts_signal_first():
    x, y_cls, y_reg = _fake()
    for y in (y_cls, y_reg):
        table = reduce.rank_features(x, y)
        assert list(table.columns) == ["feature", "score"]
        assert set(table["feature"]) == set(x.columns)
        assert table["feature"].iloc[0] == "tin_hieu"
        assert table["score"].is_monotonic_decreasing


def test_rank_features_is_reproducible():
    x, y_cls, _ = _fake()
    pd.testing.assert_frame_equal(reduce.rank_features(x, y_cls), reduce.rank_features(x, y_cls))

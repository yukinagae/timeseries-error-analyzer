import pytest

from tserror.metrics import root_mean_squared_error


def test_rmse():
    y_true = [1, 2, 3]
    y_pred = [2, 3, 4]
    rmse = root_mean_squared_error(y_true, y_pred)
    print(rmse)
    assert rmse == pytest.approx(1, abs=1e-5)

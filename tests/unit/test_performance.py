import pandas as pd
import pytest

from toy_example.performance import *


@pytest.fixture
def y_true():
    return pd.Series([1, 1, 1, 0, 0, 0])


@pytest.fixture
def y_pred():
    return pd.Series([1, 1, 1, 1, 1, 1])


@pytest.fixture
def performance_result(y_true, y_pred) -> PerformanceData:
    return get_performance_metrics(y_true, y_pred)


def test_get_performance_metrics(performance_result):

    assert type(performance_result) == PerformanceData


# This is hacky, the correct version is in the link https://realpython.com/lessons/mocking-print-unit-tests/
def test_print_performance_metrics_runs(performance_result):
    assert print_performance_metrics(performance_result)

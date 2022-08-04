from toy_example.performance import *
import pandas as pd

y_true = pd.Series([1,1,1,0,0,0])
y_pred = pd.Series([1,1,1,1,1,1])
performance_result = get_performance_metrics(y_true,y_pred)


def test_get_performance_metrics():

    pd.testing.assert_series_equal(performance_result.true_class_balance,pd.Series([0.5,0.5]))
    # add further tests

    
# This is hacky, the correct version is in the link https://realpython.com/lessons/mocking-print-unit-tests/
def test_print_performance_metrics_runs(): 
    assert print_performance_metrics(performance_result)
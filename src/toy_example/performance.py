from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from dataclasses import dataclass
import pandas as pd


@dataclass
class PerformanceData:
    true_class_balance: pd.Series
    accuracy: float
    F1: float
    precision: float
    recall: float


def get_performance_metrics(y_true, y_pred) -> PerformanceData:
    true_class_balance = y_true.value_counts() / y_true.shape[0]
    accuracy = accuracy_score(y_true, y_pred)
    F1 = f1_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    return PerformanceData(true_class_balance, accuracy, F1, precision, recall)


def print_performance_metrics(performance_data: PerformanceData):

    print("True class balance:")
    print(performance_data.true_class_balance)
    print("")
    print(f"Accuracy score: {performance_data.accuracy}")
    print("")
    print(f"F1 score: {performance_data.F1}")
    print("")
    print(f"Precision score: {performance_data.precision}")
    print("")
    print(f"Recall score: {performance_data.recall}")

    return True

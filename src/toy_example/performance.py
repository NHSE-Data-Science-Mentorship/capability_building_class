from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def print_performance_metrics(y_true, y_pred):
    print(f"True class balance:")
    print(y_true.value_counts()/y_true.shape[0])
    print("")
    print(f"Accuracy score: {accuracy_score(y_true, y_pred)}")
    print("")
    print(f"F1 score: {f1_score(y_true, y_pred)}")
    print("")
    print(f"Precision score: {precision_score(y_true, y_pred)}")
    print("")
    print(f"Recall score: {recall_score(y_true, y_pred)}")

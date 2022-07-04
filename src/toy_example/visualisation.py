import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import auc


def plot_roc(y_test, y_score):
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
    roc_display.ax_.set_title(f"AUC = {auc(fpr, tpr):.2f}")
    plt.show()

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import auc
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def plot_roc(y_test, y_score):
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
    roc_display.ax_.set_title(f"AUC = {auc(fpr, tpr):.2f}")
    plt.show()


def plot_confusion_matrix(y_true, y_pred, normalize="true"):
    cm = ConfusionMatrixDisplay(
        confusion_matrix(y_true, y_pred, normalize=normalize)
    ).plot()
    cm.ax_.set_title("Confusion Matrix for predictions")
    plt.show()


def visualise_data(X, y):
    fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    sex_1_not_admitted = (
        X.loc[(y["admitted"] == 0) & (X["sex"] == "1"), "age_at_arrival"]
        .value_counts()
        .sort_index()
    )

    sex_1_admitted = (
        X.loc[(y["admitted"] == 1) & (X["sex"] == "1"), "age_at_arrival"]
        .value_counts()
        .sort_index()
    )

    sex_2_not_admitted = (
        X.loc[(y["admitted"] == 0) & (X["sex"] == "2"), "age_at_arrival"]
        .value_counts()
        .sort_index()
    )

    sex_2_admitted = (
        X.loc[(y["admitted"] == 1) & (X["sex"] == "2"), "age_at_arrival"]
        .value_counts()
        .sort_index()
    )

    axs[0].bar(
        sex_1_not_admitted.index,
        sex_1_not_admitted.values,
        color="blue",
        alpha=0.5,
        label="Not Admitted",
    )

    axs[0].bar(
        sex_1_admitted.index,
        sex_1_admitted.values,
        color="red",
        alpha=0.5,
        label="Admitted",
    )

    axs[0].set_ylabel("Number of attendances", fontsize=12)
    axs[0].set_title("Sex 1", fontsize=16)

    axs[0].legend(fontsize=12)

    axs[1].bar(
        sex_2_not_admitted.index,
        sex_2_not_admitted.values,
        color="blue",
        alpha=0.5,
        label="Not Admitted",
    )

    axs[1].bar(
        sex_2_admitted.index,
        sex_2_admitted.values,
        color="red",
        alpha=0.5,
        label="Admitted",
    )

    axs[1].set_ylabel("Number of attendances", fontsize=12)
    axs[1].set_title("Sex 2", fontsize=16)

    axs[1].legend(fontsize=12)

    plt.show()

    return fig, axs

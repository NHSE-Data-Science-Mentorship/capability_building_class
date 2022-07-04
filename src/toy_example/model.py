from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


class ECDSAdmissionsClassifier():

    def __init__(
        self,
        preprocessor=None,
        classifier=LogisticRegression(),
    ):
        if preprocessor is not None:
            self.preprocessor = preprocessor
        else:
            numeric_features = ["age_at_arrival"]
            numeric_transformer = StandardScaler()

            categorical_features = ["sex"]
            categorical_transformer = OneHotEncoder(handle_unknown="ignore")

            self.preprocessor = ColumnTransformer(
                transformers=[
                    ("num", numeric_transformer, numeric_features),
                    ("cat", categorical_transformer, categorical_features),
                ]
            )

        self.classifier = classifier

        self.model = Pipeline(
            steps=[
                ("preprocessor", self.preprocessor),
                ("classifier", self.classifier)
            ]
        )

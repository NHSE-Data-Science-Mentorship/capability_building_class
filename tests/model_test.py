from sklearn.linear_model import LogisticRegression

from toy_example.model import ModelPipelineWrapper


def test_ModelPipelineWrapper():
    # This is redundant, don't test python
    assert ModelPipelineWrapper(model=LogisticRegression).model == LogisticRegression

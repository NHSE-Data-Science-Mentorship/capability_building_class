import pandas as pd
import pytest

from toy_example.preprocessing import *
from toy_example.datasets import FoundrySQLWrapper


global_ecds_df = pd.DataFrame(
    {
        "sex": ["1", "1", "2", "3"],
        "age_at_arrival": [int(x) for x in [5, 40, 90, 12]],
        "admitted": [True, True, False, False],
    }
)


@pytest.fixture
def ecds_test_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "sex": ["1", "1", "2", "3"],
            "age_at_arrival": [int(x) for x in [5, 40, 90, 12]],
            "admitted": [True, True, False, False],
        }
    )


# Separate named func for each assert, bundle in class?
# tag use vs edge case
# Think about what test should do with empty dataframe
def test_split_features_targets(ecds_test_df) -> None:

    feature_df, target_df = split_features_targets(ecds_test_df)
    assert len(feature_df) == len(target_df)
    assert not set(feature_df.columns).intersection(set(target_df.columns))


def test_clean_ecds(mocker) -> None:
    def no_connection_init():
        pass

    def fake_ecds():
        return pd.DataFrame(
            {
                "sex": ["1", "1", "2", "3"],
                "age_at_arrival": [int(x) for x in [5, 40, 90, 12]],
                "admitted": [True, True, False, False],
            }
        )

    # Arrange
    mocker.patch("toy_example.datasets.FoundrySQLWrapper.__init__", no_connection_init)
    mocker.patch("toy_example.datasets.FoundrySQLWrapper.get_ecds", fake_ecds)
    foundry_wrapper = FoundrySQLWrapper
    ecds_test = foundry_wrapper.get_ecds()

    assert "3" not in clean_ecds(ecds_test)["sex"].unique()
    assert clean_ecds(ecds_test)["sex"].dtype == "category"

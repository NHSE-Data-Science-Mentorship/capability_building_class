import pandas as pd
import pytest

from toy_example.preprocessing import *

# make a fixture
ecds_test = pd.DataFrame(
    {
        "sex": ["1", "1", "2", "3"],
        "age_at_arrival": [int(x) for x in [5, 40, 90, 12]],
        "admitted": [True, True, False, False],
    }
)


def test_clean_ecds() -> None:
    assert "3" not in clean_ecds(ecds_test)["sex"].unique()
    assert clean_ecds(ecds_test)["sex"].dtype == "category"


# Separate named func for each assert, bundle in class?
# tag use vs edge case
# Think about what test should do with empty dataframe
def test_split_features_targets() -> None:

    feature_df, target_df = split_features_targets(ecds_test)
    assert len(feature_df) == len(target_df)
    assert not set(feature_df.columns).intersection(set(target_df.columns))

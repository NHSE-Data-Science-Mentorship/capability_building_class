import pytest
import numpy as np
import pandas as pd
from toy_example.datasets import (
    FoundrySQLWrapper,
    validate_ecds_df,
    validate_acute_type_one_trusts,
)


@pytest.fixture
def foundry_wrapper():
    return FoundrySQLWrapper()


@pytest.fixture
def acute_type_one_trusts(foundry_wrapper):
    return foundry_wrapper.get_acute_type_one_trusts()


@pytest.fixture
def ecds_df(foundry_wrapper, acute_type_one_trusts):
    return foundry_wrapper.get_ecds(location_ids=acute_type_one_trusts)


def test_acute_trusts_sql(acute_type_one_trusts):
    validate_acute_type_one_trusts(acute_type_one_trusts)


def test_ecds(acute_type_one_trusts, ecds_df):
    validate_ecds_df(ecds_df)
    # assert sorted(list(acute_type_one_trusts)) == sorted(list(ecds_df["der_provider_code"].unique()))
    assert all(
        [
            trust_code in list(acute_type_one_trusts)
            for trust_code in ecds_df["der_provider_code"].unique()
        ]
    )

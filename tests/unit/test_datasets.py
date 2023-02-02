# from toy_example.datasets import FoundrySQLWrapper
# import pytest
# import pandas as pd

# # from mock import patch


# # how to deal with connections/things you don't want to run at test time in the __init__
# class TestFoundrySQLWrapper(FoundrySQLWrapper):
#     def __init__(self):
#         self.conn = "Connection"


# # Alternative:
# # @pytest.fixture
# # def TestFoundrySQLWrapper():
# #     def __init__(self):
# #         self.conn = "Connection"

# #     with patch.object(FoundrySQLWrapper, "__init__", __init__):
# #         return FoundrySQLWrapper


# @pytest.fixture
# def location_df():
#     return pd.DataFrame({"location_id": ["RAL", "RH8", "RJ2"]})


# def test_FoundrySQLWrapper_init():  # TestFoundrySQLWrapper):

#     test_class = TestFoundrySQLWrapper()
#     # garbage test, just to show how you can override init
#     # print(type(TestFoundrySQLWrapper))
#     assert type(test_class) == TestFoundrySQLWrapper

#     # assert TestFoundrySQLWrapper == FoundrySQLWrapper


# def test_get_acute_type_one_trusts():
#     pass


# def test_get_ecds():
#     pass

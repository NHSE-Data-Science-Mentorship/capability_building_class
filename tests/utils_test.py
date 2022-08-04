from toy_example.utils import *
import numpy as np
import pytest


def test_list_to_sql_array_good():
    my_list = ["a", "b", "c"]
    assert list_to_sql_array(my_list) == "('a', 'b', 'c')"


def test_list_to_sql_array_bad():
    my_bad_list = [1, "b", np.nan]

    with pytest.raises(TypeError):
        list_to_sql_array(my_bad_list)

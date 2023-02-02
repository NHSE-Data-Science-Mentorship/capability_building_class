import ast
import numpy as np
import pytest
from hypothesis import given,example, strategies as st
from toy_example.utils import list_to_sql_array


def test_list_to_sql_array_good_simple():

    # Arrange
    test_input = ["a", "b", "c"]
    expected = "('a', 'b', 'c')"

    # Act
    result = list_to_sql_array(test_input)

    # Assert
    assert result == expected

def test_list_to_sql_array_bad():
    my_bad_list = [1, "b", np.nan]

    with pytest.raises(TypeError):
        list_to_sql_array(my_bad_list)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["a", "b", "c"], "('a', 'b', 'c')"),
        (["d", "e", "f"], "('d', 'e', 'f')"),
        ([""],"('')"),

    ],
)
def test_list_to_sql_array_good(test_input, expected):

    assert list_to_sql_array(test_input) == expected


@given(st.lists(st.text()))
@example(["a", "b", "c"])
def test_list_to_sql_reversible(input_list):

    reverse = ast.literal_eval(
        (list_to_sql_array(input_list).replace("(", "").replace(")", ""))
    )
    assert reverse == input_list

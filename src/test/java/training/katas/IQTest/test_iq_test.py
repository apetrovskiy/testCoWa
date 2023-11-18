# test.assert_equals(iq_test("2 4 7 8 10"),3)
# test.assert_equals(iq_test("1 2 2"), 1)
import pytest
from typing import List
from src.main.java.training.katas.IQTest.iq_test import iq_test


test_data = [([2, 4, 7, 8, 10], 3), ([1, 2, 2], 1)]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_iq_test(input_array: List[int], expected_result: int):
    assert expected_result == iq_test(input_array)

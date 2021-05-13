'''
import codewars_test as test

a = [12, 15]
test.assert_equals(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])

a = [15, 21, 24, 30, 45]
test.assert_equals(sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]])
'''

import pytest
from typing import List
from src.main.java.training.katas.SumByFactors.sum_by_factors \
    import sum_for_list


test_data = [
    ([], [])
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_sum_by_factors(input_array: List[int], expected_result: List[List[int]]):
    assert expected_result == sum_for_list(input_array)

'''
import codewars_test as test
from solution import move_zeros

@test.it("Basic tests")
def youarecute():
    test.assert_equals(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    test.assert_equals(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    test.assert_equals(move_zeros([0, 0]), [0, 0])
    test.assert_equals(move_zeros([0]), [0])
    test.assert_equals(move_zeros([]), [])
'''

import pytest
from typing import List
from src.main.java.training.katas.MovingZerosToTheEnd. \
    moving_zeros_to_the_end import move_zeros


test_data = [
    ([1, 0, 1, 2, 0, 1, 3], [1, 1, 2, 1, 3, 0, 0]),
    ([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
]


@pytest.mark.parametrize("input_array,expected_result", test_data)
def test_moving_zeros_to_the_end(
        input_array: List[int], expected_result: List[int]):
    assert expected_result == move_zeros(input_array)

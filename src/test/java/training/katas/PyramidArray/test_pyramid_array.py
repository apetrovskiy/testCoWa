"""
test.assert_equals(pyramid(0), [])
test.assert_equals(pyramid(1), [[1]])
test.assert_equals(pyramid(2), [[1], [1, 1]])
test.assert_equals(pyramid(3), [[1], [1, 1], [1, 1, 1]])
"""

import pytest
from typing import List
from src.main.java.training.katas.PyramidArray.pyramid_array import pyramid


test_data = [(0, []), (1, [[1]]), (2, [[1], [1, 1]]), (3, [[1], [1, 1], [1, 1, 1]])]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_pyramid_array(input: int, expected_result: List[List[int]]):
    assert expected_result == pyramid(input)

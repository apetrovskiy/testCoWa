# import codewars_test as test
# from solution import row_sum_odd_numbers

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(row_sum_odd_numbers(1), 1)
#         test.assert_equals(row_sum_odd_numbers(2), 8)
#         test.assert_equals(row_sum_odd_numbers(13), 2197)
#         test.assert_equals(row_sum_odd_numbers(19), 6859)
#         test.assert_equals(row_sum_odd_numbers(41), 68921)

import pytest
from src.main.java.training.katas.SumOfOddNumbers.sum_of_odd_numbers \
    import row_sum_odd_numbers


test_data = [
    (1, 1),
    (2, 8),
    (13, 2197),
    (19, 6859),
    (41, 68921)
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_row_sum_odd_numbers(input: int, expected_result: int):
    assert expected_result == row_sum_odd_numbers(input)

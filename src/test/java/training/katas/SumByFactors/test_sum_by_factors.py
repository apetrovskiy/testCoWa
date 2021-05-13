'''
import codewars_test as test

a = [12, 15]
test.assert_equals(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])

a = [15, 21, 24, 30, 45]
test.assert_equals(sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]])
'''

import python


test_data = [
    ()
]

@pytest.mark.parametrize("input,expected_result",test_data)
def test_sum_by_factors(input,expected_result):
    assert expec == sum_for_list(input)
'''
test.assert_equals(pyramid(0), [])
test.assert_equals(pyramid(1), [[1]])
test.assert_equals(pyramid(2), [[1], [1, 1]])
test.assert_equals(pyramid(3), [[1], [1, 1], [1, 1, 1]])
'''

import pytest

test_data = [
    
]

@pytest.mark.parametrize("input,expected_reslult",test_data)
def test_pyramid_array(input:int,expected_result:List[int]):
    assert expected_result = 
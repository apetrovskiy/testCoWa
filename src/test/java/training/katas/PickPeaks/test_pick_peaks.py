import pytest


test_data = [
    ([1,2,3,6,4,1,2,3,2,1], {"pos":[3,7], "peaks":[6,3]}),
([3,2,3,6,4,1,2,3,2,1,2,3], {"pos":[3,7], "peaks":[6,3]}),
([3,2,3,6,4,1,2,3,2,1,2,2,2,1], {"pos":[3,7,10], "peaks":[6,3,2]}),
([2,1,3,1,2,2,2,2,1], {"pos":[2,4], "peaks":[3,2]}),
([2,1,3,1,2,2,2,2], {"pos":[2], "peaks":[3]}),
([2,1,3,2,2,2,2,5,6], {"pos":[2], "peaks":[3]}),
([2,1,3,2,2,2,2,1], {"pos":[2], "peaks":[3]}),
([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3], {"pos":[2,7,14,20], "peaks":[5,6,5,5]}),
([],{"pos":[],"peaks":[]}),
([1,1,1,1],{"pos":[],"peaks":[]})
]


@pytest.mark.parametrize("input,expected_result",test_data)
def test_pick_peaks(input:List[int],expected_result:Dict):
    assert expected_result == pick_peaks(input)


'''
Test.assert_equals(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})
Test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})
Test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})
Test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})
Test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2]), {"pos":[2], "peaks":[3]})
Test.assert_equals(pick_peaks([2,1,3,2,2,2,2,5,6]), {"pos":[2], "peaks":[3]})
Test.assert_equals(pick_peaks([2,1,3,2,2,2,2,1]), {"pos":[2], "peaks":[3]})
Test.assert_equals(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
Test.assert_equals(pick_peaks([]),{"pos":[],"peaks":[]})
Test.assert_equals(pick_peaks([1,1,1,1]),{"pos":[],"peaks":[]})
'''

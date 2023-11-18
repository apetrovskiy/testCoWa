from src.main.java.training.katas.NestingStructureComparison.nesting_structure_comparison import (
    same_structure_as,
)
from typing import List
import pytest


test_data = [
    ([1, [1, 1]], [2, [2, 2]], True),
    ([1, [1, 1]], [[2, 2], 2], False),
    ([], 1, False),
    ([1, "[", "]"], ["[", "]", 1], True),
]


@pytest.mark.parametrize("original,other,expected_result", test_data)
def test_nesting_structure_comparison(
    original: List[int], other: List[int], expected_result: bool
):
    assert expected_result == same_structure_as(original, other)


"""
# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""

"""
Test.assert_equals(same_structure_as(
    [1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
Test.assert_equals(same_structure_as(
    [1,[1,1]],[[2,2],2]),
False, "[1,[1,1]] not same as [[2,2],2]")Test.assert_equals(
    same_structure_as([1,[1,1]],[2,[2,2]]),
    True, "[1,[1,1]]
    same as [2,[2,2]]")
Test.assert_equals(same_structure_as(
    [1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")
"""

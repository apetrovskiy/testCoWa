"""
def _test(cases):
    for _in, _out in cases:
        test.assert_equals(triangle(_in), _out)


test.describe('Insane Coloured Triangles')
basic_cases = [
    ['B', 'B'],
    ['GB', 'R'],
    ['RRR', 'R'],
    ['RGBG', 'B'],
    ['RBRGBRB', 'G'],
    ['RBRGBRBGGRRRBGBBBGG', 'G']
]
test.it('Basic Tests')
_test(basic_cases)
"""

import pytest
from src.main.java.training.katas.InsaneColouredTriangles.insane_coloured_triangles import (
    triangle,
)


test_data = basic_cases = [
    ("B", "B"),
    ("GB", "R"),
    ("RRR", "R"),
    ("RGBG", "B"),
    ("RBRGBRB", "G"),
    ("RBRGBRBGGRRRBGBBBGG", "G"),
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_insane_coloured_triangles(input: str, expected_result: str):
    assert expected_result == triangle(input)

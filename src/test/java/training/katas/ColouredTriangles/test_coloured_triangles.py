'''
test.assert_equals(triangle('GB'), 'R')
test.assert_equals(triangle('RRR'), 'R')
test.assert_equals(triangle('RGBG'), 'B')
test.assert_equals(triangle('RBRGBRB'), 'G')
test.assert_equals(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')
test.assert_equals(triangle('B'), 'B')
'''

import pytest
from src.main.java.training.katas.ColouredTriangles.coloured_triangles \
    import get_color, triangle


test_data = [
    ("RRGBRGBB", "G"),
    ('GB', 'R'),
    ('RRR', 'R'),
    ('RGBG', 'B'),
    ('RBRGBRB', 'G'),
    ('RBRGBRBGGRRRBGBBBGG', 'G'),
    ('B', 'B')
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_coloured_triangles(input: str, expected_result: str):
    assert expected_result == triangle(input)


test_data_single_color = [
    ('R', 'R', 'R'),
    ('G', 'G', 'G'),
    ('B', 'B', 'B'),
    ('R', 'G', 'B'),
    ('G', 'B', 'R'),
    ('B', 'R', 'G')
]


@pytest.mark.parametrize(
    "color1,color2,expected_result", test_data_single_color)
def test_single_color(color1: str, color2: str, expected_result: str):
    assert expected_result == get_color(color1, color2)

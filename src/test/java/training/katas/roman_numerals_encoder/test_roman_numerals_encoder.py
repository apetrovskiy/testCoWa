from src.main.java.training.katas.roman_numerals_encoder.roman_numerals_encoder import (
    solution_roman_numerals_encoder,
)
import pytest

# import ptest


test_data = [
    (1, "I"),
    (4, "IV"),
    (6, "VI"),
    (14, "XIV"),
    (21, "XXI"),
    (89, "LXXXIX"),
    (91, "XCI"),
    (984, "CMLXXXIV"),
    (1000, "M"),
    (1889, "MDCCCLXXXIX"),
    (1989, "MCMLXXXIX"),
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_roman_numerals_encoder(input: int, expected_result: str):
    # test.assert_equals(
    # solution_roman_numerals_encoder(input), expected_result)
    assert solution_roman_numerals_encoder(input) == expected_result

from src.main.java.training.katas.exes_and_ohs.exes_and_ohs import xo
import pytest


test_data = [
    ("ooxx", True),
    ("xooxx", False),
    ("ooxXm", True),
    ("zpzpzpp", True),
    ("zzoo", False),
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_xo(input: str, expected_result: bool):
    assert xo(input) is expected_result

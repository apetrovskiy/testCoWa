# test.assert_equals(evaporator(10, 10, 10), 22)
import pytest
from src.main.java.training.katas.DeodorantEvaporator.deodorant_evaporator import (
    evaporator,
)


test_data = [(10, 10, 5, 29), (10, 10, 10, 22), (100, 5, 5, 59)]


@pytest.mark.parametrize("content,evap_per_day,threshold,expected_result", test_data)
def test_deodorant_evaporator(
    content: int, evap_per_day: int, threshold: int, expected_result: int
):
    assert expected_result == evaporator(content, evap_per_day, threshold)

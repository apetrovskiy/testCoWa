from src.main.java.training.katas.HumanReadableDurationFormat.solution import format_duration
import pytest


test_data = [
    (1, "1 second"),
    (62, "1 minute and 2 seconds"),
    (120, "2 minutes"),
    (3600, "1 hour"),
    (3662, "1 hour, 1 minute and 2 seconds")
]


@ pytest.mark.parametrize("seconds,expected_result", test_data)
def test_human_readable_duration_format(seconds: int, expected_result: str):
    assert expected_result == format_duration(seconds)


'''
est.assert_equals(format_duration(1), "1 second")
test.assert_equals(format_duration(62), "1 minute and 2 seconds")
test.assert_equals(format_duration(120), "2 minutes")
test.assert_equals(format_duration(3600), "1 hour")
test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
'''

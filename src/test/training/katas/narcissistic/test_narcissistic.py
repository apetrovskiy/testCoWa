import pytest

from src.main.training.katas.narcissistic.narcissistic import narcissistic


def check_7():
    print("==============")
    assert narcissistic(7)


def check_371():
    assert narcissistic(371)


def check_122():
    assert narcissistic(122)


def check_4887():
    assert narcissistic(4887)

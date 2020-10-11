from src.main.java.training.katas.narcissistic.code import narcissistic


def test_7():
    assert narcissistic(7) is True


def test_371():
    assert narcissistic(371) is True


def test_122():
    assert narcissistic(122) is False


def test_4887():
    assert narcissistic(4887) is False

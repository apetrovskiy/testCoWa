def check_7():
    print("============== 777 ====================")
    from src.main.training.katas.narcissistic.code import narcissistic
    assert narcissistic(7) is True


def check_371():
    from src.main.training.katas.narcissistic.code import narcissistic
    assert narcissistic(371) is True


def check_122():
    from src.main.training.katas.narcissistic.code import narcissistic
    assert narcissistic(122) is False


def check_4887():
    from src.main.training.katas.narcissistic.code import narcissistic
    assert narcissistic(4887) is False

from src.main.training.katas.disemvowel_trolls.code import disemvowel


def test_disemvowel_trolls():
    assert disemvowel("abcdef") == "bcdf"

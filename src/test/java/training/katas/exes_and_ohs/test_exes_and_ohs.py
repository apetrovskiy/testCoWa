from src.main.java.training.katas.exes_and_ohs.code import xo


def test_xo():
    assert xo("ooxx") is True
    assert xo("xooxx") is False
    assert xo("ooxXm") is True
    assert xo("zpzpzpp") is True
    assert xo("zzoo") is False

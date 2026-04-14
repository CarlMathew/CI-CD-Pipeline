from app.calculator import add, minus, multiplaction, division


def test_add():
    assert add(2,4) == 6


def test_minus():
    assert minus(4, 2) == 2



def test_multiplaction():
    assert multiplaction(5, 5) == 25


def test_division():
    assert division(10, 2) == 5

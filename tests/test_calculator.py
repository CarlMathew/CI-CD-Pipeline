from app.calculator import add, minus, multiplaction


def test_add():
    assert add(2,4) == 6


def test_minus():
    assert minus(4, 2) == 2



def test_multiplaction():
    assert multiplaction(5, 5) == 25
from calculator import subtract


def test_subtract():
    assert subtract(5, 3) == 2


def test_subtract_zero():
    assert subtract(7, 0) == 7


def test_subtract_negative():
    assert subtract(-4, 1) == -5

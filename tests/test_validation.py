
from validation import validate_order


def test_valid_order():
    assert validate_order(100, 2) is True


def test_negative_amount():
    assert validate_order(-50, 2) is False


def test_zero_quantity():
    assert validate_order(100, 0) is False

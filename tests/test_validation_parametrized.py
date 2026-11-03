
import pytest
from validation import validate_order

@pytest.mark.parametrize(
    "amount, quantity, expected",
    [
        (100, 2, True),
        (-50, 2, False),
        (100, 0, False),
        (0, 5, False),
        (200, -3, False),
        (150, 10, True),
    ]
)
def test_order_validation(amount, quantity, expected):
    result = validate_order(amount, quantity)
    assert result == expected

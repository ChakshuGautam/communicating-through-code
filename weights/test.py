import pytest
from weights import calculate_weighted_sum


def test_calculate_weighted_sum():
    assert calculate_weighted_sum(1, 1, 1) == 10
    assert calculate_weighted_sum(0, 0, 0) == 0
    assert calculate_weighted_sum(1, 2, 3) == 21


def test_calculate_weighted_sum_invalid_input():
    with pytest.raises(ValueError):
        calculate_weighted_sum(1, "a", 3)

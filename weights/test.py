import pytest
from weights import calculate_weighted_sum


def test_calculate_weighted_sum():
    assert calculate_weighted_sum(1, 1, 1) == 10
    assert calculate_weighted_sum(0, 0, 0) == 0
    assert calculate_weighted_sum(1, 2, 3) == 21


def test_calculate_weighted_sum_invalid_input():
    with pytest.raises(ValueError):
        calculate_weighted_sum(1, "a", 3)


def test_values_are_numbers():
    with pytest.raises(ValueError):
        calculate_weighted_sum("one", 2, 3)
    with pytest.raises(ValueError):
        calculate_weighted_sum(1, "two", 3)
    with pytest.raises(ValueError):
        calculate_weighted_sum(1, 2, "three")


def test_values_are_none():
    with pytest.raises(TypeError):
        calculate_weighted_sum(None, 2, 3)
    with pytest.raises(TypeError):
        calculate_weighted_sum(1, None, 3)
    with pytest.raises(TypeError):
        calculate_weighted_sum(1, 2, None)


def test_valid_weights():
    assert calculate_weighted_sum(1, 1, 1) == 2 * 1 + 3 * 1 + 5 * 1
    assert calculate_weighted_sum(1, 2, 3) == 2 * 1 + 3 * 2 + 5 * 3
    assert calculate_weighted_sum(0, 0, 0) == 0


def test_no_inputs():
    with pytest.raises(TypeError):
        calculate_weighted_sum()


def test_extra_inputs():
    with pytest.raises(TypeError):
        calculate_weighted_sum(1, 2, 3, 4)

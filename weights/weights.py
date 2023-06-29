def calculate_weighted_sum(
    first_value: float, second_value: float, third_value: float
) -> float:
    """
    Calculates a weighted sum of three values.

    Each value is multiplied by a predetermined weight (2, 3, and 5 respectively)
    and then all the products are summed up.

    Returns:
    weighted_sum (float): The resulting weighted sum of the input values.

    Raises:
    ValueError: If any of the inputs are not numbers.
    """

    if not all(
        isinstance(i, (int, float)) for i in [first_value, second_value, third_value]
    ):
        raise ValueError("All inputs must be numbers")

    weight_first = 2
    weight_second = 3
    weight_third = 5
    weighted_sum = (
        (first_value * weight_first)
        + (second_value * weight_second)
        + (third_value * weight_third)
    )
    return weighted_sum

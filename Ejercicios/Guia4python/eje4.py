import math, pytest

def calculate_statistics(numbers):
    longitud = len(numbers)
    promedio = sum(numbers) / longitud

    variance = sum((x - promedio) ** 2 for x in numbers) / longitud
    std_deviation = math.sqrt(variance)

    return promedio, std_deviation

@pytest.mark.parametrize("numbers, expected_mean, expected_std_deviation", [
    ([1, 2, 3, 4, 5], 3.0, 1.4142135623730951),
    ([0, 0, 0, 0, 0], 0.0, 0.0),
    ([1], 1.0, 0.0),
    ([1, 3, 5, 7, 9], 5.0, 2.8284271247461903)
])

def test_calculate_statistics(numbers, expected_mean, expected_std_deviation):
    actual_mean, actual_std_deviation = calculate_statistics(numbers)
    assert actual_mean == expected_mean
    assert actual_std_deviation == expected_std_deviation

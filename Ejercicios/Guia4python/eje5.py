import pytest

def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return False


@pytest.mark.parametrize("matrix, target, expected_value", [
    ([
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ], 9, True),
    ([
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ], 10, False),
    ([
        [2, 4, 6, 8],
        [10, 12, 14, 16],
        [18, 20, 22, 24],
        [26, 28, 30, 32]
    ], 14, True),
    ([], 5, False),
    ([[]], 5, False)
])

def test_search_matrix(matrix, target, expected_value):
    assert search_matrix(matrix, target) == expected_value


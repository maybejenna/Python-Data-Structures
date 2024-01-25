def sum_up_diagonals(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("Input must be a square matrix")

    n = len(matrix)
    total_sum = 0

    for i in range(n):
        total_sum += matrix[i][i]          # TL-to-BR diagonal
        total_sum += matrix[i][n - 1 - i]  # BL-to-TR diagonal

    # Subtract the middle element once if n is odd, as it gets counted twice.
    if n % 2 == 1:
        total_sum -= matrix[n // 2][n // 2]

    return total_sum
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
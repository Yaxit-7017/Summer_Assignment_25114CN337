def diagonal_sum(matrix):
    n = len(matrix)
    primary = sum(matrix[i][i] for i in range(n))
    secondary = sum(matrix[i][n - 1 - i] for i in range(n))
    if n % 2 == 1:
        secondary -= matrix[n // 2][n // 2]
    return primary + secondary

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(matrix))

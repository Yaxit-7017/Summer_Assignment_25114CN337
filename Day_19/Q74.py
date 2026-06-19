def subtract_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]
    return result

matrix1 = [[10, 20, 30], [40, 50, 60]]
matrix2 = [[1, 2, 3], [4, 5, 6]]

result = subtract_matrices(matrix1, matrix2)
for row in result:
    print(row)
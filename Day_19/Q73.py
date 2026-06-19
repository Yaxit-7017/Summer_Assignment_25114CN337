def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]

result = add_matrices(matrix1, matrix2)
for row in result:
    print(row)
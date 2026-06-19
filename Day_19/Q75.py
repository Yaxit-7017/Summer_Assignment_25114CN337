def transpose_matrix(A):
    rows = len(A)
    cols = len(A[0])
    result = [[A[i][j] for i in range(rows)] for j in range(cols)]
    return result

matrix = [[1, 2, 3], [4, 5, 6]]

result = transpose_matrix(matrix)
for row in result:
    print(row)
    
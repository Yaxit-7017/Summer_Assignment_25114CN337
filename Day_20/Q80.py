def column_wise_sum(M):
    rows = len(M)
    cols = len(M[0])
    sums = [0] * cols

    for j in range(cols):
        for i in range(rows):
            sums[j] += M[i][j]

    return sums


def print_matrix(M):
    for row in M:
        print(row)


if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix(A)
    sums = column_wise_sum(A)

    for j, s in enumerate(sums):
        print(f"Sum of column {j}: {s}")
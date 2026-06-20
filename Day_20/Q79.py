def row_wise_sum(M):
    return [sum(row) for row in M]


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
    sums = row_wise_sum(A)

    for i, s in enumerate(sums):
        print(f"Sum of row {i}: {s}")
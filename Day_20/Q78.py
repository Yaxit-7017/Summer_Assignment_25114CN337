def is_symmetric(M):
    n = len(M)
    for i in range(n):
        if len(M[i]) != n:
            return False

    for i in range(n):
        for j in range(n):
            if M[i][j] != M[j][i]:
                return False

    return True


def print_matrix(M):
    for row in M:
        print(row)


if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [2, 5, 6],
        [3, 6, 9]
    ]

    B = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix(A)
    print("Symmetric:", is_symmetric(A))

    print()

    print_matrix(B)
    print("Symmetric:", is_symmetric(B))
    
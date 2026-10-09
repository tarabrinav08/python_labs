def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []

    n = len(mat[0])

    for row in mat:
        if len(row) != n:
            raise ValueError("рваная матрица")

    result = []

    for i in range(n):
        result.append([row[i] for row in mat])

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    n = len(mat[0])

    for row in mat:
        if len(row) != n:
            raise ValueError("рваная матрица")

    result = []

    for row in mat:
        result.append(sum(row))

    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    n = len(mat[0])

    for row in mat:
        if len(row) != n:
            raise ValueError("рваная матрица")

    result = []

    for i in range(n):
        result.append(sum(row[i] for row in mat))

    return result


print("\ntranspose:")
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))

try:
    transpose([[1, 2], [3]])
except ValueError as e:
    print(f"ValueError: {e}")


print("\nrow_sums:")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))

try:
    row_sums([[1, 2], [3]])
except ValueError as e:
    print(f"ValueError: {e}")


print("\ncol_sums:")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))

try:
    col_sums([[1, 2], [3]])
except ValueError as e:
    print(f"ValueError: {e}")


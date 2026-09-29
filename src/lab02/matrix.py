def transpose(mat: list[list[float | int]]) -> list[list]:
    # Меняем строки и столбцы местами
    if not mat:
        return []

    columns = len(mat[0])  # Запоминаем количество столбцов

    # Проверяем длину каждой строки
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица')

    result = []  # Список для новой матрицы

    # Перебираем столбцы исходной матрицы
    for col in range(columns):
        new_row = []

        # Берём элементы из всех строк
        for row in range(len(mat)):
            new_row.append(mat[row][col])

        result.append(new_row)

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    # Считаем сумму элементов каждой строки
    if not mat:
        return []

    columns = len(mat[0])  # Определяем длину строки

    # Проверяем, что матрица прямоугольная
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица')

    result = []  # Список для сумм строк

    # Считаем сумму каждой строки
    for row in mat:
        total = 0

        for x in row:
            total += x

        result.append(total)

    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:
    # Считаем сумму элементов каждого столбца
    if not mat:
        return []

    columns = len(mat[0])  # Запоминаем количество столбцов

    # Проверяем одинаковую длину строк
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица')

    result = []  # Список для сумм столбцов

    # Перебираем столбцы
    for col in range(columns):
        total = 0

        # Складываем элементы текущего столбца
        for row in mat:
            total += row[col]

        result.append(total)

    return result


print('\ntranspose:')
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))

try:
    print(transpose([[1, 2], [3]]))
except ValueError:
    print('ValueError')


print('\nrow_sums:')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))

try:
    print(row_sums([[1, 2], [3]]))
except ValueError:
    print('ValueError')


print('\ncol_sums:')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))

try:
    print(col_sums([[1, 2], [3]]))
except ValueError:
    print('ValueError')
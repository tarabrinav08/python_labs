def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    # Проверяем список на пустоту
    if not nums:
        raise ValueError("Список чисел не должен быть пустым")

    minimum = nums[0]
    maximum = nums[0]

    # Ищем минимальное и максимальное значения
    for x in nums[1:]:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x

    return minimum, maximum


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    result = []

    # Добавляем только уникальные числа
    for x in nums:
        if x not in result:
            result.append(x)

    # Сортируем список вручную
    for i in range(len(result)):
        for j in range(len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def flatten(mat: list[list | tuple]) -> list:
    result = []

    # Проверяем каждую строку матрицы
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Элемент матрицы должен быть списком или кортежем")

        for x in row:
            result.append(x)

    return result

print('\nmin_max')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))

try:
    min_max([])
except ValueError as e:
    print(f"ValueError: {e}")

print('\nunique_sorted')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print('\nflatten')
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))

try:
    flatten([[1, 2], "ab"])
except TypeError as e:
    print(f"TypeError: {e}")


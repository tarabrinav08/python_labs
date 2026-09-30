def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    # Проверяем список на пустоту
    if len(nums) == 0:
        raise ValueError

    minimum = nums[0]
    maximum = nums[0]

    # Ищем минимальное и максимальное значение
    for x in nums:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x

    return minimum, maximum


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    result = []  # Список для уникальных чисел

    # Добавляем только неповторяющиеся числа
    for x in nums:
        if x not in result:
            result.append(x)

    # Сортируем список вручную
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]

    return result


def flatten(mat: list[list | tuple]) -> list:
    result = []  # Новый список для элементов

    # Проверяем каждую строку
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError

        # Добавляем элементы строки в общий список
        for x in row:
            result.append(x)

    return result


print('\nmin_max')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))


print('\nunique_sorted')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))


print('\nflatten')
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))

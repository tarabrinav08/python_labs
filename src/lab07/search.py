def linear_search(nums, x):
    """
    Возвращает индекс первого вхождения x.
    Если число не найдено, возвращает -1.
    """

    # Перебираем все индексы списка
    for i in range(len(nums)):
        # Проверяем, совпадает ли элемент с искомым числом
        if nums[i] == x:
            return i

    # Если число не найдено, возвращаем -1
    return -1


def binary_search(sorted_nums, x):
    """
    Ищет число x в отсортированном списке.
    Возвращает индекс или -1.
    На неотсортированном списке результат не определён.
    """

    # Устанавливаем левую и правую границы поиска
    lo = 0
    hi = len(sorted_nums) - 1

    # Продолжаем поиск, пока границы не пересеклись
    while lo <= hi:
        # Находим индекс середины списка
        mid = (lo + hi) // 2

        # Если число найдено, возвращаем его индекс
        if sorted_nums[mid] == x:
            return mid

        # Если искомое число больше, ищем в правой половине
        elif sorted_nums[mid] < x:
            lo = mid + 1

        # Иначе продолжаем поиск в левой половине
        else:
            hi = mid - 1

    # Если число отсутствует, возвращаем -1
    return -1


def two_sum_brute(nums, target):
    """
    Ищет два числа, сумма которых равна target.
    Возвращает их индексы или None.
    """

    # Перебираем все пары элементов с разными индексами
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Проверяем, равна ли сумма нужному значению
            if nums[i] + nums[j] == target:
                return (i, j)

    # Если подходящая пара не найдена
    return None


def two_sum_fast(nums, target):
    """
    Ищет два числа с суммой target через словарь.
    Возвращает пару индексов или None.
    """

    # Создаём словарь для хранения чисел и их индексов
    seen = {}

    # Перебираем элементы списка
    for i in range(len(nums)):
        x = nums[i]

        # Вычисляем число, которого не хватает до target
        need = target - x

        # Проверяем, встречалось ли нужное число ранее
        if need in seen:
            return (seen[need], i)

        # Сохраняем текущее число и его индекс
        seen[x] = i

    # Если подходящая пара не найдена
    return None


if __name__ == "__main__":

    # Проверка линейного поиска
    print("\nLinear Search:")
    print(linear_search([4, 2, 7, 2], 2))
    print(linear_search([4, 2, 7, 2], 9))
    print(linear_search([], 5))

    # Проверка бинарного поиска
    print("\nBinary Search:")
    print(binary_search([1, 3, 5, 7, 9], 5))
    print(binary_search([1, 3, 5, 7, 9], 3))
    print(binary_search([1, 3, 5, 7, 9], 10))
    print(binary_search([], 5))

    # Проверка поиска пары перебором
    print("\nTwo Sum Brute:")
    print(two_sum_brute([2, 7, 11, 15], 9))
    print(two_sum_brute([1, 2, 3], 10))
    print(two_sum_brute([4, 4, 8], 8))

    # Проверка быстрого поиска пары через словарь
    print("\nTwo Sum Fast:")
    print(two_sum_fast([2, 7, 11, 15], 9))
    print(two_sum_fast([1, 2, 3], 10))
    print(two_sum_fast([4, 4, 8], 8))

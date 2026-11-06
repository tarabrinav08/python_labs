import random

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials=100):
    """
    Проверяет правильность сортировки.
    Также проверяет, что исходный список не изменился.
    """

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]

        original = list(nums)
        result = fn(nums)

        # Сравниваем результат с обычной сортировкой Python
        assert result == sorted(nums), f"Ошибка сортировки: {nums}"

        # Проверяем, что исходный список не изменился
        assert nums == original, "Исходный список изменился"


def check_search():
    """
    Проверяет линейный и бинарный поиск.
    """

    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-100, 100)

        # Получаем ожидаемый результат линейного поиска
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1

        result = linear_search(nums, x)

        assert result == expected, "Ошибка линейного поиска"

        # Бинарный поиск выполняем на отсортированном списке
        sorted_nums = sorted(nums)
        binary_result = binary_search(sorted_nums, x)

        if x not in sorted_nums:
            assert binary_result == -1, "Ошибка бинарного поиска"
        else:
            assert 0 <= binary_result < len(sorted_nums)
            assert sorted_nums[binary_result] == x, "Ошибка бинарного поиска"

    # Проверяем граничные случаи
    nums = [1, 3, 5, 7, 9]

    assert binary_search(nums, 1) == 0
    assert binary_search(nums, 9) == 4
    assert binary_search(nums, 10) == -1
    assert binary_search([], 5) == -1

    assert linear_search([], 5) == -1
    assert linear_search([2, 4, 2], 2) == 0


def check_two_sum(trials=100):
    """
    Проверяет две функции поиска пары чисел.
    """

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target = random.randint(-100, 100)

        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)

        # Если первая функция не нашла пару,
        # вторая тоже должна вернуть None
        if brute is None:
            assert fast is None, "Ошибка Two Sum Fast"
        else:
            # Проверяем индексы и сумму первой функции
            i, j = brute

            assert 0 <= i < j < len(nums)
            assert nums[i] + nums[j] == target

            # Вторая функция тоже должна найти пару
            assert fast is not None, "Ошибка Two Sum Fast"

            i, j = fast

            assert 0 <= i < j < len(nums)
            assert nums[i] + nums[j] == target

    # Дополнительные проверки
    assert two_sum_brute([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum_fast([2, 7, 11, 15], 9) == (0, 1)

    assert two_sum_brute([1, 2, 3], 10) is None
    assert two_sum_fast([1, 2, 3], 10) is None

    assert two_sum_brute([], 5) is None
    assert two_sum_fast([], 5) is None


if __name__ == "__main__":

    # Проверяем три сортировки
    check_sorting(bubble_sort)
    check_sorting(insertion_sort)
    check_sorting(selection_sort)

    # Проверяем поиск
    check_search()

    # Проверяем Two Sum
    check_two_sum()

    print("OK: все проверки пройдены")

def linear_search(nums, x):
    """
    Возвращает индекс первого вхождения x.
    Если число не найдено, возвращает -1.
    """

    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def binary_search(sorted_nums, x):
    """
    Ищет число x в отсортированном списке.
    Возвращает индекс или -1.
    На неотсортированном списке результат не определён.
    """
    lo = 0
    hi = len(sorted_nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def two_sum_brute(nums, target):
    """
    Ищет два числа, сумма которых равна target.
    Возвращает их индексы или None.
    """

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)

    return None


def two_sum_fast(nums, target):
    """
    Ищет два числа с суммой target через словарь.
    Возвращает пару индексов или None.
    """

    seen = {}
    for i in range(len(nums)):
        x = nums[i]
        need = target - x

        if need in seen:
            return (seen[need], i)
        seen[x] = i

    return None


if __name__ == "__main__":
    print("Линейный поиск:")
    print(linear_search([4, 2, 7, 2], 2))
    print(linear_search([4, 2, 7, 2], 9))
    print(linear_search([], 5))

    print("Бинарный поиск:")
    print(binary_search([1, 3, 5, 7, 9], 5))
    print(binary_search([1, 3, 5, 7, 9], 3))
    print(binary_search([1, 3, 5, 7, 9], 10))
    print(binary_search([], 5))

    print("Two Sum Brute:")
    print(two_sum_brute([2, 7, 11, 15], 9))
    print(two_sum_brute([1, 2, 3], 10))
    print(two_sum_brute([4, 4, 8], 8))

    print("Two Sum Fast:")
    print(two_sum_fast([2, 7, 11, 15], 9))
    print(two_sum_fast([1, 2, 3], 10))
    print(two_sum_fast([4, 4, 8], 8))

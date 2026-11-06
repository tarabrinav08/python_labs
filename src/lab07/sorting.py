def bubble_sort(nums):
    """
    Сортирует список по возрастанию методом пузырька.
    Возвращает новый список, исходный не изменяет.
    """

    nums = list(nums)

    for i in range(len(nums)):
        swapped = False

        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break

    return nums

def insertion_sort(nums):
    """
    Сортирует список по возрастанию методом вставок.
    Возвращает новый список, исходный не изменяет.
    """

    nums = list(nums)

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

def selection_sort(nums):
    """
    Сортирует список по возрастанию методом выбора.
    Возвращает новый список, исходный не изменяет.
    """

    nums = list(nums)
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        
        nums[i], nums[min_index] = nums[min_index], nums[i]
    
    return nums

if __name__ == "__main__":
    print("\nBubble Sort:")
    print(bubble_sort([3, 1, 2]))
    print(bubble_sort([2, 2, 1]))
    print(bubble_sort([]))

    print("\nInsertion Sort:")
    print(insertion_sort([3, 1, 2]))
    print(insertion_sort([5, 2, 4]))
    print(insertion_sort([]))

    print("\nSelection Sort:")
    print(selection_sort([3, 1, 2]))
    print(selection_sort([5, 2, 8, 1]))
    print(selection_sort([]))




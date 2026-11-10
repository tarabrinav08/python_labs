import random
import timeit

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab04.io_txt_csv import write_csv


def bench_sorts(n):
    """
    Измеряет время выполнения разных алгоритмов сортировки.
    Возвращает список результатов измерений.
    """
    # Создаём случайный список и список для результатов
    data = [random.randint(-1000, 1000) for _ in range(n)]
    rows = []

    # Измеряем время встроенной сортировки
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", t))

    # Сравниваем три сортировки на списках меньше 100000 элементов
    if n < 100000:
        t = timeit.timeit(lambda: bubble_sort(data), number=1)
        rows.append(("sort", n, "bubble_sort", t))

        t = timeit.timeit(lambda: insertion_sort(data), number=1)
        rows.append(("sort", n, "insertion_sort", t))

        t = timeit.timeit(lambda: selection_sort(data), number=1)
        rows.append(("sort", n, "selection_sort", t))
    else:
        # Для больших списков пропускаем медленные сортировки
        rows.append(("sort", n, "bubble_sort", "> 60 с"))
        rows.append(("sort", n, "insertion_sort", "> 60 с"))
        rows.append(("sort", n, "selection_sort", "> 60 с"))

    return rows


def bench_search():
    """
    Сравнивает время линейного и бинарного поиска.
    Отдельно измеряет предварительную сортировку.
    """
    # Создаём список чисел и 10000 запросов
    nums = [random.randint(0, 100000) for _ in range(100000)]
    queries = [random.randint(0, 100000) for _ in range(10000)]
    rows = []

    # Измеряем время сортировки перед бинарным поиском
    t = timeit.timeit(lambda: sorted(nums), number=1)
    rows.append(("search", 100000, "sorting_before_binary", t))

    sorted_nums = sorted(nums)

    # Измеряем время линейного поиска
    t = timeit.timeit(
        lambda: [linear_search(nums, x) for x in queries],
        number=1
    )
    rows.append(("search", 100000, "linear_search", t))

    # Измеряем время бинарного поиска
    t = timeit.timeit(
        lambda: [binary_search(sorted_nums, x) for x in queries],
        number=1
    )
    rows.append(("search", 100000, "binary_search", t))

    return rows


def bench_two_sum(n):
    """
    Сравнивает скорость двух способов поиска пары чисел.
    Возвращает результаты измерений.
    """
    # Создаём список уникальных чисел и гарантированную сумму
    nums = random.sample(range(1, 1000000000), n)
    target = nums[-2] + nums[-1]
    rows = []

    # Измеряем время перебора пар
    t = timeit.timeit(lambda: two_sum_brute(nums, target), number=1)
    rows.append(("two_sum", n, "two_sum_brute", t))

    # Измеряем время поиска через словарь
    t = timeit.timeit(lambda: two_sum_fast(nums, target), number=1)
    rows.append(("two_sum", n, "two_sum_fast", t))

    return rows


if __name__ == "__main__":
    # Фиксируем генерацию случайных чисел
    random.seed(42)
    results = []

    # Запускаем измерения сортировок
    for n in [1000, 10000, 100000]:
        results.extend(bench_sorts(n))

    # Запускаем измерения поиска
    results.extend(bench_search())

    # Запускаем измерения Two Sum
    for n in [1000, 10000]:
        results.extend(bench_two_sum(n))

    # Выводим заголовок таблицы
    print(f"{'task':<12} {'n':<10} {'impl':<25} {'seconds':<15}")
    print("-" * 65)

    csv_rows = []

    # Выводим результаты и подготавливаем данные для CSV
    for task, n, impl, seconds in results:
        if isinstance(seconds, float):
            seconds_text = f"{seconds:.6f}"
        else:
            seconds_text = seconds

        print(f"{task:<12} {n:<10} {impl:<25} {seconds_text:<15}")
        csv_rows.append((task, n, impl, seconds_text))

    # Сохраняем результаты в CSV-файл
    write_csv(
        csv_rows,
        "data/lab07/bench.csv",
        header=("task", "n", "impl", "seconds")
    )

    print("\nResults saved to data/lab07/bench.csv")


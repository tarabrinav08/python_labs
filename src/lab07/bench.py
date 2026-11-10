
import random
import timeit

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab04.io_txt_csv import write_csv


def bench_sorts(n):
    data = [random.randint(-1000, 1000) for _ in range(n)]
    rows = []

    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", t))

    if n < 100000:
        t = timeit.timeit(lambda: bubble_sort(data), number=1)
        rows.append(("sort", n, "bubble_sort", t))

        t = timeit.timeit(lambda: insertion_sort(data), number=1)
        rows.append(("sort", n, "insertion_sort", t))

        t = timeit.timeit(lambda: selection_sort(data), number=1)
        rows.append(("sort", n, "selection_sort", t))
    else:
        rows.append(("sort", n, "bubble_sort", "> 60 с"))
        rows.append(("sort", n, "insertion_sort", "> 60 с"))
        rows.append(("sort", n, "selection_sort", "> 60 с"))

    return rows


def bench_search():
    nums = [random.randint(0, 100000) for _ in range(100000)]
    queries = [random.randint(0, 100000) for _ in range(10000)]
    rows = []

    t = timeit.timeit(lambda: sorted(nums), number=1)
    rows.append(("search", 100000, "sorting_before_binary", t))

    sorted_nums = sorted(nums)

    t = timeit.timeit(
        lambda: [linear_search(nums, x) for x in queries],
        number=1
    )
    rows.append(("search", 100000, "linear_search", t))

    t = timeit.timeit(
        lambda: [binary_search(sorted_nums, x) for x in queries],
        number=1
    )
    rows.append(("search", 100000, "binary_search", t))

    return rows


def bench_two_sum(n):
    nums = random.sample(range(1, 1000000000), n)
    target = nums[-2] + nums[-1]
    rows = []

    t = timeit.timeit(lambda: two_sum_brute(nums, target), number=1)
    rows.append(("two_sum", n, "two_sum_brute", t))

    t = timeit.timeit(lambda: two_sum_fast(nums, target), number=1)
    rows.append(("two_sum", n, "two_sum_fast", t))

    return rows


if __name__ == "__main__":
    random.seed(42)
    results = []

    for n in [1000, 10000, 100000]:
        results.extend(bench_sorts(n))

    results.extend(bench_search())

    for n in [1000, 10000]:
        results.extend(bench_two_sum(n))

    print(f"{'task':<12} {'n':<10} {'impl':<25} {'seconds':<15}")
    print("-" * 65)

    csv_rows = []

    for task, n, impl, seconds in results:
        if isinstance(seconds, float):
            seconds_text = f"{seconds:.6f}"
        else:
            seconds_text = seconds

        print(f"{task:<12} {n:<10} {impl:<25} {seconds_text:<15}")
        csv_rows.append((task, n, impl, seconds_text))

    write_csv(
        csv_rows,
        "data/lab07/bench.csv",
        header=("task", "n", "impl", "seconds")
    )

    print("\nРезультаты сохранены в data/lab07/bench.csv")

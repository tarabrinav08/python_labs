# Лабораторная работа №1
## Задание 1
 ![1 задание](images/lab01/img01.png)
  Определяется возраст человека через один год на основе введённых имени и текущего возраста.

## Задание 2
 ![2 задание](images/lab01/img02.png)
  Для двух введённых чисел находятся их общая сумма и среднее арифметическое.

## Задание 3
 ![3 задание](images/lab01/img03.png) 
  Рассчитывается конечная стоимость товара после применения скидки и добавления НДС.

## Задание 4
 ![4 задание](images/lab01/img04.png)
  Указанное количество минут преобразуется в соответствующее количество часов и минут.

## Задание 5
 ![5 задание](images/lab01/img05.png)
 Из введённого ФИО формируются инициалы, а также подсчитывается количество символов после удаления лишних пробелов.

## Задание 6
 ![6 задание](images/lab01/img06.png)
 По данным участников определяется, сколько человек выбрали очное обучение, а сколько — заочное.


# Лабораторная работа №2
## Задание 1 
```python 
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
```
 ![1 задание](images/lab02/arrays01.png)
 По списку чисел находятся минимальное и максимальное значения, удаляются повторяющиеся элементы и выполняется сортировка, а вложенные списки объединяются в один.
 









## Задание B
```python
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


print("\nrow_sums:")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))

print("\ncol_sums:")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
```
 ![2 задание](images/lab02/matrix02.png)
 Для матрицы выполняется транспонирование, а также подсчитываются суммы элементов каждой строки и каждого столбца.


## Задание C
```python
def format_record(rec: tuple[str, str, float]) -> str:
    """Форматирует запись студента в виде строки."""

    if not isinstance(rec, tuple):
        raise TypeError("Запись должна быть кортежем")

    if len(rec) != 3:
        raise ValueError("В кортеже должно быть 3 элемента")

    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("ФИО и группа должны быть строками")

    if not isinstance(gpa, float):
        raise TypeError("GPA должен быть числом float")

    fio = " ".join(fio.strip().split())
    group = group.strip()

    if not fio or not group:
        raise ValueError("ФИО и группа не должны быть пустыми")

    if gpa < 0.0 or gpa > 5.0:
        raise ValueError("GPA должен быть от 0.0 до 5.0")

    parts = fio.split()

    if len(parts) < 2 or len(parts) > 3:
        raise ValueError("ФИО должно содержать 2 или 3 слова")

    surname = parts[0].capitalize()

    initials = ""
    for name in parts[1:]:
        initials += name[0].upper() + "."

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
 ![3 задание](images/lab02/tuples03.png)
 Из записи студента формируются фамилия и инициалы, удаляются лишние пробелы и выводится группа и GPA с округлением до двух знаков.



def format_record(rec: tuple[str, str, float]) -> str:
    # Проверяем, что запись является кортежем
    if not isinstance(rec, tuple):
        raise TypeError

    # Проверяем количество элементов
    if len(rec) != 3:
        raise ValueError

    fio = rec[0]
    group = rec[1]
    gpa = rec[2]

    # Проверяем тип ФИО
    if not isinstance(fio, str):
        raise TypeError

    # Проверяем тип группы
    if not isinstance(group, str):
        raise TypeError

    # Проверяем тип GPA
    if not isinstance(gpa, float):
        raise TypeError

    # Убираем лишние пробелы
    fio = ' '.join(fio.strip().split())
    group = group.strip()

    # Проверяем, что ФИО и группа не пустые
    if not fio or not group:
        raise ValueError

    # Проверяем допустимый диапазон GPA
    if gpa < 0.0 or gpa > 5.0:
        raise ValueError

    # Разделяем ФИО на отдельные слова
    parts = fio.split()

    # В ФИО должно быть 2 или 3 слова
    if len(parts) < 2 or len(parts) > 3:
        raise ValueError

    surname = parts[0].capitalize()  # Фамилия
    initials = ''

    # Формируем инициалы имени и отчества
    for name in parts[1:]:
        initials += name[0].upper() + '.'

    # Собираем итоговую строку
    return f'{surname} {initials}, гр. {group}, GPA {gpa:.2f}'


print('\nformat_record:')
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))

try:
    print(format_record(("", "BIVT-25", 4.6)))
except ValueError:
    print('ValueError')

try:
    print(format_record(("Иванов Иван", "", 4.6)))
except ValueError:
    print('ValueError')

try:
    print(format_record(("Иванов Иван", "BIVT-25", "4.6")))
except TypeError:
    print('TypeError')
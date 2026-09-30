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

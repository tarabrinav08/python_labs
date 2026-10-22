
import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает содержимое текстового файла и возвращает его строкой.

    path указывает расположение файла, а encoding определяет
    кодировку для чтения. По умолчанию используется UTF-8,
    но при необходимости можно указать encoding="cp1251".

    Если файл отсутствует, возникает FileNotFoundError.
    При неправильной кодировке возникает UnicodeDecodeError.
    Если файл пустой, функция возвращает пустую строку.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """
    Проверяет наличие папок по указанному пути.
    Если нужных папок нет, создаёт их.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """
    Создаёт CSV-файл и записывает в него переданные данные.

    rows содержит строки для записи, path указывает,
    где будет сохранён файл. Параметр header позволяет
    добавить заголовки столбцов в первую строку.

    Перед сохранением проверяется количество элементов
    в каждой строке. Если длины различаются, возникает
    ValueError. Длина заголовка также проверяется.

    Если rows пустой, создаётся пустой CSV-файл
    или файл только с заголовком, если он указан.
    При повторной записи старые данные заменяются новыми.
    """
    rows = list(rows)
    lengths = {len(row) for row in rows}

    if header is not None:
        lengths.add(len(header))

    if len(lengths) > 1:
        raise ValueError("Все строки должны иметь одинаковую длину")

    ensure_parent_dir(path)
    p = Path(path)

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if header is not None:
            writer.writerow(header)

        for row in rows:
            writer.writerow(row)


if __name__ == "__main__":
    txt = read_text("data/lab04/input.txt")
    print(txt)

    write_csv([("word", "count"), ("test", 3)], "data/lab04/check.csv")
    print("CSV создан.")

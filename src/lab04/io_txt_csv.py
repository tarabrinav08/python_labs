
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл и возвращает его содержимое одной строкой.
    По умолчанию используется UTF-8.
    Для другой кодировки можно указать encoding="cp1251".
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """
    Записывает строки в CSV-файл.
    Если передан header, записывает его первой строкой.
    Проверяет, что все строки имеют одинаковую длину.
    """
    rows = list(rows)
    lengths = {len(row) for row in rows}

    if header is not None:
        lengths.add(len(header))

    if len(lengths) > 1:
        raise ValueError("Все строки должны иметь одинаковую длину")

    def ensure_parent_dir(path: str | Path) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)

    ensure_parent_dir(path)
    p = Path(path)

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if header is not None:
            writer.writerow(header)

        for row in rows:
            writer.writerow(row)

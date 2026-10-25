import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей, заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — по первому появлению ключей.
    """

    if not json_path.endswith(".json"):
        raise ValueError("Файл должен быть JSON")
    if not csv_path.endswith(".csv"):
        raise ValueError("Файл должен быть CSV")

    with open(json_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неправильный формат")

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("JSON должен содержать список словарей")

    columns = []
    for item in data:
        for key in item:
            if key not in columns:
                columns.append(key)

    if len(columns) == 0:
        raise ValueError("В JSON нет полей")

    path = Path(csv_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()

        for item in data:
            row = {}
            for column in columns:
                row[column] = item.get(column, "")
            writer.writerow(row)

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON.
    Заголовок обязателен, значения сохраняются как строки.
    """
    if not json_path.endswith(".json"):
        raise ValueError("Файл должен быть JSON")
    if not csv_path.endswith(".csv"):
        raise ValueError("Файл должен быть CSV")

    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if not reader.fieldnames:
             raise ValueError("CSV без заголовка")
        
        data = list(reader)
        for row in data:
             if None in row:
                 raise ValueError("Неверное количество столбцов CSV")

             for key in row:
                 if row[key] is None:
                     row[key] = ""

    if not data:
        raise ValueError("Пустой CSV")

    path = Path(json_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(json_path, "w", encoding="utf-8") as f:
         json.dump(data, f, ensure_ascii=False, indent=2)

           
if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")

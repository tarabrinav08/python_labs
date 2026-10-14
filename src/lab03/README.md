# Лабораторная работа №3

## Задание A 

В модуле `src/lib/text.py` собраны четыре функции для обработки текста. `normalize` приводит строку к единому виду: убирает различия в регистре (через `casefold`), заменяет `«ё»` на `«е»` и сводит все пробельные символы к одиночным пробелам. `tokenize` с помощью регулярного выражения вытаскивает из текста слова, при этом дефис внутри слова не разрывает его, а знаки препинания и эмодзи отбрасываются. `count_freq` считает, сколько раз встречается каждое слово. `top_n` выбирает самые частые слова: сначала по убыванию частоты, а при одинаковой частоте по алфавиту. Функции не вводят и не выводят данные, а правильность их работы проверяется блоком assert в конце файла.

```python
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Приводит текст к единому виду, чтобы его было удобно сравнивать.

    casefold=True  - регистр убирается через casefold(), иначе через lower().
    yo2e=True      - буквы ё и Ё превращаются в е и Е.
    Табы и переводы строк становятся пробелами, лишние пробелы сливаются в один.
    """
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е")
        text = text.replace("Ё", "Е")

    text = text.replace("\t", " ")
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    text = " ".join(text.split())

    return text


def tokenize(text: str) -> list[str]:
    """
    Достаёт из текста слова и возвращает их списком.

    Слово - это буквы, цифры и подчёркивания подряд. Дефис между двумя
    частями тоже остаётся внутри слова (например, "по-настоящему").
    Знаки препинания, пробелы и эмодзи в результат не попадают.
    """
    words = re.findall(r"\w+(?:-\w+)*", text)

    return words


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Считает, сколько раз каждое слово встретилось в списке.

    Возвращает словарь, где ключ - слово, а значение - его количество.
    """
    freq = {}

    for word in tokens:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Выбирает n самых популярных слов из словаря частот.

    Сначала идут слова, которые встречаются чаще всего.
    Если частота одинаковая, слова расставляются по алфавиту.
    """
    words = list(freq.items())
    words.sort(key=lambda x: (-x[1], x[0]))
    return words[:n]


if __name__ == "__main__":
    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"

    # tokenize
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello,world!!!") == ["hello", "world"]
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

    # count_freq + top_n
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]

    # тай-брейк: при равной частоте слова идут по алфавиту
    tokens = ["bb", "aa", "bb", "aa", "cc"]
    freq = count_freq(tokens)
    assert freq == {"aa": 2, "bb": 2, "cc": 1}
    assert top_n(freq, 2) == [("aa", 2), ("bb", 2)]
```    
## Задание B - Статистика текста
Файл src/lab03/text_stats.py анализирует любой текст, который ему подали на вход через терминал. Он принимает всё, что было введено до сигнала конца ввода, затем чистит текст и делит его на отдельные слова, используя готовые функции из src/lib/text.py. В результате на экране появляются три вещи: сколько слов в тексте всего, сколько среди них разных, и список из пяти лидеров по частоте, где каждая строка записана как слово:количество.

```python
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n


def main() -> None:
    """
    Читает текст из stdin, считает статистику по словам и печатает её:
    общее число слов, число уникальных слов и топ-5 самых частых.
    """
    # читаем весь текст из stdin (до EOF)
    text = sys.stdin.read()

    # приводим к нормальному виду и делим на слова
    text = normalize(text)
    tokens = tokenize(text)

    # считаем частоты слов
    freq = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(freq)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")

    # пять самых частых слов в формате слово:количество
    for word, count in top_n(freq, n=5):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
```
![](images/lab03/textstats.png)

# Запуск кода:

Команды вводятся в терминале, открытом в корне проекта, то есть в папке, где лежит каталог `src/`. Скрипт запускается как модуль, для этого нужен ключ `-m`.

Быстрая проверка: текст передаётся прямо в команде
```bash
echo 'Привет, мир! Привет!!!' | python -m src.lab03.text_stats
```
Ввод вручную: текст набирается с клавиатуры

Запусти скрипт без `echo`:
```bash
python -m src.lab03.text_stats
```

После запуска терминал будет ждать текст. Напиши его и закончи ввод сочетанием `Ctrl+D` (на Windows: `Ctrl+Z`, затем `Enter` ). Тогда программа выведет результат.




"""
Скрипт читает весь введённый текст до конца ввода (EOF),
обрабатывает его функциями из lib/text.py и выводит статистику:
сколько всего слов, сколько из них уникальных и какие 5 слов самые частые.
"""

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
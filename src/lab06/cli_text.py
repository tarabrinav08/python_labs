import argparse
from src.lab04.io_txt_csv import read_text
from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        text = read_text(args.input)
        lines = text.splitlines()

        number = 1
        for line in lines:
            if args.n:
                print(f"{number}: {line}")
            else:
                print(line)
            number += 1

    elif args.command == "stats":
        if args.top <= 0:
            parser.error("--top должен быть положительным числом")

        text = read_text(args.input)
        text = normalize(text)
        tokens = tokenize(text)
        freq = count_freq(tokens)

        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freq)}")

        top_words = top_n(freq, n=args.top)

        for word, count in top_words:
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()

import argparse
import os


def parse_args():
    """Получает параметры командной строки."""
    parser = argparse.ArgumentParser(
        description="Анализатор зависимостей Maven"
    )

    parser.add_argument("--package", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--test-mode", action="store_true")
    parser.add_argument("--version", default="1.0.0")
    parser.add_argument("--ascii-tree", action="store_true")
    parser.add_argument("--filter", default="")

    return parser.parse_args()


def validate_args(args):
    """Проверяет корректность введённых параметров."""
    if not args.package or " " in args.package:
        raise ValueError("Название пакета пустое или содержит пробелы")

    if not args.version or " " in args.version:
        raise ValueError("Версия пустая или содержит пробелы")

    is_url = args.repo.startswith("http")

    if not is_url and not os.path.exists(args.repo):
        raise ValueError("Указанный путь не существует")

    if args.test_mode and not is_url:
        if not os.path.isfile(args.repo):
            raise ValueError("Указанный файл не существует")

    return args


def main():
    """Запускает программу и выводит параметры."""
    try:
        args = validate_args(parse_args())
    except ValueError as error:
        print(f"Ошибка: {error}")
        return

    print(f"package: {args.package}")
    print(f"repo: {args.repo}")
    print(f"test_mode: {args.test_mode}")
    print(f"version: {args.version}")
    print(f"ascii_tree: {args.ascii_tree}")
    print(f"filter: {args.filter}")


if __name__ == "__main__":
    main()

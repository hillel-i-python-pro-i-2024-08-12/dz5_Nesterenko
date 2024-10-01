# import argparse
# import logging
# from message_pkg import generator
#
# #Логування
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
# def main():
#     parser = argparse.ArgumentParser(description="Отримайте випадкову ідею для власного висловлення.")
#     parser.add_argument('--chance', type=float, default=0.5, help='Шанс отримання теми (за замовчуванням 50%)')
#     args = parser.parse_args()
#
#     #Лог запуску програми
#     logging.info("Програма запущена із шансом: %s", args.chance)
#
#     #Використання генератора для вибору теми
#     message = generator.get_random_message(args.chance)
#
#     #Виводимо результат
#     print(message)
#
# if __name__ == "__main__":
#     main()


import argparse
from message_pkg.generator import get_random_message


def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description="Генерация случайных тем или сообщений.")
    parser.add_argument('--chance', type=float, required=True, help="Шанс на получение случайной темы.")

    # Парсим аргументы командной строки
    args = parser.parse_args()

    print(f"Програма запущена із шансом: {args.chance}")
    # Вызываем функцию генерации сообщения с указанным шансом
    message = get_random_message(args.chance)
    print(message)


if __name__ == "__main__":
    main()

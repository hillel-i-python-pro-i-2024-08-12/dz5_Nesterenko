import argparse
from message_pkg.generator import get_random_message


def main():
    parser = argparse.ArgumentParser(description="Генерація випадкових тем або повідомлень.")
    parser.add_argument('--chance', type=float, required=True, help="Шанс на отримання випадкової теми.")

    args = parser.parse_args()

    message = get_random_message(args.chance)
    print(message)


if __name__ == "__main__":
    main()

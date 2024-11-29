""" Главная точка входа для запуска приложения """

from src.cli.interface import TaskManagerCLI


def main():
    """
    Главная функция для запуска CLI-приложения
    """
    cli = TaskManagerCLI()
    cli.run()


if __name__ == "__main__":
    main()

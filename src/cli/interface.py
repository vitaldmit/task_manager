""" Модуль для работы с интерфейсом CLI-приложения """

import re
from datetime import datetime

from src.services.task_manager import TaskManager
from src.models.task import Task
from src.utils.constants import PRIORITIES, STATUSES, CATEGORIES


class TaskManagerCLI:
    """
    Класс для работы с интерфейсом CLI-приложения
    """
    def __init__(self):
        self.task_manager = TaskManager()

    def display_menu(self):
        """
        Отображает главное меню CLI-приложения
        """
        print("\n=== Менеджер задач ===")
        print("1. Просмотр всех задач")
        print("2. Добавить задачу")
        print("3. Изменить задачу")
        print("4. Удалить задачу")
        print("5. Поиск задач")
        print("0. Выход")

    def run(self):
        """
        Запускает CLI-приложение
        """
        while True:
            self.display_menu()
            choice = input("\nВыберите действие: ")

            actions = {
                "1": self.show_tasks,
                "2": self.add_task,
                "3": self.edit_task,
                "4": self.delete_task,
                "5": self.search_tasks,
                "0": exit
            }

            action = actions.get(choice)
            if action:
                action()
            else:
                print("Неверный выбор. Попробуйте снова.")

    def show_tasks(self):
        """
        Отображает список задач
        """
        if not self.task_manager.tasks:
            print("Список задач пуст")
            return

        for task in self.task_manager.tasks:
            self._print_task(task)

    def add_task(self):
        """
        Добавляет новую задачу
        """
        title = input("Название задачи: ")
        if not title:
            print("Название задачи не может быть пустым")
            return

        description = input("Описание задачи: ")

        print("\nДоступные категории:", ", ".join(CATEGORIES))
        category = input("Категория: ")

        due_date = input("Срок выполнения (ГГГГ-ММ-ДД): ")
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', due_date):
            print("Неверный формат даты. Используйте формат ГГГГ-ММ-ДД")
            return

        print("\nПриоритеты:", ", ".join(PRIORITIES))
        priority = input("Приоритет: ")
        if priority not in PRIORITIES:
            print("Неверный приоритет. Выберите из списка:", ", ".join(PRIORITIES))
            return

        try:
            task = Task(
                id=0,  # будет сгенерирован автоматически
                title=title,
                description=description,
                category=category,
                due_date=datetime.fromisoformat(due_date),
                priority=priority
            )
            self.task_manager.add_task(task)
            print("Задача успешно добавлена!")
        except ValueError as e:
            print(f"Ошибка при создании задачи: {e}")

    def _print_task(self, task: Task):
        """
        Выводит меню при редактировании задачи
        """
        print(f"\nID: {task.id}")
        print(f"Название: {task.title}")
        print(f"Описание: {task.description}")
        print(f"Категория: {task.category}")
        print(f"Срок: {task.due_date.strftime('%Y-%m-%d')}")
        print(f"Приоритет: {task.priority}")
        print(f"Статус: {task.status}")
        print("-" * 30)

    def edit_task(self):
        """
        Редактирует задачу
        """
        task_id = int(input("Введите ID задачи для редактирования: "))
        task = self.task_manager.get_task_by_id(task_id)

        if not task:
            print("Задача не найдена")
            return

        print("\nТекущие данные задачи:")
        self._print_task(task)
        print("\nВведите новые данные (или оставьте пустым для сохранения текущего значения):")

        title = input("Название задачи: ") or task.title
        description = input("Описание задачи: ") or task.description

        print("\nДоступные категории:", ", ".join(CATEGORIES))
        category = input("Категория: ") or task.category

        due_date_str = input("Срок выполнения (ГГГГ-ММ-ДД): ")
        due_date = datetime.fromisoformat(due_date_str) if due_date_str else task.due_date

        print("\nПриоритеты:", ", ".join(PRIORITIES))
        priority = input("Приоритет: ") or task.priority

        print("\nСтатусы:", ", ".join(STATUSES))
        status = input("Статус: ") or task.status

        task.title = title
        task.description = description
        task.category = category
        task.due_date = due_date
        task.priority = priority
        task.status = status

        self.task_manager.save_tasks()
        print("Задача успешно обновлена!")

    def delete_task(self):
        """
        Удаляет задачу
        """
        task_id = int(input("Введите ID задачи для удаления: "))
        task = self.task_manager.get_task_by_id(task_id)

        if not task:
            print("Задача не найдена")
            return

        self._print_task(task)
        confirm = input("Вы уверены, что хотите удалить эту задачу? (да/нет): ")

        if confirm.lower() == 'да':
            self.task_manager.tasks = [t for t in self.task_manager.tasks if t.id != task_id]
            self.task_manager.save_tasks()
            print("Задача успешно удалена!")
        else:
            print("Удаление отменено")

    def search_tasks(self):
        """
        Выполняет поиск задач
        """
        print("\nПоиск задач:")
        print("1. По ключевому слову")
        print("2. По категории")
        print("3. По статусу")

        choice = input("Выберите тип поиска: ")

        if choice == "1":
            keyword = input("Введите ключевое слово: ").lower()
            results = [
                task for task in self.task_manager.tasks
                if keyword in task.title.lower() or keyword in task.description.lower()
            ]
        elif choice == "2":
            print("Доступные категории:", ", ".join(CATEGORIES))
            category = input("Введите категорию: ")
            results = self.task_manager.get_tasks_by_category(category)
        elif choice == "3":
            print("Доступные статусы:", ", ".join(STATUSES))
            status = input("Введите статус: ")
            results = [task for task in self.task_manager.tasks if task.status == status]
        else:
            print("Неверный выбор")
            return

        if results:
            print(f"\nНайдено задач: {len(results)}")
            for task in results:
                self._print_task(task)
        else:
            print("Задачи не найдены")

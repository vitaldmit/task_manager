""" Модуль для управления задачами. """

from typing import List, Optional

from src.models.task import Task
from src.services.file_handler import FileHandler
from src.utils.constants import DEFAULT_DATA_FILE


class TaskManager:
    """
    Класс для управления задачами.
    """
    def __init__(self, file_path: str = DEFAULT_DATA_FILE):
        self.file_handler = FileHandler(file_path)
        self.tasks: List[Task] = []
        self.load_tasks()

    def load_tasks(self) -> None:
        """
        Загружает задачи из файла
        """
        data = self.file_handler.read_data()
        self.tasks = [Task.from_dict(task_dict) for task_dict in data]

    def save_tasks(self) -> None:
        """
        Сохраняет задачи в файл
        """
        data = [task.to_dict() for task in self.tasks]
        self.file_handler.write_data(data)

    def add_task(self, task: Task) -> None:
        """
        Добавляет задачу в список задач
        """
        task.id = self._generate_id()
        self.tasks.append(task)
        self.save_tasks()

    def _generate_id(self) -> int:
        """
        Генерирует уникальный ID для задачи
        """
        return max((task.id for task in self.tasks), default=0) + 1

    def get_tasks_by_category(self, category: str) -> List[Task]:
        """
        Возвращает задачи по категории
        """
        return [task for task in self.tasks if task.category == category]

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Возвращает задачу по ID
        """
        return next((task for task in self.tasks if task.id == task_id), None)

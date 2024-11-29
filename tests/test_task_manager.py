import pytest
from datetime import datetime

from src.models.task import Task
from src.services.task_manager import TaskManager


@pytest.fixture
def task_manager(tmp_path):
    return TaskManager(tmp_path / "test_tasks.json")


@pytest.fixture
def sample_task():
    return Task(
        id=1,
        title="Тестовая задача",
        description="Test Description",
        category="Работа",
        due_date=datetime(2024, 12, 31),
        priority="Высокий"
    )


def test_add_task(task_manager, sample_task):
    task_manager.add_task(sample_task)
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0].title == "Тестовая задача"


def test_delete_task(task_manager, sample_task):
    task_manager.add_task(sample_task)
    initial_count = len(task_manager.tasks)
    task_manager.tasks = [t for t in task_manager.tasks if t.id != sample_task.id]
    assert len(task_manager.tasks) == initial_count - 1


def test_search_by_category(task_manager, sample_task):
    task_manager.add_task(sample_task)
    results = task_manager.get_tasks_by_category("Работа")
    assert len(results) == 1
    assert results[0].category == "Работа"

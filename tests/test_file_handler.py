import os
from typing import List, Dict, Any

import pytest
from src.services.file_handler import FileHandler


@pytest.fixture
def test_file_path():
    return "test_data.json"


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    return [
        {
            "id": "1",
            "title": "Test Task",
            "description": "Test Description",
            "category": "Работа",
            "due_date": "2023-12-31"
        }
    ]


@pytest.fixture
def file_handler(test_file_path):
    handler = FileHandler(test_file_path)
    yield handler
    # Удаляем файл после завершения теста
    if os.path.exists(test_file_path):
        os.remove(test_file_path)


def test_write_data(file_handler, sample_data):
    file_handler.write_data(sample_data)
    assert os.path.exists(file_handler.file_path)


def test_read_data(file_handler, sample_data):
    file_handler.write_data(sample_data)
    data = file_handler.read_data()
    assert data == sample_data


def test_empty_file_returns_empty_list(file_handler):
    data = file_handler.read_data()
    assert isinstance(data, list)
    assert len(data) == 0


def test_write_and_read_multiple_tasks(file_handler):
    test_data = [
        {
            "id": "1",
            "title": "Task 1",
            "description": "Description 1",
            "category": "Личное",
            "due_date": "2023-12-31"
        },
        {
            "id": "2",
            "title": "Task 2",
            "description": "Description 2",
            "category": "Работа",
            "due_date": "2024-01-01"
        }
    ]
    file_handler.write_data(test_data)
    read_data = file_handler.read_data()
    assert len(read_data) == 2
    assert read_data == test_data

""" Модуль для работы с файлами. Запись и чтение данных из файла """

import json
from pathlib import Path
from typing import List, Dict, Any


class FileHandler:
    """
    Класс для работы с файлами
    """
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def read_data(self) -> List[Dict[str, Any]]:
        """
        Читает данные из файла
        """
        if not self.file_path.exists():
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write_data(self, data: List[Dict[str, Any]]) -> None:
        """
        Записывает данные в файл
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

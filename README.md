# Менеджер задач
Консольное приложение для управления списком задач с возможностью добавления, выполнения, удаления и поиска задач.

## Возможности
- Просмотр всех текущих задач
- Просмотр задач по категориям (работа, личное, обучение)
- Добавление новых задач с указанием названия, описания, категории, срока и приоритета
- Редактирование существующих задач
- Отметка задач как выполненных
- Удаление задач
- Поиск по ключевым словам, категории или статусу

## Установка
1. Клонируйте репозиторий:
```bash
git clone https://github.com/vitaldmit/task_manager.git
cd task_manager
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
# или
venv\Scripts\activate  # Для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование
1. Запустите приложение: `python main.py`
2. Выберите опцию из меню и следуйте инструкциям.

## Запуск тестов
1. Для запуска тестов выполните следующую команду:
```bash
pytest tests/
```

## Структура проекта
```
task_manager/
│
├── src/
│   ├── models/
│   │   └── task.py
│   ├── services/
│   │   ├── task_manager.py
│   │   └── file_handler.py
│   ├── utils/
│   │   └── constants.py
│   └── cli/
│       └── interface.py
│
├── tests/
│   ├── test_task.py
│   ├── test_task_manager.py
│   └── test_file_handler.py
│
├── data/
│   └── tasks.json
│
├── requirements.txt
├── README.md
└── main.py
```

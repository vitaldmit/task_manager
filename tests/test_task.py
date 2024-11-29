from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    description: str
    category: str
    due_date: datetime
    priority: str
    status: str = "Не выполнена"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date.isoformat(),
            "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        data['due_date'] = datetime.fromisoformat(data['due_date'])
        return cls(**data)

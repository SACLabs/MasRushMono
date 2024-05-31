from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class TaskStatus(Enum):
    CREATED = "C"
    IN_PROGRESS = "P"
    COMPLETED = "X"
    FAILED = "F"


class TaskItem(BaseModel):
    # must have
    name: str
    description: str
    status: TaskStatus  # 确保TaskStatus是一个合适的枚举或者pydantic model
    # optional
    tags: List[str] = Field(default_factory=list)
    subtasks: List["TaskItem"] = Field(default_factory=list)
    owner: List = Field(default_factory=list)  # 确保owner的类型明确，如List[str]
    priority: Optional[int] = 0
    due_date: Optional[datetime] = None
    created_time: Optional[datetime] = Field(default_factory=datetime.now)
    updated_time: Optional[datetime] = None

    def update(self, attribute: str, new_value: Any):
        if attribute == "name":
            raise AttributeError("name cannot be updated")
        setattr(self, attribute, new_value)
        self.updated_time = datetime.now()


class TaskHistory(BaseModel):
    history: List[TaskItem] = Field(default_factory=list)

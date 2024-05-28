# TODO
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Any, Optional
from enum import Enum
import uuid

from message import Message
from graph import Graph

"""
如果把MAS系统当成一个群体智能系统，那么
task相当于是一个给MAS系统的prompt，尽量简单，无状态
"""

class TaskStatus(Enum):
    CREATED = "C"
    IN_PROGRESS = "P"
    COMPLETED = "X"
    FAILED = "F"

@dataclass
class TaskGraph:
    initial_input: Message
    entry_node: str
    exit_node: str = None
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: TaskStatus = TaskStatus.CREATED
    priority: int = 0
    sub_tasks: List['TaskGraph'] = field(default_factory=list)

@dataclass
class TaskItem:
    # must have
    name: str
    description: str
    status: TaskStatus
    # optional
    tags: Optional[List[str]] = field(default_factory=list)
    subtasks: Optional[List['TaskItem']] = field(default_factory=list)
    owner: Optional[List] = field(default_factory=list)
    priority: Optional[int] = 0
    due_date: Optional[datetime] = None
    created_time: Optional[datetime] = field(default_factory=datetime.now)

# @dataclass
# class TaskHistory:
#     time_stamp: datetime
#
# """history = {"t0": {C: "Task1@A", "Task2@B"}, {P: "Task2@B"}, {X: "Task1@A"}},
#            "t1": task_changed_state, }"""
#     history: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class TaskEvent:
    task: TaskItem
    update_time: datetime
    attribute: str
    old_value: Any
    new_value: Any


@dataclass
class TaskHistory:
    history: List[TaskEvent] = field(default_factory=list)

    def append_history(self, task: TaskItem, attribute: str, old: Any, new: Any):
        update_time = datetime.now()
        event = TaskEvent(task, update_time, attribute, old, new)
        self.history.append(event)

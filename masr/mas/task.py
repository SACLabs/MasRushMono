# TODO
from dataclasses import dataclass, field
from typing import Dict, List, Tuple
from enum import Enum
import uuid

from message import Message
from graph import Graph



class TaskStatus(Enum):
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

"""
如果把MAS系统当成一个群体智能系统，那么
task相当于是一个给MAS系统的prompt，尽量简单，无状态
"""
@dataclass
class Task:
    initial_input: Message
    entry_node: str
    exit_node:str  = None
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: TaskStatus = TaskStatus.CREATED
    priority: int = 0
    sub_tasks: List['Task'] = field(default_factory=list)

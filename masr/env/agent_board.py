# This class define the agent board
# used by env, env get the task implementation details from mas, and present the task state of each agent.

from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum
import uuid
# 不是demand board， 是agent的task board, 需要有个字符串去测试


class TaskStatus(Enum):
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Task:
    name: str
    description: str
    status: TaskStatus
    subtasks: List['Task'] = field(default_factory=list)
    owner: Optional[List] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))


def parse_task(task_from_mas: str) -> Task:
    # parse the task file from mas, store in dataclass Task(name, description, status, subtasks, owner)
    pass


if __name__ == "__main__":
    task_desc = """
    开发贪吃蛇游戏: in-progress, 创建一个简单的贪吃蛇游戏
        - 设置游戏界面
            -创建游戏窗口: created, 创建游戏窗口, agent a
            - 绘制游戏区域: in-progress, 绘制游戏区域, agent b
    """
    task = parse_task(task_desc)
    print(task)

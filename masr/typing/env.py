from masr.typing.message import Message
from typing import List

from masr.typing.graph import Graph
from masr.typing.task import TaskGraph


class Env2MAS(BaseModel):
    demand: str = None  # 用户的编码需求
    result: str = None  # 这里是源代码
    report: str = None  # 包含performance和CI通过率等·


class MAS2Env(BaseModel):
    result: str  # 这里是源代码
    history: str  # 从log中可以提取看板信息
    graph: Graph  # agent组织结构


class Algo2MAS(BaseModel):
    graph: Graph
    task: TaskGraph


class MAS2Algo(BaseModel):
    graph: Graph
    history: List[Message]

from archive.typing.message import Message
from typing import List
from pydantic import BaseModel, Dict

from archive.typing.graph import Graph
from archive.typing.task import TaskGraph
from archive.typing.task import TaskHistory


class Env2MAS(BaseModel):
    # RunningReport + Demand
    task_id: str = None # 任务的唯一ID
    demand: str = None  # 用户的编码需求
    pytest_result: Dict = None  # CI测试结果
    cprofile_performance: Dict = None  # cprofile performance·


class MAS2Env(BaseModel):
    task_id: str = None # 任务的唯一ID
    result: str  # 这里是源代码
    history: TaskHistory  # 从log中可以提取看板信息
    graph: Graph  # agent组织结构


class Algo2MAS(BaseModel):
    graph: Graph
    task: TaskGraph


class MAS2Algo(BaseModel):
    graph: Graph
    history: List[Message]

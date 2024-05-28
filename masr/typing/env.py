from masr.typing.message import Message
from typing import List, Dict, File


from masr.typing.graph import Graph
from masr.typing.task import TaskGraph

from pydantic import BaseModel

class Env2MAS(BaseModel):
    task_id: str = None # 任务的唯一ID
    demand: str = None  # 用户的编码需求
    run_shell: bytes  # sh文件
    pytest_result: Dict = None  # CI测试结果
    cprofile_performance: Dict = None  # cprofile performance·



class MAS2Env(BaseModel):
    task_id: str = None
    source_code: bytes  # 这里是源代码tar.gz文件
    history: str  # 从log中可以提取看板信息
    graph: Graph  # agent组织结构


class Algo2MAS(BaseModel):
    graph: Graph
    task: TaskGraph


class MAS2Algo(BaseModel):
    graph: Graph
    history: List[Message]

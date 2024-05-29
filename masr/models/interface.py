from typing import Dict

from pydantic import BaseModel

from .graph import GML
from .task import TaskHistory


class Demand(BaseModel):
    content: str


class Report(BaseModel):
    pytest_result: Dict
    cprofile_perfomance: Dict


class SourceCode(BaseModel):
    # Use tree dir to get the structure
    tree: str
    # {file_name: src_str}
    content: Dict[str, str]


def pack_env_to_mas_msg(
    task_id, demand: Demand, report: Report, src: SourceCode
) -> Dict:
    return {task_id: {"demand": demand, "report": report, "src": src}}


def pack_mas_to_env_msg(
    task_id, result: SourceCode, history: TaskHistory, graph: GML
) -> Dict:
    return {task_id: {"result": result, "history": history, "graph": graph}}

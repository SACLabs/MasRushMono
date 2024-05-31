# import uuid
from typing import Dict
from uuid import UUID

from pydantic import BaseModel

from masr.models.graph import GML
from masr.models.task import TaskHistory


class Demand(BaseModel):
    content: str
    test_file: Dict


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
    return {
        "task_id": task_id,
        "content": {"demand": demand, "report": report, "src": src},
    }


def pack_mas_to_env_msg(
    task_id: UUID, result: SourceCode, history: TaskHistory, graph: GML
) -> Dict:
    return {
        "task_id": task_id,
        "content": {"result": result, "history": history, "graph": graph},
    }

from masr.env_server.runner import pipeline
from masr.models.interface import pack_mas_to_env_msg, Report
from masr.models.task import TaskHistory, TaskItem, TaskStatus
from masr.models.graph import GML
from tests.test_base import task_id, report, source_code

from unittest.mock import patch
from unittest import mock

task = TaskItem(
    name="test task", description="test task description", status=TaskStatus.COMPLETED
)

history = TaskHistory(history=[task])

graph = GML(content="test graph")

pipeline_input = {
    "task_id": task_id,
    "content": {
        "result": source_code,
        "history": history,
        "graph": graph,
    },
}

runner_output = report


# TODO 实现pipeline循环
def test_pipeline():
    pipeline = mock.Mock()
    pipeline.return_value = report
    pipeline_output = pipeline(pipeline_input)
    assert pipeline_output == report


# TODO
def test_kanban():
    kanban = mock.Mock()
    kanban.return_value = None
    kanban_output = kanban(TaskHistory)

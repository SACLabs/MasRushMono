from masr.env_server.runner import pipeline, generate_code_project
from masr.models.interface import pack_mas_to_env_msg, Report
from masr.models.task import TaskHistory, TaskItem, TaskStatus
from tests.test_base import task_id, report, source_code, gml, task_desc

from unittest.mock import patch
from unittest import mock
import os
from pathlib import Path

task = task_desc

history = TaskHistory(history=[task])

graph = gml

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


def test_generate_source_code_project():
    source_code_path = generate_code_project(source_code)
    file_paths = []
    for dirpath, dirnames, filenames in os.walk(source_code_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_paths.append(file_path)
    assert len(file_paths) == len(source_code.content)
    for file_path in file_paths:
        file_test = Path(file_path).read_text()
        assert file_test == source_code.content[file_path.split('/tmp/')[1]]


# TODO
def test_kanban():
    kanban = mock.Mock()
    kanban.return_value = None
    kanban_output = kanban(TaskHistory)

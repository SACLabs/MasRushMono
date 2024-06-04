from masr.runtime.runner import (
    generate_code_project,
    run_pytest,
    run_cprofile,
)

from masr.runtime.monitor import pipeline

from masr.models.interface import pack_mas_to_env_msg, Report
from masr.models.task import TaskHistory, TaskItem, TaskStatus
from tests.test_base import task_id, report, source_code, gml, task_desc

from unittest.mock import patch
from unittest import mock
import os
from pathlib import Path
import shutil

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
        assert file_test == source_code.content[file_path.split("/tmp/")[1]]


def test_pytest():
    demand_dir = "/tmp/demand/pytest_demo"
    if os.path.exists(demand_dir):
        shutil.rmtree(demand_dir)
    os.makedirs(demand_dir)
    tests_dir = os.path.join(demand_dir, "tests")
    os.makedirs(tests_dir)
    test_main_path = os.path.join(tests_dir, "test_main.py")
    with open(test_main_path, "w") as f:
        f.write(
            """
def test_add():
    assert 1+ 1 == 2
"""
        )
    pytest_result = run_pytest(demand_dir)
    assert "coverage_report" in pytest_result
    assert "pytest_report" in pytest_result
    assert pytest_result["pytest_report"] == {"collected": 1, "passed": 1, "total": 1}
    assert pytest_result["coverage_report"][f"{demand_dir}/tests/test_main.py"][
        "summary"
    ] == {
        "covered_lines": 2,
        "num_statements": 2,
        "percent_covered": 100.0,
        "percent_covered_display": "100",
        "missing_lines": 0,
        "excluded_lines": 0,
    }


def test_cprofile():
    demand_dir = "/tmp/demand/cprofile_demo"
    if os.path.exists(demand_dir):
        shutil.rmtree(demand_dir)
    os.makedirs(demand_dir)
    main_file = f"{demand_dir}/main.py"
    with open(main_file, "w") as file:
        file.write(
            """
def add(a, b):
    return a+b
if __name__ == "__main__":
    add(1,1)
    """
        )
    # 写入运行脚本
    with open(f"{demand_dir}/run.sh", "w") as file:
        file.write("python -m cProfile -o output.prof main.py")
    cprofile_result = run_cprofile(demand_dir)
    assert "main.py:1:(<module>)" in cprofile_result
    assert "main.py:2:(add)" in cprofile_result


# TODO
def test_kanban():
    kanban = mock.Mock()
    kanban.return_value = None
    kanban_output = kanban(TaskHistory)

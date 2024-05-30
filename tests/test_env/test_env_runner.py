from masr.env_server.runner import pipeline
from masr.models.interface import pack_mas_to_env_msg, SourceCode, Report
from masr.models.task import TaskHistory, TaskItem, TaskStatus
from masr.models.graph import GML

from unittest.mock import patch

source_code = SourceCode(
    tree="procoder                \
            ├── functional.py       \
            ├── __init__.py         \
            ├── prompt              \
            │   ├── base.py         \
            │   ├── __init__.py     \
            │   ├── modules.py      \
            │   ├── proxy.py        \
            │   ├── sequential.py   \
            │   └── utils.py        \
            └── utils               \
                ├── __init__.py     \
                └── my_typing.py",
    content={
        "procoder/functional.py": "mock_functional_code",
        "procoder/__init__.py": "mock_init_code",
        "procoder/prompt/base.py": "mock base code",
        "procoder/prompt/__init__.py": "mock init code",
        "procoder/prompt/modules.py": "mock modules code",
        "procoder/prompt/proxy.py": "mock proxy code",
        "procoder/prompt/sequential.py": "mock sequential code",
        "procoder/prompt/utils.py": "mock utils code",
        "procoder/utils/__init__.py": "mock utils init code",
        "procoder/utils/my_typing.py": "mock my typing code",
    },
)

task = TaskItem(
    name = "test task",
    description = "test task description",
    status=TaskStatus.COMPLETED
)

history = TaskHistory(
    history = [task]
)

graph = GML(
    content = "test graph"
)

pipeline_input = {
    "task_id": "mock task id",
    "result": source_code,
    "history": history,
    "graph": graph
}


runner_output = Report(
    pytest_result = {"mock_pytest": "mock_pytest_output"},
    cprofile_perfomance = {"mock_cprofile": "mock_cprofile_output"}
)

def test_pipeline():
    with patch(pipeline) as mock_pipeline:
        mock_pipeline.return_value = Report(
        pytest_result= {"mock_pytest": "mock_pytest_output"},
        cprofile_perfomance= {"mock_cprofile": "mock_cprofile_output"}
        )
        pipeline_output = pipeline(pipeline_input)
        assert runner_output == pipeline_output

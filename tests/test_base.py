from datetime import datetime
from pathlib import Path
import uuid
from masr.models import interface
from masr.models.task import TaskStatus, TaskItem
import os

# read demand
# content
with open("demand/readme.md", "r", encoding="utf-8") as f:
    contents = f.read()
# test file
test_file = {}
for filename in os.listdir("demand/tests"):
    with open(
        os.path.join("demand/tests", filename), "r", encoding="utf-8"
    ) as f:
        test_file[filename] = f.read()
# mock demand data
demand = interface.Demand(
    demand_id=uuid.uuid4(), content=contents, test_file=test_file
)

gml = Path("tests/test.gml").read_text()

task_id = uuid.uuid4()


cprofile_perfomance = {
    "~:0:(<built-in method builtins.exec>)": {
        "ncalls": 1,
        "tottime": 1,
        "cumtime": 3.2230000000000003e-06,
    },
    "main.py:1:(sum)": {"ncalls": 1, "tottime": 1, "cumtime": 2.68e-07},
    "main.py:1:(<module>)": {"ncalls": 1, "tottime": 1, "cumtime": 1.54e-06},
    "~:0:(<method 'disable' of '_lsprof.Profiler' objects>)": {
        "ncalls": 1,
        "tottime": 1,
        "cumtime": 1.4500000000000001e-07,
    },
}


pytest_result = {
    "passed": 3,
    "total": 3,
    "collected": 3,
    "coverage": 0.95,
}

report = interface.Report(
    pytest_result=pytest_result, cprofile_perfomance=cprofile_perfomance
)

source_code = interface.SourceCode(
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

task_desc = TaskItem(
    name="Task_A",
    description="This is an example task.",
    status=TaskStatus.IN_PROGRESS,
    tags=["project1"],
    owner=["agent1", "agent2"],
    priority=1,
    due_date=datetime(2024, 6, 30),
    subtasks=[
        TaskItem(
            name="Task_A_1",
            description="This is the first subtask.",
            status=TaskStatus.CREATED,
            owner=["agent1"],
            priority=2,
        ),
        TaskItem(
            name="Subtask_A_2",
            description="This is the second subtask.",
            status=TaskStatus.COMPLETED,
            owner=["agent2"],
            priority=1,
        ),
    ],
)

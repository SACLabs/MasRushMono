from masr.models import interface


mock_task_id = "mock_task_id"
mock_demand = interface.Demand(content="mock demand")
mock_report = interface.Report(
    pytest_result={"pytest_key": "pytest_value"},
    cprofile_perfomance={"cprofile_key": "cprofile_value"},
)
mock_code = interface.SourceCode(
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

mock_sender = lambda x: x


def test_sender_data_format():
    sender_data = interface.pack_env_to_mas_msg(
        mock_task_id, mock_demand, mock_report, mock_code
    )
    assert "task_id" in sender_data
    assert sender_data["task_id"] == mock_task_id

    assert "demand" in sender_data
    assert sender_data["demand"] == mock_demand

    assert "report" in sender_data
    assert sender_data["report"] == mock_report

    assert "src" in sender_data
    assert sender_data["src"] == mock_code


def test_reciever_data_format():
    sender_data = interface.pack_env_to_mas_msg(
        mock_task_id, mock_demand, mock_report, mock_code
    )
    reciever_data = mock_sender(sender_data)
    assert sender_data == reciever_data

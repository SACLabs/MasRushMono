from masr.models import interface


from tests.test_base import source_code, gml, task_desc
from masr.models.task import TaskHistory
from tests.test_base import task_id, report, source_code

mock_task_id = task_id
mock_code = source_code
mock_graph = gml
mock_history = TaskHistory(history=[task_desc])

demand = interface.Demand(content="mock demand")


def mock_sender(x):
    return x


def test_mas_sender_format():
    sender_data = interface.pack_mas_to_env_msg(
        task_id=mock_task_id,
        result=mock_code,
        history=mock_history,
        graph=mock_graph,
    )
    assert "task_id" in sender_data
    assert sender_data["task_id"] == mock_task_id

    assert "result" in sender_data["content"]
    assert sender_data["content"]["result"] == mock_code

    assert "history" in sender_data["content"]
    assert sender_data["content"]["history"] == mock_history

    assert "graph" in sender_data["content"]
    assert sender_data["content"]["graph"] == mock_graph


def test_mas_reciever_format():
    sender_data = interface.pack_env_to_mas_msg(
        task_id, demand, report, mock_code
    )
    reciever_data = mock_sender(sender_data)
    assert sender_data == reciever_data

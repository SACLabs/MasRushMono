from masr.models import interface
import uuid

from tests.test_base import source_code, gml, task_desc
from masr.models.task import TaskHistory

mock_task_id = uuid.uuid4()
mock_code = source_code
mock_graph = gml
mock_history = TaskHistory(history=[task_desc])


def mock_sender(x):
    return x


def test_sender_data_format():
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


def test_reciever_data_format():
    sender_data = interface.pack_env_to_mas_msg(
        mock_task_id, mock_code, mock_history, mock_graph
    )
    reciever_data = mock_sender(sender_data)
    assert sender_data == reciever_data

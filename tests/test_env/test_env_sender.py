from masr.models import interface
from tests.test_base import task_id, report, source_code, demand

mock_demand = demand


# TODO, 之后需要改成真正的发送
mock_sender = lambda x: x


def test_sender_data_format():
    sender_data = interface.pack_env_to_mas_msg(
        task_id, demand, report, source_code
    )
    assert "task_id" in sender_data
    assert sender_data["task_id"] == task_id

    sender_content = sender_data["content"]

    assert "demand" in sender_content
    assert sender_content["demand"] == mock_demand

    assert "report" in sender_content
    assert sender_content["report"] == report

    assert "src" in sender_content
    assert sender_content["src"] == source_code


def test_reciever_data_format():
    sender_data = interface.pack_env_to_mas_msg(
        task_id, mock_demand, report, source_code
    )
    reciever_data = mock_sender(sender_data)
    assert sender_data == reciever_data

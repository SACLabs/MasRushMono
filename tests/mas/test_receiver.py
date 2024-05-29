"""
这部分测试将检查 FastAPI 应用是否正确接收数据并将其存储到 Redis 中。
"""


import pytest

from fastapi.testclient import TestClient
from masr.mas.receiver import app
from masr.mas.main import pipeline
from masr.typing.env import Env2MAS, MAS2Env
from unittest.mock import patch, AsyncMock
from masr.typing.task import TaskGraph, TaskHistory
from masr.typing.graph import Graph


client = TestClient(app)


@pytest.fixture
def mock_message():
    return {
        "message": Env2MAS()
    }


def test_receive_message():
    # 发送一条消息到接收端
    response = client.post("/receive_from_env/", json={"message": mock_message})
    assert response.status_code == 200
    assert response.json() == {"message": "Data received and added to Redis"}
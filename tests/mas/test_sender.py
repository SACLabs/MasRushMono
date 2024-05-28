import pytest
from masr.mas.sender import sending_from_mas_to_env
import httpx
from masr.typing.env import MAS2Env
from unittest.mock import patch, AsyncMock
from masr.typing.task import TaskGraph, TaskHistory
from masr.typing.graph import Graph

@pytest.fixture
def mock_httpx(mocker):
    return patch('httpx.AsyncClient.post', new_callable=AsyncMock)

@pytest.mark.asyncio
async def test_sending_from_mas_to_env(mock_httpx):
    url = "http://env_server:8002"
    data = MAS2Env(task_id="1", result="test_result", history=TaskHistory(), graph=Graph(nodes={}, edges=[]))
    mock_httpx.return_value.json.return_value = {"response": "mocked"}
    
    response = await sending_from_mas_to_env(url, data)
    assert response["message"] == "Data sent to env"
    mock_httpx.assert_called_once_with(f"{url}/receive_from_mas", json=data)


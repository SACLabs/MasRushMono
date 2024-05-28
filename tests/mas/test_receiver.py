import pytest
import pathlib
import sys
folder_path = pathlib.Path(__file__)
sys.path.append(str(folder_path.parent.parent.parent))
from fastapi.testclient import TestClient
from masr.mas.receiver import app
from masr.mas.main import pipeline
from masr.typing.env import Env2MAS, MAS2Env
from unittest.mock import patch, AsyncMock
from masr.typing.task import TaskGraph, TaskHistory
from masr.typing.graph import Graph


client = TestClient(app)

@pytest.fixture
def mock_pipeline(mocker):
    return mocker.patch('receiver.pipeline', new_callable=AsyncMock)

@pytest.fixture
def mock_sending(mocker):
    return mocker.patch('sender.sending_from_mas_to_env', new_callable=AsyncMock)

def test_receiving_endpoint(mock_pipeline, mock_sending):
    message = {"task_id": "1", "demand": "test_demand", "pytest_result": {}, "cprofile_performance": {}}
    mock_pipeline.return_value = MAS2Env(task_id="1", result="result", history=TaskHistory(), graph=Graph())
    response = client.post("/receive_from_env/", json=message)
    assert response.status_code == 200
    mock_pipeline.assert_called_once()
    mock_sending.assert_called_once()

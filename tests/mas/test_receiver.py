import pytest
from fastapi.testclient import TestClient
from masr.mas.receiver import app
from masr.mas.main import pipeline

client = TestClient(app)

@pytest.fixture
def mock_pipeline(mocker):
    return mocker.patch('receiver.pipeline')

@pytest.fixture
def mock_sending(mocker):
    return mocker.patch('sender.sending_from_mas_to_env')

def test_receiving_endpoint(mock_pipeline, mock_sending):
    message = {"data": "test"}
    mock_pipeline.return_value = message
    response = client.post("/receive_from_env/", json=message)
    assert response.status_code == 200
    mock_pipeline.assert_called_once_with(message)
    mock_sending.assert_called_once()

import pytest
from masr.mainloop import Mas, Env, Report, mainloop
import uuid


@pytest.fixture
def mock_task_config():
    return {"task_id": uuid.uuid4()}


@pytest.fixture
def mock_env():
    return Env()


@pytest.fixture
def mock_mas():
    return Mas()


@pytest.mark.asyncio
async def test_mainloop_success(mock_task_config, mock_env, mock_mas):
    # Mock methods to always return success
    async def mock_send_success(url):
        return "SUCCESS"

    async def mock_check_success(promise):
        return Report(status="SUCCESS")

    mock_env.send = mock_send_success
    mock_mas.send = mock_send_success
    mock_env.check = mock_check_success

    await mainloop(mock_task_config, mock_env, mock_mas)
    assert mock_env._success is True


@pytest.mark.asyncio
async def test_mainloop_failure(mock_task_config, mock_env, mock_mas):
    # Mock methods to alternate success and failure
    async def mock_send_success(url):
        return "SUCCESS"

    async def mock_check_failure(promise):
        return Report(status="FAILURE")

    mock_env.send = mock_send_success
    mock_mas.send = mock_send_success
    mock_env.check = mock_check_failure

    await mainloop(mock_task_config, mock_env, mock_mas)
    assert mock_env._success is False


if __name__ == "__main__":
    pytest.main()

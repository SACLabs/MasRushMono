import pytest
from masr.mainloop import mainloop
import asyncio
import uuid


async def send(url):
    await asyncio.sleep(1)
    return "SUCCESS"


class Env:
    def __init__(self):
        self.url = "http://mas.url"
        self._success = False

    def init(self, task_config):
        pass

    async def run(self):
        return not self._success

    async def send(self, url):
        await asyncio.sleep(1)
        return "SUCCESS"

    async def check(self, promise):
        await asyncio.sleep(1)
        return Report(status="SUCCESS")  # Mocked success for simplicity

    def set_success_flag(self, tid):
        self._success = True


class Mas:
    def __init__(self):
        self.url = "http://env.url"

    def init(self, task_config):
        pass

    async def send(self, url):
        await asyncio.sleep(1)
        return "SUCCESS"

    async def handel_failure(self, report):  # start again if fail
        print("Handeling failure", report)


class Report:
    def __init__(self, status):
        self.status = status


@pytest.fixture
def mock_task_config():
    return {
        uuid.uuid4(): {"demand": "task123", "report": "good", "src": "code"}
    }


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

import pytest

pytestmark = pytest.mark.skip(
    reason="Skipping all tests in this file temporarily."
)

from masr.mainloop import mainloop
from tests.mainloop.test_base import Env, Mas
from tests.test_base import task_id, report, source_code
from masr.models.interface import pack_env_to_mas_msg, Demand

demand = Demand(content="mock demand")


@pytest.fixture
def mock_task_config():
    return pack_env_to_mas_msg(task_id, demand, report, source_code)


@pytest.fixture()
def env():
    return Env("http://env.url")


@pytest.fixture()
def mas():
    return Mas("http://mas.url")


@pytest.mark.asyncio
async def test_mainloop_success(mock_task_config, env, mas):
    # Mock methods to always return success
    async def mock_send_success(url, task_config):
        return "SUCCESS"

    async def mock_receive_success(url):
        return mock_task_config

    async def mock_perform_test_success():
        env._success = True

    env.send = mock_send_success
    mas.receive = mock_receive_success
    env.perform_test = mock_perform_test_success

    await mainloop(mock_task_config, env, mas)
    assert env._success is True


@pytest.mark.asyncio
async def test_mainloop_failure(mock_task_config, env, mas):
    # Mock methods to alternate success and failure
    async def mock_send_success(url):
        return "SUCCESS"

    async def mock_receive_success(url):
        return mock_task_config

    async def mock_perform_test_failure(promise):
        env._success = False

    env.send = mock_send_success
    mas.receive = mock_receive_success
    env.perform_test = mock_perform_test_failure

    await mainloop(mock_task_config, env, mas)
    assert env._success is False


if __name__ == "__main__":
    pytest.main()

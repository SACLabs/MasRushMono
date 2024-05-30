import pytest
import asyncio
from unittest.mock import AsyncMock, Mock, patch
from fastapi.testclient import TestClient
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from enum import Enum
from fastapi import FastAPI
import uuid

from masr.models.interface import pack_env_to_mas_msg, Demand, Report, SourceCode

task_id = uuid.uuid4()
report = Report(pytest_result={'pytest_key': 'pytest_value'}, cprofile_test={'cprofile_key': 'cprofile_value'})
demand = Demand(content='this is a demand')
src = SourceCode(tree="procoder\
            ├── functional.py       \
            ├── __init__.py         \
            ├── prompt              \
            │   ├── base.py         \
            │   ├── __init__.py     \
            │   ├── modules.py      \
            │   ├── proxy.py        \
            │   ├── sequential.py   \
            │   └── utils.py        \
            └── utils               \
                ├── __init__.py     \
                └── my_typing.py",
                 content={"procoder/functional.py": "mock_functional_code",
                          "procoder/__init__.py": "mock_init_code",
                          "procoder/prompt/base.py": "mock base code",
                          "procoder/prompt/__init__.py": "mock init code",
                          "procoder/prompt/modules.py": "mock modules code",
                          "procoder/prompt/proxy.py": "mock proxy code",
                          "procoder/prompt/sequential.py": "mock sequential code",
                          "procoder/prompt/utils.py": "mock utils code",
                          "procoder/utils/__init__.py": "mock utils init code",
                          "procoder/utils/my_typing.py": "mock my typing code"})


@pytest.fixture()
def mock_send_env_data():
    return pack_env_to_mas_msg(task_id, demand, report, src)


@pytest.fixture()
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

env_app = FastAPI()
mas_app = FastAPI()

client_env = TestClient(env_app)
@env_app.post("/send_env")
async def send_env(mock_send_env_data):


@pytest.mark.asyncio
async def test_env_sends_data_to_mas(mock_env_to_mas_data):
    response = await client_env.post("/send-to-mas", json=mock_env_to_mas_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Data sent to MAS"}
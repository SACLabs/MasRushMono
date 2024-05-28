# ENV2MAS
from typing import Dict
from masr.typing.env import MAS2Env
import httpx


async def send_message_from_mas_to_env(ENV_SERVER_URL: str, demand: str, pytest_result: Dict,
                                       cprofile_result: Dict) -> None:
    send_message = MAS2Env(demand, pytest_result, cprofile_result)
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{ENV_SERVER_URL}/receive_from_env", json=send_message)

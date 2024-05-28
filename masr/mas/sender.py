# MAS2Env
from masr.typing.env import MAS2Env
import httpx

async def sending_from_mas_to_env(ENV_SERVER_URL, data: MAS2Env):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{ENV_SERVER_URL}/receive_from_mas", json=data)
    return {"message": "Data sent to env", "response": response.json()}


# ENV2MAS
import requests
from masr.typing.env import Env2MAS
from masr.config import MASSERVER, MASSERVERPORT


def send_message_from_mas_to_env(env_to_mas_data: Env2MAS) -> None:
    response = requests.post(
        f"http://{MASSERVER}:{MASSERVERPORT}/receive_from_env/",
        json=env_to_mas_data.model_dump()
    )

    return "success" if response.status_code == 200 else "send faliure"

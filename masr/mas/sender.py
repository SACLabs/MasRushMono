# MAS2Env
from masr.typing.env import MAS2Env
import redis
import time
import requests
from masr.mas.config import ENV_SERVER_URL, REDIS_URL

redis_client = redis.from_url(
            REDIS_URL,
            decode_responses=True,
            encoding="utf8",
        )


# 用于发送处理过的消息到指定的URL
def sender():
    while True:
        # 尝试从Redis获取处理过的消息
        message = redis_client.brpop("send_queue", 0)
        if message:
            try:
                # 发送消息到外部URL
                # message返回是一个元组，第二个元素是数据
                response = requests.post(ENV_SERVER_URL, json={"data": message[1].decode('utf-8')})
                print(f"Message sent with response: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to send message: {str(e)}")
        time.sleep(1)

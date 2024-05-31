import time

import redis
import requests


def gen_sender(dtypes, target):
    redis_client = redis.from_url(
        # TODO:REDIS_URL,
        decode_responses=True,
        encoding="utf-8",
    )

    def sender():
        while True:
            # 根据 dtypes 从对应队列获取消息
            message = redis_client.brpop(f"{dtypes}_send_queue", 0)
            if message:
                try:
                    response = requests.post(target, json=message)
                    response.raise_for_status()
                except requests.RequestException as e:
                    print(f"{dtypes}, {target}, sender error: {str(e)}")
            time.sleep(1)

    return sender


"""
sender = gen_sender(dtypes='MAS', target="http://example.com:8080")
import threading

sender_thread = threading.Thread(target=sender)
sender_thread.start()
"""

import requests
import redis
import time

def gen_sender(dtypes, target):
    redis_client = redis.from_url(
        # TODO:REDIS_URL,
        decode_responses = True,
        encoding = "utf-8"
    )
    
    def sender(data):
        while True:
            # 根据 dtypes 从对应队列获取消息
            message = redis_client.brpop(f"{dtypes}_send_queue", 0)
            if message:
                try:
                    resposne = requests.post(target, json=message)
                except requests.RequestException as e:
                    print(f"{dtypes}, {target}, sender error: {str(e)}")
            time.sleep(1)
    return sender
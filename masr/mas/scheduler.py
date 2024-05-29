import redis
import time
from masr.mas.config import ENV_SERVER_URL, REDIS_URL
from masr.mas.main import pipeline

redis_client = redis.from_url(
            REDIS_URL,
            decode_responses=True,
            encoding="utf8",
        )


def scheduler():
    while True:
        # 尝试从Redis获取消息
        message = redis_client.brpop("message_queue", 0)
        if message:
            # message返回是一个元组，第二个元素是数据
            result = pipeline(message[1].decode('utf-8'))
            # 处理完的消息送入另一个Redis队列等待发送
            redis_client.lpush("send_queue", result)
        time.sleep(1)  # 适当休息避免过度消耗CPU


if __name__ == "__main__":
    scheduler()
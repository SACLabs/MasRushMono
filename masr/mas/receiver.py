import redis
from fastapi import FastAPI, HTTPException
from masr.mas.main import pipeline
from masr.mas.sender import sending_from_mas_to_env
from masr.typing.env import Env2MAS
from masr.mas.config import ENV_SERVER_URL, REDIS_URL


# async def receiving(message: Env2MAS):
#     processed_message = await pipeline(message)
#     await sending_from_mas_to_env(ENV_SERVER_URL, processed_message)
#     return {"status": "Message processed and sent"}


app = FastAPI()
redis_client = redis.from_url(
            REDIS_URL,
            decode_responses=True,
            encoding="utf8",
        )


@app.post("/receive_from_env/")
async def receiving(message: Env2MAS):
    try:
        # 将数据作为消息推入Redis的列表（队列）
        redis_client.lpush("message_queue", message)
        return {"message": "Data received and added to Redis"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5252)
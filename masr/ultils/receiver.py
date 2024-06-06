import redis
from fastapi import FastAPI, HTTPException


def gen_receiver(dtypes):
    app = FastAPI()
    redis_client = redis.from_url(
        # REDIS_URL
        "redis://localhost:6379",
        decode_responses=True,
        encoding="utf-8",
    )

    @app.post("/receive/")
    async def receiver(message: dict):
        try:
            redis_client.lpush(f"{dtypes}_message_queue", message)
            return {"message": "Data received and added to Redis"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return app


"""
def start_app():
    from marsr.ultils import gen_receiver

    app = gen_receiver(dtypes='MAS')
    uvicorn.run(app, host='0.0.0.0', port=5252)
"""

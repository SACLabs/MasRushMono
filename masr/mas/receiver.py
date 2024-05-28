from fastapi import FastAPI
from masr.mas.main import pipeline
from masr.mas.sender import sending_from_mas_to_env
from masr.typing.env import Env2MAS

app = FastAPI()
ENV_SERVER_URL = "http://env_server:8002"

@app.post("/receive_from_env/")
async def receiving(message: Env2MAS):
    processed_message = await pipeline(message)
    await sending_from_mas_to_env(ENV_SERVER_URL, processed_message)
    return {"status": "Message processed and sent"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5252)

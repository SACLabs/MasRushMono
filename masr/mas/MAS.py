"""负责与algo或env系统的交互接口
ENV -- --> MAS -> ALGO -> MAS -> ENV

"""

from fastapi import FastAPI, File, UploadFile
import httpx
import uvicorn
from pydantic import BaseModel
from singleton import singleton
from typing import List

from message import Message
from task import Task
from graph import Graph

app = FastAPI()

ALGORITHM_SERVER_URL = "http://algorithm_server:8001"
ENV_SERVER_URL = "http://env_server:8002"

class Algo2MAS(BaseModel):
    graph: Graph
    task: Task

class MAS2Algo(BaseModel):
    graph: Graph
    history: List[Message]

class Env2MAS(BaseModel):
    score: str

    
class MAS2Env(BaseModel):
    result: str
    performance: str
    graph: Graph


@singleton
class MAS:
    def __init__(self, graph=None):
        if not hasattr(self, 'initialized'):  # 确保初始化只执行一次
            self.graph = graph
            self.initialized = True
            self.graph.init()
        elif graph is not None and graph != self.graph:
            self.parse_and_update_graph(graph)

    def parse_and_update_graph(self, new_graph):
        # 解析新旧graph的不同并更新实例
        pass

    def run(self, task):
        self.graph.run(task)

@app.post("/to_algorithm/")
async def send_to_algorithm(data: MAS2Algo):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{ALGORITHM_SERVER_URL}/receive_from_mas", json=data)
    return {"message": "Data sent to algorithm", "response": response.json()}


@app.post("/receive_from_algorithm/")
async def receive_from_algorithm(data: Algo2MAS):
    # 算法给MAS下发运行命令，MAS运行后将结果推给ENV

    graph = data.graph # 从algorithm接收到的数据包含Graph
    task = data.task # 从algorithm接收到的数据包含Task
    
    # 实例化MAS
    mas = MAS(graph)
    # 运行MAS
    mas.run(task)

    # 获取MAS的输出
    final_output = mas.get_final_result(task)
    performance = mas.get_resource_usage(task)


    # 将MAS的输出发送给ENV,结束
    return send_to_env(MAS2Env(result=final_output, performance=performance, graph=mas.graph))
    

@app.post("/receive_from_env/")
async def receive_from_env(data: Env2MAS):
    # 处理从 env 接收到的数据
    return {"message": "Data received from env", "data": data}

@app.post("/to_env/")
async def send_to_env(data: MAS2Env):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{ENV_SERVER_URL}/receive_from_mas", json=data)
    return {"message": "Data sent to env", "response": response.json()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
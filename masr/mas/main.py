"""负责mas系统的runing
ENV -- --> MAS -> ALGO -> MAS -> ENV
"""

from singleton import singleton

from masr.typing.env import Env2MAS, MAS2Env, Algo2MAS, MAS2Algo




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
    
    def get_result(self, task_id):
        pass

    def get_log(self, task_id):
        pass


async def pipeline(data: Env2MAS) -> MAS2Env:
    #算法处理
    res = await algorithm(data)
    task_id = res.task_id
    task = res.task
    graph = res.graph
    # 实例化、运行MAS
    mas = MAS(graph)
    mas.run(task)

    # 获取MAS的输出（源代码）和日志
    result = mas.get_result(task_id)
    history = mas.get_log(task_id)

    return MAS2Env(task_id=task_id, graph=graph, result=result, history=history)


async def algorithm(data:Env2MAS) -> Algo2MAS:
    # 将Env2MAS进行处理，变成MAS2Algo的形式
    data_to_algo = process_Env2MAS_data(data)
    # 丢给Algo模块处理，返回下一步的运行结果
    res = await send_to_algorithm(data_to_algo)  
    return res


def process_Env2MAS_data(data: Env2MAS) -> MAS2Algo:
    pass

async def send_to_algorithm(data: MAS2Algo) -> Algo2MAS:
    pass

# ALGORITHM_SERVER_URL = "http://algorithm_server:8001"



# @app.post("/to_algorithm/")
# async def send_to_algorithm(data: MAS2Algo):
#     async with httpx.AsyncClient() as client:
#         response = await client.post(f"{ALGORITHM_SERVER_URL}/receive_from_mas", json=data)
#     return {"message": "Data sent to algorithm", "response": response.json()}


# @app.post("/receive_from_algorithm/")
# async def receive_from_algorithm(data: Algo2MAS):
#     # 算法给MAS下发运行命令，MAS运行后将结果推给ENV

#     graph = data.graph # 从algorithm接收到的数据包含Graph
#     task = data.task # 从algorithm接收到的数据包含Task
    
#     # 实例化MAS
#     mas = MAS(graph)
#     # 运行MAS
#     mas.run(task)

#     # 获取MAS的输出
#     final_output = mas.get_final_result(task)
#     performance = mas.get_resource_usage(task)


#     # 将MAS的输出发送给ENV,结束
#     await send_to_env(MAS2Env(result=final_output, performance=performance, graph=mas.graph))

# user给出使用的demand，包括软件编写任务的description和测试文件
from dataclasses import dataclass
import subprocess


@dataclass
class Demand:
    demand: str = None
    owner: str = None

    def __type_match__(self, demand:str, owner:str):
        demand_list = self.demand.split(";")
        self.demand_task = next((val.split(':')[1] for val in demand_list if val.startswith('task:')), None)
        self.demand_test = next((val.split(':')[1] for val in demand_list if val.startswith('test:')), None)

    def __coverage__(self):
        self.coverage = subprocess.run('python main.py')

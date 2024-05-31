from typing import Dict
import asyncio
from uuid import UUID
import httpx
from masr.models.interface import Demand, SourceCode


# TODO: 实现env功能
class Env:
    def __init__(self, url):
        self.url = url
        self._success = False

    async def run(self):
        return not self._success

    # env send to mas
    async def send(self, url, task_config: Dict):
        await asyncio.sleep(1)
        print(f"env send data to {url}")

    # env receive from mas
    async def receive(self, task_return: Dict):
        # handel received data: present kanban and graph
        print(f"env received data {task_return}")
        await asyncio.sleep(1)

    # perform pytest and cprofile test
    async def perform_test(self):
        await asyncio.sleep(1)
        test_results = 'SUCCESS'
        self._success = (test_results == 'SUCCESS')
        print(f"env performed test, success")

    def set_success_flag(self, demand_id: UUID):
    # present to user the task is complete
        print(f"demand {demand_id} is success")


# TODO: 实现mas功能
class Mas:
    def __init__(self, url):
        self.url = url

    async def send(self, url, task_return: Dict):
        await asyncio.sleep(1)
        print(f"returned data sent to {url}")

    async def receive(self, url):
        # handel received data into the pipeline
        await asyncio.sleep(1)
        print(f"env received data from {url}")


    async def handel_failure(self, report):  # start again if fail
        # implement to logi of handelling failure
        print("Handeling failure", report)

    def set_success_flag(self, demand_id:UUID):
        print(f"task {demand_id} is marked as success")

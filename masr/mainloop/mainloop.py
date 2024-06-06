import asyncio
from typing import Awaitable

import redis.asyncio as redis

from masr.mainloop.wrapper import EnvWrapper, MasWrapper
from masr.models.interface import EnvOutput


class Promise:
    def __init__(self, coro):
        self._coro = coro
        self._future = asyncio.ensure_future(coro)

    def __await__(self):
        return self._future.__await__()


class TaskPromise:
    def __init__(self, promise_handler):
        self._promise_handler = promise_handler
        self._promise = None

    @property
    def promise(self):
        return self._promise

    @promise.setter
    def promise(self, promise):
        self._promise = promise
        self._promise_handler(self._promise)


def create_task_promise(coro: Awaitable) -> TaskPromise:
    promise = Promise(coro)
    task_promise = TaskPromise(lambda p: asyncio.create_task(p))
    task_promise.promise = promise
    return task_promise


async def env_loop(r: redis.Redis, task_config: EnvOutput):
    env = EnvWrapper(r)
    while True:
        # step 1: env send task_config to mas if there is a new task
        await env.send(task_config)

        # step 2: env receive task from redis, if there is a completed task
        mas_promise = create_task_promise(env.receive(task_config.task_id))
        mas_output = await mas_promise.promise

        # step 3: env perform pipeline
        task_config = await env.perform_pipeline(mas_output)

        # step 4: judge if the test is passed and task is completed
        if env.success:
            break


async def mas_loop(r: redis.Redis, stop_event: asyncio.Event):
    mas = MasWrapper(r)
    while not stop_event.is_set():
        # step 1: mas receive message from redis
        env_promise = create_task_promise(mas.receive())
        env_output = await env_promise.promise

        # step 2: mas perform pipeline
        task_return = await mas.perform_pipeline(env_output)

        # step 3: mas send result to redis
        await mas.send(task_return)


async def main_loop(task_configs: list[EnvOutput], r: redis.Redis):
    # 创建停止信号
    stop_event = asyncio.Event()
    # 创建任务列表
    env_tasks = [
        asyncio.create_task(env_loop(r, task_config))
        for task_config in task_configs
    ]
    mas_task = asyncio.create_task(mas_loop(r, stop_event))
    # 并发执行
    await asyncio.gather(*env_tasks)
    # stop when env finished
    stop_event.set()
    # await for mas finish
    await mas_task

import asyncio
import uuid
from typing import Any, cast

import redis.asyncio as redis

from masr.models.interface import EnvOutput, MASOutput


class EnvWrapper:

    def __init__(self, r: redis.Redis):
        self.r = r
        self._success = False

    async def send(self, env_output: EnvOutput) -> None:
        # 需要具体实现send2redis的通讯。
        await cast(Any, self.r.rpush("demand_queue", env_output.json()))

    async def receive(self, task_id: uuid.UUID) -> MASOutput:
        # 需要具体实现redis2env的通讯
        result = await cast(Any, self.r.blpop([f"result_queue:{task_id}"]))
        return MASOutput.parse_raw(result[1])

    async def perform_pipeline(self, mas_output: MASOutput):
        # 需要具体call env.pipeline()
        await asyncio.sleep(1)
        self._success = True

    @property
    def success(self):
        return self._success


class MasWrapper:

    def __init__(self, r: redis.Redis):
        self.r = r

    async def send(self, mas_output: MASOutput):
        # 需要具体实现mas2redis 的通讯
        await cast(
            Any,
            self.r.rpush(
                f"result_queue:{mas_output.task_id}", mas_output.json()
            ),
        )

    async def receive(self) -> EnvOutput:
        # 需要具体实现redis2mas的通讯
        msg = await cast(Any, self.r.blpop(["demand_queue"]))
        return EnvOutput.parse_raw(msg[1])

    async def perform_pipeline(self, env_output: EnvOutput):
        # 需要具体call mas.pipeline()
        await asyncio.sleep(1)

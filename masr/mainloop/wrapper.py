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
        await cast(Any, self.r.rpush("demand_queue", env_output.json()))

    async def receive(self, task_id: uuid.UUID) -> MASOutput:
        result = await cast(Any, self.r.blpop([f"result_queue:{task_id}"]))
        return MASOutput.parse_raw(result[1])

    async def perform_pipeline(self, mas_output: MASOutput):
        # test implementation
        await asyncio.sleep(1)
        self._success = True

    @property
    def success(self):
        return self._success


class MasWrapper:

    def __init__(self, r: redis.Redis):
        self.r = r

    async def send(self, mas_output: MASOutput):
        await cast(
            Any,
            self.r.rpush(
                f"result_queue:{mas_output.task_id}", mas_output.json()
            ),
        )

    async def receive(self) -> EnvOutput:
        msg = await cast(Any, self.r.blpop(["demand_queue"]))
        return EnvOutput.parse_raw(msg[1])

    async def perform_pipeline(self, env_output: EnvOutput):
        # write pipeline
        await asyncio.sleep(1)

import asyncio

# from typing import Dict
# import uuid


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


async def mainloop(task_config, env, mas):
    env.init(task_config)
    mas.init(task_config)

    while await env.run():
        e_promise = env.send(mas.url)
        m_promise = mas.send(env.url)

        # Assert the env2mas successfully run
        e_promise = await e_promise
        assert e_promise == "SUCCESS"

        # Assert the mas2env successfully run
        m_promise = await m_promise
        report = await env.check(m_promise)

        if report.status == "SUCCESS":
            mas.set_success_flag(task_config["task_id"])
            break
        else:
            await mas.handel_failure(report)
            await asyncio.sleep(1)

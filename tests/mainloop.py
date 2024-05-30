import asyncio
# from typing import Dict
import uuid


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


async def send(url):
    await asyncio.sleep(1)
    return "SUCCESS"


class Env:
    def __init__(self):
        self.url = "http://mas.url"
        self._success = False

    def init(self, task_config):
        pass

    async def run(self):
        return not self._success

    async def send(self, url):
        await asyncio.sleep(1)
        return "SUCCESS"

    async def check(self, promise):
        await asyncio.sleep(1)
        return Report(status="SUCCESS")  # Mocked success for simplicity

    def set_success_flag(self, tid):
        self._success = True


class Mas:
    def __init__(self):
        self.url = "http://env.url"

    def init(self, task_config):
        pass

    async def send(self, url):
        await asyncio.sleep(1)
        return "SUCCESS"

    async def handel_failure(self, report):  # start again if fail
        print('Handeling failure', report)


class Report:
    def __init__(self, status):
        self.status = status


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


if __name__ == "__main__":
    env = Env()
    mas = Mas()
    task_config = {"task_id": uuid.uuid4()}

    asyncio.run(mainloop(task_config, env, mas))

import asyncio


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

    while await env.run():
        # step 1 env send packed data (task_config) to mas
        e_promise = Promise(env.send(mas.url, task_config))
        env_promise = TaskPromise(lambda p: print(f"env sent data: {p}"))
        env_promise.promise = e_promise

        # step 2 mas received and process data
        m_promise = Promise(mas.receive(env.url))
        mas_promise = TaskPromise(lambda p: print(f"mas received data: {p}"))
        mas_promise.promise = m_promise

        # step 3 mas sends data back to env
        mas_results = await mas_promise.promise
        await env.receive(mas_results)

        # step 4 env performs test
        await env.perform_test()

        # step 5 judge if the task is success or not
        if env._success:
            mas.set_success_flag(task_config["content"]["demand"]["demand_id"])
            break
        else:
            await mas.handel_failure()
            await asyncio.sleep(1)

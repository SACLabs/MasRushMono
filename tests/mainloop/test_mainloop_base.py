import asyncio


async def send(url):
    await asyncio.sleep(1)
    return "SUCCESS"


# TODO: 实现env功能
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
        return "SUCCESS"  # Mocked success for simplicity

    def set_success_flag(self, tid):
        self._success = True


# TODO: 实现mas功能
class Mas:
    def __init__(self):
        self.url = "http://env.url"

    def init(self, task_config):
        pass

    async def send(self, url):
        await asyncio.sleep(1)
        return "SUCCESS"

    async def handel_failure(self, report):  # start again if fail
        print("Handeling failure", report)

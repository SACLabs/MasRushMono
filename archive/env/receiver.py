# MAS2ENV
# graph, kanban, performance
from archive.env import share_queue
from archive.typing.env import MAS2Env
from fastapi import FastAPI

app = FastAPI()
@app.route("/mas_to_env")
def pipeline(data: MAS2Env):
    # TODO，ID蕴藏在文件的名字中
    share_queue.append(data)

# MAS2ENV
# graph, kanban, performance
from masr.env import share_queue
from masr.typing.env import MAS2Env

@app.route("/mas_to_env")
def pipeline(data:MAS2Env):
    # TODO，ID蕴藏在文件的名字中
    share_queue.append(data)

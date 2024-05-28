import pathlib

from masr.env import share_queue, runner, sender, kanban, vis_graph
from masr.typing.env import MAS2Env, Env2MAS
from masr.config import ENVSERVER, ENVSERVERPORT

folder_path = pathlib.Path(__file__).parent


def pipeline(mas_data: MAS2Env):
    pytest_result, cprofile_result = runner.run(mas_data)
    kanban.entre(mas_data.history)
    vis_graph.from_networkx_graph(mas_data.graph)
    run_sh_file = folder_path.parent / "config/run.sh"
    env_to_mas_data = Env2MAS(
        task_id=mas_data.task_id,
        demand="mock random demand",
        shell=run_sh_file,
        pytest_result=pytest_result,
        cprofile_performance=cprofile_result
    )
    sender.send_message_from_mas_to_env(env_to_mas_data)




def run():
    # 单独子进程，用来启动receiver
    while True:
        if not share_queue.empty():
            mas_data = share_queue.get()
            pipeline(mas_data)


if __name__=="__main__":
    run()

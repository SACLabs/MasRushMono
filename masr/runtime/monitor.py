from masr.runtime.runner import run_ci


def kanban():
    return None


def start_reciever_server():
    pass


def pipeline(pipeline_input):
    pytest_result, performance_result = run_ci(pipeline_input["content"]["result"])


def run():
    while True:
        pass

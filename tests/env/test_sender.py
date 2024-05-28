# sender send stuffs to mas
import pathlib
import sys
folder_path = pathlib.Path(__file__)
print(folder_path.parent.parent)
sys.path.append(str(folder_path.parent.parent.parent))

from masr.typing.env import Env2MAS
from masr.env.sender import send_message_from_mas_to_env
import pathlib

folder_path = pathlib.Path(__file__).parent

def test_env_send_to_mas():
    shell_path = folder_path.parent.parent /"config/run.sh"
    with open(shell_path, 'rb') as file:
        file_bytes = file.read()

    test_env_to_mas = Env2MAS(
        task_id= "mock task id",
        demand="mock random demand",
        shell= file_bytes,
        pytest_result={"mock_pytest_key": "mock_test_result"},
        cprofile_performance={"mock_performance_key": "test_performance"},
    )
    send_message_from_mas_to_env(test_env_to_mas)

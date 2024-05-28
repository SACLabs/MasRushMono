# This runner run src code provided by MAS2ENV
import sys
import os
import pathlib
root_folder_path = pathlib.Path(__file__).parent.parent.parent
sys.path.append(str(root_folder_path))
from masr.env.runner import run

def test_env_runner():

    source_code_path = f"{root_folder_path}/demand/snake"
    res = run(source_code_path)
    print(source_code_path)

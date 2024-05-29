# 负责和mas交互数据，并且提供统一的测试环境

from flask import Flask, request
import requests

import os
import subprocess
import json
import pstats

from .utils import uncompressed_file, parse_file_name

app = Flask(__name__)

venv_path = "/path/venv_path"
task_history_path = "/path/history"


def run_pytest(source_code_path):
    # 载入预先创建好的虚拟环境
    json_report_path = os.path.join(source_code_path, "report.json")
    pytest_command = [
        os.path.join(venv_path, "bin", "pytest"),
        "--json-report",
        f"--json-report-file={json_report_path}",
        source_code_path,
    ]
    subprocess.run(pytest_command)
    # 读取json报告
    with open(json_report_path, "r") as file:
        report_data = json.load(file)
    # {'passed': 3, 'total': 3, 'collected': 3}
    return report_data["summary"]


def run_cprofile(source_code_path):
    # 编辑run.sh文件，追加虚拟环境进去
    run_script_path = os.path.join(source_code_path, "run.sh")
    activate_command = f". {venv_path}/bin/activate\n"
    # 读取脚本的原始内容
    with open(run_script_path, "r") as file:
        original_content = file.readlines()
    # 插入激活命令
    new_content = [activate_command] + original_content
    # 重新写回文件
    with open(run_script_path, "w") as file:
        file.writelines(new_content)

    # 此处为了使用cprofile监控函数的运行，则需要修改shell脚本的
    command = ["/bin/bash", run_script_path]
    subprocess.run(command)
    # 初始化pstats对象并加载.prof文件
    profile_file_path = os.path.join(source_code_path, "output.prof")
    pstats_obj = pstats.Stats(profile_file_path)
    pstats_obj.strip_dirs().sort_stats("cumulative")  # 根据需要调整排序方式

    # 构建字典数据
    profile_data = {}
    for func_name, stats in pstats_obj.stats.items():
        # 将stats对象转化为更易处理的形式，这里简化处理，只提取几个关键指标
        func_stats = {
            "ncalls": stats[0],  # 调用次数
            "tottime": stats[1],  # 总时间（不包括子调用）
            "cumtime": stats[3],  # 累积时间（包括子调用）
            # 可以根据需要添加更多字段，例如 'filename', 'lineno' 等
        }
        profile_data[f"{func_name[0]}:{func_name[1]}:({func_name[2]})"] = func_stats
    return profile_data

@massage_handler()
def env_to_mas(task_id: str) -> dict:
    """_summary_

    Args:
        mas_url (_type_): _description_
    Return:
        test_result (_type_): _description_
        performance_result (_type_): _description_
    """
    # 发送run.sh, test_result, performance_result
    # run_script_path = "./run.sh"
    # file = open(run_script_path, "rb")
    # requests.post(
    #     mas_url,
    #     file=file,
    #     data={"test_result": test_result, "performance_result": performance_result},
    # )
    mas_url = get_mas_url(task_id)
    test_result, performance_result = get_results_by_url(mas_url)
    return {mas_url: {"run.sh": run_script_path,"test_result": test_result, "performance_result": performance_result}}


def convert_src_code_to_uml_structure(source_code_path):
    # 此处调用pylint将source code转为uml图
    pass


def append_task_history(task_id, test_result, performance_result):
    with open(os.path.join(task_history_path, task_id), "+w") as f:
        f.write(test_result)
        f.write(performance_result)

def mas_to_env():
    pass


@app.route("/mas_to_env")
def pipeline(compressed_source_code):
    # TODO，ID蕴藏在文件的名字中
    task_id, uncompressed_file_path = uncompressed_file(compressed_source_code)
    test_result = run_pytest(uncompressed_file_path)
    performance_result = run_cprofile(uncompressed_file_path)
    env_to_mas({"test_result": test_result, "performance_result": performance_result})
    append_task_history(task_id, test_result, performance_result)


if __name__ == "__main__":
    app.run()

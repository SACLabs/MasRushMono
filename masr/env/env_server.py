# 负责和mas交互数据，并且提供统一的测试环境

from flask import Flask, request
import requests

import cProfile

app = Flask(__name__)

mas_url = "http://example.com/env_mas"

class Env:
    def __init__(self):
        self._test_runner = self._load_test_env()


    def _load_test_env(self):
        # 载入环境，用来对mas传过来的src代码进行测试
        # 过程是，开一个进程，载入环境
        return None


    def _send_to_env(self, test_result):
        # 一个shell文件，一个description文件，以及当前测试结果
        task_id = test_result.task_id
        # TODO,从数据库中拿出对应的run.sh
        run_sh = "Mock file"
        requests.post(mas_url, files=run_sh, data=test_result)


    def _check_test_result(self, test_result):
        # TODO 如果测试的覆盖率高，且全测试通过，则测试数据放行给mas，否则直接block？
        # 测试结果放入到数据库中，也就是unittest的coverage report信息
        passed_test = False
        return passed_test


    def _uncompressed_data(self, compressed_data):
        # TODO，此处对数据进行解压
        uncompressed_data = "Mock uncomp"
        return uncompressed_data


    def _convert_src_code_to_uml_structure(self, src_code):
        # TODO传入源代码，转换为uml图，形式为svg格式
        # ?保存下来的svg图发送到哪里，是否直接放入到数据库中
        pass


    def pipeline(self, compressed_data):
        uncompressed_data = self._uncompressed_data(compressed_data)
        test_result = self._test_runner(uncompressed_data)
        passed_flag = self._check_test_result(test_result)
        if passed_flag:
            self._convert_src_code_to_uml_structure(uncompressed_data)
            self._send_to_env(test_result)


    def show(self):
        pass




run_env = Env()



@app.route("/mas_env")
def mas_env():
    compossed_file = request.files['file']
    run_env.pipeline(compossed_file)


# TODO，留一个url用来给前端进行展示使用
@app.route("show")
def show():
    run_env.show()


if __name__ == '__main__':
    app.run()

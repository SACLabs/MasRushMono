# 负责和mas交互数据，并且提供统一的测试环境

from flask import Flask, request
import requests

app = Flask(__name__)

mas_url = "http://example.com/env_mas"

class Env:
    def __init__(self):
        self._test_runner = self._load_test_env()
        self.create_db_link()

    def create_db_link(self):
        # 采用Prometheus数据库，由于此数据库是通过api上传，无需载入orm
        pass

    def _load_test_env(self):
        # 载入环境，用来对mas传过来的src代码进行测试
        return None


    def _send_to_env(self, test_result):
        # 一个shell文件，一个description文件，以及当前测试结果
        task_id = test_result.task_id
        # TODO,从数据库中拿出对应的run.sh
        run_sh = "Mock file"
        requests.post(mas_url, files=run_sh, data=test_result)


    def _check_test_result(self, test_result):
        # TOD如果测试的覆盖率高，且全测试通过，则测试数据放行给mas，否则直接block？
        passed_test = False
        return passed_test


    def _uncompressed_data(self, compressed_data):
        # TODO，此处对数据进行解压
        uncompressed_data = "Mock uncomp"
        return uncompressed_data


    def pipeline(self, compressed_data):
        uncompressed_data = self._uncompressed_data(compressed_data)
        test_result = self._test_runner(uncompressed_data)
        passed_flag = self._integrate_test_result(test_result)
        if passed_flag:
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

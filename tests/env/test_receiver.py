# The receiver receive Code and other stuff from env

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

import base64
from typing import Dict
import os
app = FastAPI()

class Env2MAS(BaseModel):
    task_id: str = None # 任务的唯一ID
    demand: str = None  # 用户的编码需求
    run_shell: bytes = None # sh文件
    pytest_result: Dict = None  # CI测试结果
    cprofile_performance: Dict = None  # cprofile performance·


@app.post("/receive_from_env/")
async def upload_file(env_data: Env2MAS, file: UploadFile = File(...)):
    # 读取上传文件的内容并进行Base64编码
    file_content = await file.read()
    encoded_content = base64.b64encode(file_content).decode('utf-8')
    # 将文件内容添加到env_data中
    env_data_with_file = env_data.copy(update={"shell_script_content": encoded_content})

    # 保存文件到本地
    save_path = os.path.join("uploads", file.filename)
    with open(save_path, "wb") as f:
        f.write(file_content)
    # 将文件内容添加到env_data中

    return {"status": "success", "detail": "File uploaded and processed."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

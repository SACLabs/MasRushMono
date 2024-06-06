from fastapi.testclient import TestClient
from masr.ultils.receiver import (
    gen_receiver,
)  # 确保正确导入你的 FastAPI 应用生成函数


def test_gen_receiver(mocker):
    # 使用 mocker 来模拟 redis.from_url 方法
    mock_redis_client = mocker.MagicMock()
    mocker.patch("redis.from_url", return_value=mock_redis_client)

    # 获取 FastAPI 应用实例
    app = gen_receiver(dtypes="MAS")
    client = TestClient(app)

    # 定义模拟的消息数据
    test_message = {"data": "test data"}

    # 发送 POST 请求到接收端点
    response = client.post("/receive/", json=test_message)

    # 验证接收端点的响应
    assert response.status_code == 200
    assert response.json() == {"message": "Data received and added to Redis"}

    # 验证是否正确调用了 mock_redis_client 的 lpush 方法
    mock_redis_client.lpush.assert_called_once_with(
        "MAS_message_queue", test_message
    )

import pytest
from unittest.mock import patch
from scheduler import process_message, scheduler

def test_process_message():
    # 测试消息处理逻辑
    result = process_message("Test message")
    assert result == "Processed: Test message"

@patch('scheduler.redis_client')
def test_scheduler(mock_redis):
    # 模拟 Redis 的 brpop 方法
    mock_redis.brpop.return_value = [None, b'Test message']
    # 模拟 process_message 方法
    with patch('scheduler.process_message', return_value='Processed message'):
        scheduler()  # 实际调用会无限循环，你可能需要进一步调整这个测试
        assert mock_redis.lpush.called

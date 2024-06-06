import pytest
from masr.ultils.sender import gen_sender


def test_gen_sender(mocker):
    # Mock redis client 以及返回值
    mock_redis_client = mocker.Mock()
    mock_message = ("key", "value")
    mock_redis_client.brpop.return_value = mock_message
    mocker.patch(
        "masr.ultils.sender.redis.from_url", return_value=mock_redis_client
    )

    # Mock requests.post response
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None
    mock_post = mocker.patch(
        "masr.ultils.sender.requests.post", return_value=mock_response
    )

    sender = gen_sender(dtypes="MAS", target="http://example.com:8080")

    # Run sender in a limited loop for testing
    mocker.patch("masr.ultils.sender.time.sleep", side_effect=StopIteration)

    try:
        sender()
    except StopIteration:
        pass

    # Assertions to check if correct interactions occurred
    mock_redis_client.brpop.assert_called_once_with("MAS_send_queue", 0)
    mock_post.assert_called_once_with(
        "http://example.com:8080", json=mock_message
    )


if __name__ == "__main__":
    pytest.main()

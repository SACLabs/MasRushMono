import asyncio
import unittest
import uuid
from unittest.mock import AsyncMock, patch, MagicMock

from masr.mainloop.mainloop import env_loop, mas_loop, main_loop
from masr.models.interface import EnvOutput, MASOutput
from tests.test_base import (
    task_id,
    demand,
    report,
    source_code,
    task_desc,
    gml,
)
from masr.models.task import TaskHistory


class TestEnvMAS(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.redis_mock = MagicMock()

        mock_history = TaskHistory(history=[task_desc])
        # Mock EnvOutput and MASOutput
        self.env_output = EnvOutput(
            task_id=task_id, demand=demand, report=report, src=source_code
        )
        self.mas_output = MASOutput(
            task_id=task_id,
            result=source_code,
            graph=gml,
            history=mock_history,
        )

    @patch(
        "masr.mainloop.wrapper.EnvWrapper.perform_pipeline",
        new_callable=AsyncMock,
    )
    @patch("masr.mainloop.wrapper.EnvWrapper.send", new_callable=AsyncMock)
    @patch("masr.mainloop.wrapper.EnvWrapper.receive", new_callable=AsyncMock)
    async def test_env_loop(
        self, mock_receive, mock_send, mock_perform_pipeline
    ):
        # Set up mocks
        mock_receive.return_value = self.mas_output
        mock_perform_pipeline.return_value = True

        task_config = self.env_output
        await env_loop(self.redis_mock, task_config)

        # Verify the mocks were called as expected
        mock_send.assert_called_once()
        mock_receive.assert_called_once()
        mock_perform_pipeline.assert_called_once()

    @patch("masr.mainloop.wrapper.MasWrapper.receive", new_callable=AsyncMock)
    @patch("masr.mainloop.wrapper.EnvWrapper.send", new_callable=AsyncMock)
    @patch(
        "masr.mainloop.wrapper.MasWrapper.perform_pipeline",
        new_callable=AsyncMock,
    )
    async def test_mas_loop(
        self, mock_receive, mock_send, mock_perform_pipeline
    ):
        # Set up mocks
        mock_receive.return_value = self.env_output
        mock_perform_pipeline.return_value = True

        stop_event = asyncio.Event()
        mas_task = asyncio.create_task(mas_loop(self.redis_mock, stop_event))

        await asyncio.sleep(0.1)  # Allow loop to process

        # Simulate stopping the loop
        stop_event.set()
        await mas_task

        # Verify the mocks were called as expected
        mock_receive.assert_called()
        mock_send.assert_called()
        mock_perform_pipeline.assert_called()

    @patch(
        "masr.mainloop.wrapper.EnvWrapper.perform_pipeline",
        new_callable=AsyncMock,
    )
    @patch("masr.mainloop.wrapper.EnvWrapper.send", new_callable=AsyncMock)
    @patch("masr.mainloop.wrapper.EnvWrapper.receive", new_callable=AsyncMock)
    @patch("masr.mainloop.wrapper.MasWrapper.receive", new_callable=AsyncMock)
    @patch("masr.mainloop.wrapper.EnvWrapper.send", new_callable=AsyncMock)
    @patch(
        "masr.mainloop.wrapper.MasWrapper.perform_pipeline",
        new_callable=AsyncMock,
    )
    async def test_main_loop(
        self,
        mock_mas_receive,
        mock_mas_send,
        mock_mas_perform_pipeline,
        mock_env_receive,
        mock_env_send,
        mock_env_perform_pipeline,
    ):
        mock_mas_receive.return_value = self.env_output
        mock_mas_perform_pipeline.return_value = self.mas_output
        mock_env_receive.return_value = self.mas_output
        mock_env_perform_pipeline.return_value = self.env_output

        task_config1 = self.env_output
        task_config2 = self.env_output
        task_config2.task_id = uuid.uuid4()
        task_config2.demand.demand_id = uuid.uuid4()

        await main_loop([task_config1, task_config2], self.redis_mock)

        # Verify the mocks were called as expected
        self.assertEqual(mock_env_send.call_count, 2)
        self.assertEqual(mock_env_receive.call_count, 2)
        self.assertEqual(mock_env_perform_pipeline.call_count, 2)
        self.assertEqual(mock_mas_send.call_count, 2)
        self.assertEqual(mock_mas_receive.call_count, 2)
        self.assertEqual(mock_mas_perform_pipeline.call_count, 2)


if __name__ == "__main__":
    unittest.main()

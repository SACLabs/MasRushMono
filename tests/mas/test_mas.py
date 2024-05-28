import pytest
from masr.mas.main import MAS, pipeline

from masr.typing.env import Env2MAS, MAS2Env, Algo2MAS, MAS2Algo
from masr.mas.graph import Graph
from masr.mas.task import TaskGraph, TaskHistory
from unittest.mock import Mock

@pytest.fixture
def mock_graph(mocker):
    graph = mocker.Mock(spec=Graph)
    graph.init = mocker.Mock()
    graph.run = mocker.Mock()
    return graph

@pytest.fixture
def mas_instance(mock_graph):
    return MAS(graph=mock_graph)

def test_mas_initialization(mas_instance, mock_graph):
    assert mas_instance.graph == mock_graph
    mock_graph.init.assert_called_once()

def test_mas_run(mas_instance, mock_graph, mocker):
    task = mocker.Mock()
    mas_instance.run(task)
    mock_graph.run.assert_called_once_with(task)

@pytest.fixture
def mock_pipeline_dependencies(mocker):
    mocker.patch('mas.algorithm', return_value=Mock(spec=Algo2MAS))
    mocker.patch('mas.MAS.get_result', return_value="mock_result")
    mocker.patch('mas.MAS.get_log', return_value="mock_log")

@pytest.mark.asyncio
async def test_pipeline(mock_pipeline_dependencies):
    data = Env2MAS(task_id="1", demand="test_demand", pytest_result={}, cprofile_performance={}, mas_ip="127.0.0.1")
    result = await pipeline(data)
    assert isinstance(result, MAS2Env)
    assert result.result == "mock_result"
    assert result.history == "mock_log"

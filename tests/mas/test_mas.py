import pytest
from masr.mas.main import MAS, pipeline

@pytest.fixture
def mock_graph(mocker):
    graph = mocker.Mock()
    graph.init = mocker.Mock()
    graph.run = mocker.Mock()
    return graph

@pytest.fixture
def mas_instance(mock_graph):
    return MAS(graph=mock_graph)

def test_mas_initialization(mas_instance, mock_graph):
    assert mas_instance.graph == mock_graph
    mock_graph.init.assert_called_once()

def test_mas_run(mas_instance, mock_graph):
    task = mocker.Mock()
    mas_instance.run(task)
    mock_graph.run.assert_called_once_with(task)
    
# Additional tests for the remaining methods...

from dataclasses import dataclass, field
from typing import Dict, Any, List, Tuple

from masr.mas.node import Node


@dataclass
class VisualNode:
    id: str
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class VisualEdge:
    source: str
    target: str
    label: str
    key: int
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class VisualGraph:
    graph: nx.MultiDiGraph
    nodes: List[VisualNode]
    edges: List[VisualEdge]


@dataclass
class Graph:
    nodes: Dict[Node]
    edges = List[Tuple[Node,Node]]

    @classmethod
    def init(cls, graph_dict: Dict[Node, List[Node]]) -> None:
        pass

    def add_node(self, node: Node) -> None:
        pass

    def add_edge(self, edge: Tuple) -> None:
        pass

    def remove_node(self, node: Node) -> None:
        pass

    def remove_edge(self, edge: Tuple) -> None:
        pass

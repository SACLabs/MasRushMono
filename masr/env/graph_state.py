# 解析回传的graph数据，存入node和edge visual dataclass，用于 visulization
from dataclasses import dataclass, field
from typing import Any, Dict, List
import networkx as nx


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

    def from_networkx_graph(self, graph: nx.MultiDiGraph) -> None:
        self.graph = graph
        self.nodes = [VisualNode(str(node), graph.nodes[node]) for node in graph.nodes()]
        self.edges = [
            VisualEdge(
                source=edge[0],
                target=edge[1],
                label='',
                key=key,
                properties=graph.edges[edge[0], edge[1], key]
            )
            for edge in graph.edges
            for key in graph.edges[edge]
        ]


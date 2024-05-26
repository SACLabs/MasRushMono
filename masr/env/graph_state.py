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


# 一个总的dataclass
@dataclass
class VisualGraph:
    graph: nx.MultiDiGraph
    nodes: List[VisualNode]
    edges: List[VisualEdge]


# 将图数据存入dataclass用于可视化
def from_networkx_graph(graph: nx.MultiDiGraph) -> VisualGraph:  # 遍历图数据存入dataclass 用于可视化
    nodes = [VisualNode(str(node), graph.nodes[node]) for node in graph.nodes()]
    edges = [
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
    return VisualGraph(graph, nodes, edges)


if __name__ == "__main__":
    # 生成随机图
    G = nx.gnm_random_graph(n=10, m=30, directed=True, seed=42)
    M = nx.MultiDiGraph(G)
    # 存入dataclass
    visual_graph = from_networkx_graph(M)
    # 可视化...
    print(visual_graph.graph)
    print(visual_graph.nodes)
    print(visual_graph.edges)
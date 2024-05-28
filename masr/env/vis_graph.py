# 解析回传的graph数据，存入node和edge visual dataclass，用于 visulization
import matplotlib.pyplot as plt
import networkx as nx

from masr.typing.graph import VisualNode, VisualEdge, VisualGraph


# graph visualization 的入口
def graph_start(graph: nx.MultiDiGraph) -> None:
    graph_data = from_networkx_graph(graph)
    graph_draw(graph_data)


# 作图，待扩充
def graph_draw(graph_data: VisualGraph) -> None:
    nx.draw(graph_data.graph)
    plt.savefig()


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

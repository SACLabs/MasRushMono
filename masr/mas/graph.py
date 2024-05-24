# TODO
from dataclasses import dataclass
from typing import Dict, List, Tuple
from node import Node  

 
"""
Graph类的init函数和CRUD的函数，在对Graph数据结构进行改变的同时，
要映射到MAS系统中，要保证可以成功实例化node节点，并且通过更改路由表的方式更改edges的连接
"""
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

    # 使用GML格式进行序列化和反序列化
    def stringizer(self, file_path: str) -> None:
        pass

    def destringizer(self, file_path: str) -> None:
        pass
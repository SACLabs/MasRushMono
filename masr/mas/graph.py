# TODO
from networkx import MultiDiGraph
import networkx as nx

 
"""
Graph类的init函数和CRUD的函数，在对Graph数据结构进行改变的同时，
要映射到MAS系统中，要保证可以成功实例化node节点，并且通过更改路由表的方式更改edges的连接
"""

# 使用GML格式进行序列化和反序列化
def stringize_graph(MDGraph: MultiDiGraph) -> str:
    return "\n".join(nx.generate_gml(MDGraph))

def destringize_graph(gml_text: str) -> MultiDiGraph:
    return nx.parse_gml(gml_text)
from pydantic import BaseModel
import networkx as nx
from networkx import MultiDiGraph


class GML(BaseModel):
    content: str


# 使用GML格式进行序列化和反序列化
def stringize_graph(MDGraph: MultiDiGraph) -> GML:
    return GML(content="\n".join(nx.generate_gml(MDGraph)))


def destringize_graph(gml: GML) -> MultiDiGraph:
    content = gml.content
    return nx.parse_gml(content)

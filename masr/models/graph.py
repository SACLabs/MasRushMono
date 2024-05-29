import networkx as nx
from networkx import MultiDiGraph
from pydantic import BaseModel


class GML(BaseModel):
    content: str


# 使用GML格式进行序列化和反序列化
def from_nxGraph_to_GML(MDGraph: MultiDiGraph) -> GML:
    return GML(content="\n".join(nx.generate_gml(MDGraph)))


def from_GML_to_nxGraph(gml: GML) -> MultiDiGraph:
    content = gml.content
    return nx.parse_gml(content)

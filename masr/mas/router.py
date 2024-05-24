# router
# 负责管理 A:B 间消息的路由、生成新的 A Gate 与 B Gate

from typing import List, Tuple
import copy
from .message import Message
from .actor import AbstractActor
from address import MultiAddr
from gate import NodeGate


class Router(AbstractActor):
    def __init__(self, node_addr):
        super().__init__()
        self._node_type = "Router"
        self._node_addr = node_addr
        self._node_gate_type_address_dict = {}
        self.spawn_new_actor(NodeGate, self._node_addr.name)

    def on_receive(self, message: Message):
        # 区分 message 是 left gate 还是 right gate; 
        # [QA:DE]: left gate: QA; right gate: DE
        # left -> right; right -> left;
        ...

    def spawn_new_actor(self, cls, node_gate_link_type):
        # 生成 node_gate
        # 告诉NodeGate能够直接链接的路由节点
        ...
# gate
# 充当网络参与者系统中的管理实体，处理节点之间的消息并相应地路由它们
# Singleton , 确保每个 gate 类型(QA gate / PM gate)只有一个实例

from typing import List, Tuple, Dict, Set

from .message import Message
from .actor import AbstractActor
from .address import MultiAddr
import random
import copy


class NodeGate(AbstractActor):
    __instance__: Dict[str, "NodeGate"] = {}
    __first_init__: Set[str] = set()

    def __new__(cls, node_gate_type, *args, **kwargs):
        # 使用 __new__ 来控制实例的创建，使用 __instance__ dictionary 来跟踪这些实例
        if node_gate_type not in cls.__instance__:
            cls.__instance__[node_gate_type] = super().__new__(cls)
        return cls.__instance__[node_gate_type]

    def __init__(self, node_gate_type, addr):
        # __init__ 在每个 gate 类型中只初始化一次各种属性，__first_init__ set 跟踪已初始化的 gate 类型
        if node_gate_type not in self.__first_init__:
            super().__init__()
            self._node_type = "NodeGate"
            self._router_addr_dict = {}
            self._node_addr = addr
            self._node_gate_type = node_gate_type
            self.__first_init__.add(node_gate_type)
            self._node_count = 0
            self._node_id_instance = {}

    def set_router_addr(self, node_gate_link_type, router_addr, router_instance):
        ...

    def on_receive(self, message: Message):
        # 判断 message 源是 router 还是 node
        # if is router:
        #   send to node
        # else:
        #   send to router
        ...

    def spawn_new_actor(self, cls, args):
        # 根据提供的类和参数动态创建同类型 node 的实例，并在 对应类型的 gate 中对它们进行管理。
        ...

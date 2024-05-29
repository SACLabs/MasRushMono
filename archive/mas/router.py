# router
# 负责管理 A:B 间消息的路由、生成新的 A Gate 与 B Gate

from archive.typing.message import Message
from .actor import AbstractActor
from gate import NodeGate


class Router(AbstractActor):
    def __init__(self, node_addr):
        super().__init__()
        self._node_type = "Router"
        self._node_addr = node_addr
        self._node_gate_type_address_dict = {}
        self.spawn_new_actor(NodeGate, self._node_addr.name)

    def on_receive(self, message: Message):
        # 新消息添加至邮箱
        self._message_box.append(message)
        # 区分几个事情：
        # message只能发送给NodeGate，区分这个message是从哪个NodeGate发送过来
        if message.from_node_type_name == self._node_gate_left:
            self._send(
                message, self._node_gate_type_address_dict[self._node_gate_right]
            )

        elif message.from_node_type_name == self._node_gate_right:
            self._send(
                message, self._node_gate_type_address_dict[self._node_gate_left]
            )

    def spawn_new_actor(self, cls, node_gate_link_type):
        # 生成 node_gate
        # 告诉NodeGate能够直接链接的路由节点
        ...
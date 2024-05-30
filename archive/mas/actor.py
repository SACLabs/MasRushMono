# Actor
# This class is used for
# 1. message send
# ```mermaid
# xxxx
# ```
# https://ao.feishu

from typing import Set, Union, List

from archive.typing.message import Message
from .address import MultiAddr


class AbstractActor:
    def __init__(self):
        super().__init__()
        self.address_book: Set[str] = set()  # name -> addr
        self.instance = dict()  # addr
        self.message_box = []
        self.node_type = None
        self.node_addr = None
        self.node_alias = None

    def on_receive(self, message: Message):
        raise NotImplementedError

    def _send(self, message: "Message", next_hop_address):
        if isinstance(next_hop_address, MultiAddr):
            self._instance[next_hop_address].on_receive(message)

        elif isinstance(next_hop_address, str):
            self._instance[next_hop_address].on_receive(message)

        else:
            for next_actor_instance_addr in next_hop_address:
                self._instance[next_actor_instance_addr].on_receive(message)

    def spawn_new_actor(self, cls, args: Union[List, str]):
        raise NotImplementedError

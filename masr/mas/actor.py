# Actor
# This class is used for 
# 1. message send
# ```mermaid
# xxxx
# ```
# https://ao.feishu

from typing import Set, Union, List
from message import Message

class AbstractActor():
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
        ...

    def spawn_new_actor(self, cls, args: Union[List, str]):
        raise NotImplementedError

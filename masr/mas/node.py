import logging
from abc import ABCMeta
from typing import Any, Callable, Dict, List


from actor import AbstractActor
from message import Message


class Preprocessor(metaclass=ABCMeta):
    def pre_process(self, actor, message: Message) -> bool:
        return True  # Default behavior to always process messages


class Node(AbstractActor):
    _id_counter: int = 0
    message_handlers: Dict[str, List[Callable[..., Any]]] = (
        {}
    )  # ["DE:QA": [handler_generate_test], "PM:QA": [handler_generate_test, handler_generate_doc]]
    message_types: List[List[str]] = []     # [["DE:QA", "PM:QA"], ["PM:QA"]]
    handler_call_by_message_types: Dict[Callable, List[str]] = {}   # {"handler_generate_test": ["DE:QA", "PM:QA"], "handler_generate_doc": ["PM:QA"]}

    def __init__(self, node_name: str = "", address: str = ""):
        super().__init__()
        self.id: int = Node._id_counter
        Node._id_counter += 1
        self._node_type = "RealNode"
        self.node_name = node_name
        self.address = address
        # message name : handler
        self.handlers: Dict[str, Callable] = {}
        # { "DE:QA": [message_over, ..., message_lates], "PM:QA": [message_over, ..., message_lates]}
        self.message_map: Dict[str, List[Message]] = {}

    def on_receive(self, message: Message):
        # message_map 更新
        # target_message = handle_message(message)
        # send to gate
        ...

    @classmethod
    def process(cls, message_type_list: List[str]) -> Callable:
        def decorator(func: Callable):
            # 根据 message_type_list 更新 message_types, handler_call_by_message_types
            ...
            return func

        return decorator

    def handle_message(
        self, message: Message, *args: Any, **kwargs: Any
    ) -> Any:
        # 根据 message name，在 message_handlers 中找 handler
        # 根据 hendler 在 handler_call_by_message_types 找 handler 对应的 message_types
        # 在 message_map 中找 各个 message_types 的历史消息是否全到达，保证 task_id 一致
        # if True: 
        #   bundle messages's content as bundle_content:[content1, content2, ...] that its order is consisten with message_types
        #   target_message = handle(bundle_content)
        #   return target_message
        # else:
        #   pass
        ...
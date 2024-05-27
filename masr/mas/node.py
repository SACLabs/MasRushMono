from abc import ABCMeta
from typing import Any, Callable, Dict, List, Tuple


from actor import AbstractActor
from masr.typing.message import Message
from gate import NodeGate


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
        self.gate: NodeGate = None
        # message name : handler
        self.handlers: Dict[str, Callable] = {}
        # { "DE:QA": [message_over, ..., message_lates], "PM:QA": [message_over, ..., message_lates]}
        self.message_map: Dict[str, List[Message]] = {}

    def on_receive(self, message: Message):
        # message_map 更新
        self.message_map[message.message_name].append(message)
        # 处理当前消息
        target_messages = self.handle_message(message)
        
        [self._send(message, self.gate._node_addr) for message in target_messages]

    def handle_message(
        self, message: Message, *args: Any, **kwargs: Any
    ) -> Any:
        result = []
        # 一个消息可触发多个处理函数
        handlers = self.message_handlers[message.message_name]
        # 一个处理函数需要一个至多个消息触发, 在图上等于一个节点拥有多个入度
        for handler in handlers:
            # 根据 message 和 handler 寻找历史消息
            # 并打包消息给handler进行处理
            handled_messages = [handler(messages) for messages in self.check_prefix(message, handler) if len(messages) is not 0]
            result.append(handled_messages)
        return result
    
    def check_prefix(self, message: Message, handler: Callable
    ) -> Tuple[bool, List[Message]]:
        # 找到 触发 handler 所需的所有消息
        type_list = Node.handler_call_by_message_types[handler]
        for type in type_list:
            # 根据每个 消息类型去找历史消息
            for past_message in reversed(self.message_map[type]):
                # 遍历消息列表
                ...
        return [...]
        
    @classmethod
    def process(cls, message_type_list: List[str]) -> Callable:
        def decorator(func: Callable):
            # 根据 message_type_list 更新 message_types, handler_call_by_message_types
            ...
            return func

        return decorator
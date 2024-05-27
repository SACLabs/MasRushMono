from dataclasses import dataclass
import uuid
from typing import Union


@dataclass
class Message:
    message_name: str
    message_id: Union[uuid.UUID, str] = "None"
    from_agent: str = "None"
    to_agent: str = "None"
    content: str = "None"
    task_id: str = "None"
    from_agent_type: str = "None"
    from_node_type_name: str = "None"
    broadcasting: bool = True
    
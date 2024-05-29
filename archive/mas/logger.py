# loggger
# 记录 Node 过往活动

from dataclasses import dataclass, field
from typing import Dict, Any, List, Tuple, Optional
from typing.task import TaskStatus, Message
from mas.node import Node
from datetime import datetime

@dataclass
class MASLog:
    node_name: str
    task_id: str
    
    handle_name: str
    timestamp: str
    stage: TaskStatus
    
# sample
class Producer(Node):
    def __init__(self):
        ...
    
    @Node.process(["xxx:Producer"])
    def produce(self):
        # 生产商品
        ...
        
    @Node.process(["Consumer:Producer"])
    def transport(self):
        # 传输商品
        ...

class Consumer(Node):
    def __init__(self):
        ...
    
    @Node.process(["xxx:Consumer"])
    def consume(self):
        # 购买商品
        ...
    
    @Node.process(["Producer:Consumer"])
    def act(self):
        # 使用商品
        ...
        

class MASLogger(Node):
    def __init__(self):
        self.logbook: List[MASLog] = []
        
    def on_receive(self, message: Message):
        self.log_message(message)
    
    def log_message(self, message, stage):
        # message 转 MASLog 并存入logbook 中
        log_entry = MASLog(
            node_name=message.node_name,
            task_id=message.task_id,
            handle_name=message.handle_name,
            timestamp=datetime.now(),
            stage=stage
        )
        self.logbook.append(log_entry)
        
    def get_logs(self, task_id: Optional[str]=None, node_name: Optional[str]=None) -> List[MASLog]:
        filtered_logs = []
        # 根据 task_id 或 node_name 找到对应消息存入 filtered_logs 中
        # 根据 时间戳排序 返回 Log
        return sorted(filtered_logs, key=lambda log: log.timestamp)

    def get_result(self, task_id: str = None) -> Optional[MASLog]:
        filtered_logs = []
        # 当前task_id
        
        return max(filtered_logs, key=lambda log: log.timestamp, default=None)
    '''
        [
            [ 
                "node_name": "producer_A",
                "task_id":  "0",
                handle_name: "produce",
                timestamp: "xxxx-xx-xx-xxxx",
                stage: "IN_PROGRESS"
            ],
            [ 
                "node_name": "consumer_A",
                "task_id":  "0",
                handle_name: "consume",
                timestamp: "xxxx-xx-xx-xxxx",
                stage: "IN_PROGRESS"
            ],
            [ 
                "node_name": "producer_A",
                "task_id":  "0",
                handle_name: "produce",
                timestamp: "xxxx-xx-xx-xxxx",
                stage: "COMPLETED"
            ],
            [ 
                "node_name": "consumer_A",
                "task_id":  "0",
                handle_name: "consume",
                timestamp: "xxxx-xx-xx-xxxx",
                stage: "COMPLETED"
            ],
            [ 
                "node_name": "producer_A",
                "task_id":  "0",
                handle_name: "transport",
                timestamp: "xxxx-xx-xx-xxxx",
                stage: "IN_PROGRESS"
            ],
            [ 
                "node_name": "producer_A",
                "task_id":  "0",
                handle_name: "transport",
                timestamp: "xxxx-xx-xx-xxxx",
                stage: "COMPLETED"
            ],
            [ 
                "node_name": "consumer_A",
                "task_id":  "0",
                handle_name: "act",
                timestamp: "xxxx-xx-xx-xxxx",
                stage: "IN_PROGRESS"
            ],
            [ 
                "node_name": "consumer_A",
                "task_id":  "0",
                handle_name: "act",
                timestamp: "xxxx-xx-xx-xxxx",
                stage: "COMPLETED"
            ],
        ]
        '''
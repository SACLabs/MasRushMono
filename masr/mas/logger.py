# loggger
# 记录 Node 过往活动

from dataclasses import dataclass, field
from typing import Dict, Any, List, Tuple
from typing.task import TaskStatus, Message
from mas.node import Node

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
        self.logbook: List[MASLog]
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
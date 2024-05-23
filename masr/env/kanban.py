# This class define the nkanban dataclass
# Used by whom

import dataclass

@dataclass
class KANBAN
    tasks: List[Task]
    roles: List[str]

@dataclass
class Task(str):
    subtask: List[Task]
    owner: People

    def type_match():
        t_type, content = self.split("_")

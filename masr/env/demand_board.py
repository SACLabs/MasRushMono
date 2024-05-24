# This class define the nkanban dataclass
# Used by env, env can call and store tasks and tests from mas, which can be presented on the demand board,
# user can add tasks and tests on the board.

from dataclasses import dataclass, field
from typing import List, Tuple, Dict


@dataclass
class SubTasks:
    name: str
    description: str


@dataclass
class TaskDemand:
    name: str
    description: str
    subtasks: List[SubTasks] = field(default_factory=List)


@dataclass
class TestDemand:
    name: str
    description: str


@dataclass
class DemandBoard:
    demands: List[TaskDemand] = field(default_factory=List)
    tests: List[TestDemand] = field(default_factory=List)

    def add_demands(self, demand: TaskDemand) -> None:
        self.demands.append(demand)

    def add_tests(self, test: TestDemand) -> None:
        self.tests.append(test)

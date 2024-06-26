"""
## The MAS(Multi-agent System) will do:
# @WangXuhongCN
- Step1: receive the packed data from ENV
- Step2: unpack the data
- Step3: It first interpretate the readme.md and understand the requirements of
 the task (through some LLM tools), turn it into a task list (in todo.txt)
- Step4: The task list will then be transfer into a graph state, in which each
 node is a specific agent that has a specific task to do. A entry node is used
 to send the task list to other agents, and a exit node is used to collect the
 results from all agent.
- Step5: The relations of nodes in state transition graph created in Step4
 will then be optimized by algorithms included in **MAS**
- Step6: The optimized graph will then be run by the MAS, and the results will
 be collected and sent back to ENV, including:
  - a. task_id
  - b. the generated code
  - c. the generated tests, these tests is generated by MAS to gain more
    understand of the code it generated
  - d. the generated run.sh
  - e. the changelog of task list
  - f. the graph of state transition
"""

from typing import Dict

from networkx import MultiDiGraph

from masr.models.interface import Demand, EnvOutput, MASOutput
from masr.models.task import TaskHistory


def interpret_demand(demand: Demand) -> TaskHistory:
    # Simulate interpretation of a readme file into todo.txt style task list
    raise NotImplementedError("This function is not yet implemented.")


def create_graph(task_list: TaskHistory) -> MultiDiGraph:
    # Placeholder for creating a graph state from the task list
    raise NotImplementedError("This function is not yet implemented.")


def optimize_graph(graph: MultiDiGraph) -> MultiDiGraph:
    # Placeholder for graph optimization
    raise NotImplementedError("This function is not yet implemented.")


def run_graph(graph: MultiDiGraph) -> MASOutput:
    # Simulate running the optimized graph and collecting results
    raise NotImplementedError("This function is not yet implemented.")


def mas_run(inp: EnvOutput) -> MASOutput:
    raise NotImplementedError("This function is not yet implemented.")


def pipeline(inp: Dict) -> Dict:
    raise NotImplementedError("This function is not yet implemented.")

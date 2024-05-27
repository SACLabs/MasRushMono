# This class define the agent board
# used by env, env get the task implementation details from mas, and present the task state of each agent.

from datetime import datetime

from masr.typing.task import TaskStatus, TaskItem


def task_to_todotxt(task_des: TaskItem, indent_level: int = 0) -> str:  # convert dataclass into todotxt string (in list)
    # todotxt components, task status
    parts = [task_des.status.value]

    # add priority
    if task_des.priority > 0:
        parts.append(f"({chr(65 + task_des.priority - 1)})")

    # add due date
    if task_des.due_date:
        parts.append(task_des.due_date.strftime('%Y-%m-%d'))

    # add task name and description
    parts.append(f"{task_des.name}: {task_des.description}")

    # add tags
    for tag in task_des.tags:
        parts.append(f"+{tag}")

    # add owner
    for owner in task_des.owner:
        parts.append(f"@{owner}")

    # convert parts to string
    task_str = ' '.join(parts)

    # apply task and subtasks in a hierarchical structure
    indent = "  " * indent_level
    result = [f"{indent}{task_str}"]

    # recursively add tasks to todotxt
    for subtasks in task_des.subtasks:
        result.append(task_to_todotxt(subtasks, indent_level + 1))

    # return a todotxt string
    return "\n".join(result)


if __name__ == "__main__":
    # a example task from mas
    task_desc = TaskItem(
        name="Task_A",
        description="This is an example task.",
        status=TaskStatus.IN_PROGRESS,
        tags=["project1"],
        owner=["agent1", "agent2"],
        priority=1,
        due_date=datetime(2024, 6, 30),
        subtasks=[TaskItem(
                name="Task_A_1",
                description="This is the first subtask.",
                status=TaskStatus.CREATED,
                owner=['agent1'],
                priority=2),
                TaskItem(
                name="Subtask_A_2",
                description="This is the second subtask.",
                status=TaskStatus.COMPLETED,
                owner=['agent2'],
                priority=1)]
            )

    todo_lines = task_to_todotxt(task_desc)

    with open('task.txt', 'w') as file:
        file.write(todo_lines)

import pytest
from archive import ENV, MAS  # replace with your actual module and classes
from archive.typing import Task, TaskResult  # assuming these are the types defined in masr/typing

def test_main_loop():
    # Step 1: Load specific files
    env = ENV()
    task: Task = env.load_task('demand/Readme.md')  # assuming load_task returns a Task object

    # Step 2: Send the task to MAS
    mas = MAS()
    task_result: TaskResult = mas.process_task(task)  # assuming process_task returns a TaskResult object

    # Check if all user-provided tests passed
    if task_result.all_tests_passed:  # assuming all_tests_passed is a property of TaskResult
        assert env.send_mark('SUCCESS') == 'SUCCESS'
    else:
        assert env.send_mark('FAILED') == 'FAILED'
        # Back to Step 1 (expecting MAS to redo the task)
        test_main_loop()
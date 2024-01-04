from behave import given, when, then
from src.models.task import Task
from src.services.todo_list import ToDoList

@given('the to-do list is empty')
def step_given_empty_todo_list(context):
  context.todo_list = ToDoList()

@when('the user adds a task "{name}" "{description}"')
def step_when_user_adds_task(context, name, description):
  context.todo_list.add_task(name, description)

@then('the to-do list should contain {count} task in total')
def step_then_todo_list_should_contain_n_tasks(context, count):
  assert len(context.todo_list.tasks) == int(count)

@then('the to-do list should contain')
def step_then_todo_list_should_contain(context):
  for row in context.table:
    task = context.todo_list.find_task(row['Name'])
    assert task is not None, f"Task {row['Name']} not found"
    assert task.description == row['Description'], f"Expected description {row['Description']}, but got {task.description}"
    assert task.status == (row['Status'].lower() == 'true'), f"Expected status {row['Status']}, but got {task.status}"

@given('the todo list contains')
def step_given_todo_list_contains(context):
  context.todo_list = ToDoList()
  for row in context.table:
      context.todo_list.add_task(row['Name'], row['Description'], row['Status'].lower() == 'true')

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
  context.output_list = context.todo_list.list_tasks()

@when('the user marks the task {task_id} as done')
def step_when_user_marks_task_as_done(context, task_id):
  context.todo_list.mark_task_as_completed(int(task_id))
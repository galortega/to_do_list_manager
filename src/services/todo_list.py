# services/todo_list.py
import pickle
from src.models.task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, status=False):
        self.tasks.append(Task(title, description, status))

    def find_task(self, name):
        for task in self.tasks:
            if task.name == name:
                return task
        return None

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.name} - {task.description} - {'Done' if task.status else 'Not Done'}")

    def mark_task_as_completed(self, task_number):
        self.tasks[task_number - 1].mark_as_completed()
    
    def mark_task_as_uncompleted(self, task_number):
        self.tasks[task_number - 1].mark_as_uncompleted()

    def update_task(self, task_number, title, description):
        self.tasks[task_number - 1].update_task(title, description)

    def clear_list(self):
        self.tasks = []

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_from_file(self, filename):
        with open(filename, 'rb') as file:
            self.tasks = pickle.load(file)
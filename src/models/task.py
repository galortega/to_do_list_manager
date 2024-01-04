# models/task.py
class Task:
    def __init__(self, name, description, status=False):
        self.name = name
        self.description = description
        self.status = status

    def mark_as_completed(self):
        self.status = True

    def mark_as_uncompleted(self):
        self.status = False

    def update_task(self, title, description):
        self.name = title
        self.description = description

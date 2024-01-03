# models/task.py
class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.status = False

    def mark_as_completed(self):
        self.status = True

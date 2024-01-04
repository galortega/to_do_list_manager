# main.py
import argparse
from src.models.task import Task 
from src.services.todo_list import ToDoList

def main():
    parser = argparse.ArgumentParser(description='To-Do List Manager')
    parser.add_argument('command', choices=['add', 'list', 'done', 'undone', 'update', 'clear', 'save', 'load'])
    parser.add_argument('params', nargs='*')
    args = parser.parse_args()

    todo_list = ToDoList()

     # Load tasks from file at the start
    try:
        todo_list.load_from_file('tasks.pkl')
    except FileNotFoundError:
        pass  # It's okay if the file doesn't exist yet

    if args.command == 'add':
        todo_list.add_task(args.params[0], args.params[1])
        # Save tasks to file after adding a task
        todo_list.save_to_file('tasks.pkl')
    elif args.command == 'list':
        todo_list.list_tasks()
    elif args.command == 'done':
        todo_list.mark_task_as_completed(int(args.params[0]))
        todo_list.save_to_file('tasks.pkl')
    elif args.command == 'undone':
        todo_list.mark_task_as_uncompleted(int(args.params[0]))
        todo_list.save_to_file('tasks.pkl')
    elif args.command == 'update':
        todo_list.update_task(int(args.params[0]), args.params[1], args.params[2])
        todo_list.save_to_file('tasks.pkl')
    elif args.command == 'clear':
        todo_list.clear_list()
        todo_list.save_to_file('tasks.pkl')
    elif args.command == 'save':
        todo_list.save_to_file(args.params[0])
    elif args.command == 'load':
        todo_list.load_from_file(args.params[0])

if __name__ == '__main__':
    main()
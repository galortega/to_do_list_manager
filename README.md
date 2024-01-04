# to_do_list_manager
The To-Do List Manager is a command-line application that allows users to manage their tasks by adding, listing, and marking them as complete.

## Usage
`python3 main.py [command] [arguments]`

## Commands
- `add [task]`: Adds a task to the to-do list.
- `list`: Lists all tasks in the to-do list.
- `done [task number]`: Marks a task as complete.
- `undone`: Archives all completed tasks.
- `update [task number] [arguments]`: Updates a task.

## Testing
`behave --format=json --outfile=result.json`
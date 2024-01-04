Feature: To-Do List Management

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries" "Buy milk, eggs, bread and cereal"
    Then the to-do list should contain 1 task in total
    And the to-do list should contain
      | Name          | Description                    | Status |
      | Buy groceries | Buy milk, eggs, bread and cereal  | False  |

  Scenario: List all tasks in the to-do list
    Given the todo list contains
      | Name          | Description                    | Status |
      | Buy groceries | Buy milk, eggs, bread, cereal  | False  |
      | Do laundry    | Wash clothes and dry them      | False  |
    When the user lists all tasks
    Then the to-do list should contain
      | Name          | Description                    | Status |
      | Buy groceries | Buy milk, eggs, bread, cereal  | False  |
      | Do laundry    | Wash clothes and dry them      | False  |
    
  Scenario: Mark a task as done
    Given the todo list contains
      | Name          | Description                    | Status |
      | Buy groceries | Buy milk, eggs, bread, cereal  | False  |
      | Do laundry    | Wash clothes and dry them      | False  |
    When the user marks the task 1 as done
    Then the to-do list should contain
      | Name          | Description                    | Status |
      | Buy groceries | Buy milk, eggs, bread, cereal  | True   |
      | Do laundry    | Wash clothes and dry them      | False  |
  
  # Scenario: Clear the entire to-do list
  #   Given the todo list contains
  #     | Name          | Description                    | Status |
  #     | Buy groceries | Buy milk, eggs, bread, cereal  | False  |
  #     | Do laundry    | Wash clothes and dry them      | False  |
  #   When the user clears the to-do list
  #   Then the to-do list should contain 0 tasks in total

  # Scenario: Update a task's name
  #   Given the todo list contains
  #     | Name          | Description                    | Status |
  #     | Buy groceries | Buy milk, eggs, bread, cereal  | False  |
  #     | Do laundry    | Wash clothes and dry them      | False  |
  #   When the user updates the task "Buy groceries" to "Buy groceries and fruits"
  #   Then the output list should contain
  #     | Name                  | Description                    | Status |
  #     | Buy groceries and fruits | Buy milk, eggs, bread, cereal  | False  |
  #     | Do laundry            | Wash clothes and dry them      | False  |
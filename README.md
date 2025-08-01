
# TODO APP

This is a simple command-line TODO application built with Python. It allows users to manage their daily tasks through options like **add**, **show**, **remove**, **update**, and **quit**.

## Features

* ✅ Add tasks to your TODO list.
* 📋 View all tasks with numbered entries.
* ❌ Remove specific tasks by selecting their number.
* ✏️ Update or edit an existing task.
* 🚪 Quit the app with confirmation.

## How It Works

1. The program starts with a greeting: `TODO APP`.
2. It stores tasks in a list called `items`.
3. In a continuous loop, users can enter:

   * `add` — Add a new task (capitalized automatically).
   * `show` — Display all tasks with numbering.
   * `remove` — Remove a task by its number.
   * `update` — Update an existing task by its number.
   * `quit` — Exit the program after confirmation.

## Example Usage

```
TODO APP

Enter 'add, show, remove, update and quit': add
Add an item to the TODO: wash clothes

Enter 'add, show, remove, update and quit': show

_______ENTRIES_______
1.Wash clothes

Enter 'add, show, remove, update and quit': update
Type corresponding number of item to update: 1
Add an new item to the TODO: fold clothes
Fold clothes has been updated at 1. Thanks

Enter 'add, show, remove, update and quit': quit
Are you sure you want to quit? Enter either 'yes' or 'no': yes

Aww BYE! Let's achieve later, okay👋.
```

## Requirements

* Python 3.x

## How to Run

Save the code in a `.py` file (e.g., `todo_app.py`) and run using the terminal:

```bash
python todo_app.py
```



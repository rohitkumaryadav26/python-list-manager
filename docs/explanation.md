# List Utility Functions and Interactive CLI

## 1. Project Overview

This project is a simple command-line List Manager developed using Python.

It allows the user to:
- Add items to a list
- View the current list
- Delete items from the list
- Exit the application

## 2. Project Structure

- `src/main.py` - Handles the interactive CLI.
- `src/utils.py` - Contains reusable list utility functions.
- `tests/test_utils.py` - Contains tests for utility functions.
- `README.md` - Provides project information and instructions.
- `docs/explanation.md` - Explains the project implementation.

## 3. Utility Functions

The project uses separate functions for:

### Add Item
Adds a new item to the list.

### Remove Item
Removes an existing item from the list and handles the case when the item does not exist.

### Display Items
Displays the list in numbered format and shows a message when the list is empty.

## 4. Interactive CLI

The main program provides four options:

1. Add Item
2. View List
3. Delete Item
4. Exit

The program continuously accepts user input until the Exit option is selected.

## 5. Empty List Handling

The program checks whether the list contains any items before displaying it.

If the list is empty, the user receives an appropriate message instead of an empty output.

## 6. Testing

The utility functions are tested using pytest.

The tests verify:
- Adding an item
- Removing an existing item
- Handling an item that does not exist

## 7. Conclusion

The project demonstrates modular Python programming, list operations, functions, loops, conditional statements, user input handling, and basic unit testing.
# This prints the name of the app.
print("TODO APP\n")

# The todos are stored in the list 'items'.
items = []


while True:
    # Users enter 'add, show, remove, update and quit' to perform action.
    actions = input("Enter 'add, show, remove, update and quit': ")
    # A user can 'add' items. The items are appended into the list 'items'.
    if actions == "add":
        add_item = input("Add an item to the TODO: ")
        items.append(add_item.capitalize())

    # A user can enter 'show' to display the numbered contents of the list 'items'.
    if actions == "show":
        print("\n_______ENTRIES_______")
        for index, item in enumerate(items):
            print(f"{index + 1}.{item}")

    # A user can enter 'remove' to take out contents from the list 'items'.
    if actions == "remove":
        remove_update = int(input("Type corresponding number of item to remove: "))
        index = remove_update - 1
        removed = items[index].strip('\n')
        items.pop(index)
        print(f"{removed} has been removed. Thank you.")



    # A user can enter 'update' to edit an already existing content in the list 'items'.
    if actions == "update":
        old_update = int(input("Type corresponding number of item to update: "))
        new_update = input("Add an new item to the TODO: ").capitalize()
        items[old_update - 1] = new_update
        print(f"{new_update.capitalize()} has been updated at {old_update}. Thanks")

    # A user enters 'quit' to stop the program.

    if actions == str('quit'):
        exit_query = input("Are you sure you want to quit? Enter either 'yes' or 'no': ").lower()
        if exit_query == 'yes':
            print("\nAww BYE! Let's achieve later, okay👋.\n")
            break
        else:
            print("\nWow COOL! Let's achieve then🤗.\n")
            continue


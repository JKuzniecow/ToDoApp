from functions import get_todos, write_todos
#or import functions if you use modules in other directory
import time

now = time.strftime("%d.%m.%Y, %H:%m")
print("It is now:", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos)

        print(f"'{todo.capitalize()}' has been added to the list.")

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            # or new_todos = [item.strip("\n") for item in todos]
            row = f"{index + 1}. {item.capitalize()}"
            print(row)
        if not todos:
            print("Your todo list is empty.")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos)

            print(f"Todo number {number + 1} has been updated.")

        except ValueError:
            print("Your command is invalid. Please provide a number you want to edit.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            write_todos(todos)

            message = f"Todo '{todo_to_remove.capitalize()}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You entered an unknown command.")

print("Bye!")

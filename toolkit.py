print("=" * 40)
print("Welcome to My Personal Mini-Toolkit!")
print("=" * 40)
# This tool performs basic mathematical calculations.
def calculator():
    print("\n--- Simple Calculator ---")

    first_number = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    second_number = float(input("Enter the second number: "))

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            print("Sorry, you cannot divide by zero.")
            return
        result = first_number / second_number
    else:
        print(f"Sorry, '{operator}' is not a valid operator.")
        return

    print(f"The answer is: {result}")
    # This tool lets the user manage a changing list of tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' has been added.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                task_number = int(input("Enter the number of the task to remove: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' has been removed.")
                else:
                    print("That task number is not valid.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Sorry, that is not a valid choice.")
            # This tool challenges the user to guess a secret number.
def number_guessing_game():
    secret_number = 7

    print("\n--- Number Guessing Game ---")
    print("I have chosen a number between 1 and 10.")
    while True:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You guessed {secret_number} correctly!")
            break
        elif guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")
while True:
    print("\n" + "=" * 40)
    print("PERSONAL MINI-TOOLKIT")
    print("=" * 40)
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        number_guessing_game()

    elif choice == "4":
        print("\nThank you for using My Personal Mini-Toolkit!")
        print("Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")
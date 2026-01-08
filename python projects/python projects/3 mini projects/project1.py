# -----------------------------
# Calculator with History
# -----------------------------

HISTORY_FILE = "history.txt"


def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No history found.")
        else:
            print("\n--- Calculation History ---")
            for line in reversed(lines):
                print(line.strip())

    except FileNotFoundError:
        print("No history file found.")


def clear_history():
    open(HISTORY_FILE, "w").close()
    print("History cleared.")


def save_to_history(expression, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{expression} = {result}\n")


def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        raise ValueError("Use format: number operator number (example: 8 + 8)")

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator. Use +  -  *  /")

    if result.is_integer():
        result = int(result)

    print("Result:", result)
    save_to_history(user_input, result)


def main():
    print("=== SIMPLE CALCULATOR WITH HISTORY ===")
    print("Commands: history | clear | exit")
    print("Example calculation: 8 + 8\n")

    while True:
        user_input = input("Enter calculation or command: ").lower()

        if user_input == "exit":
            print("Goodbye.")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            try:
                calculate(user_input)
            except ValueError as error:
                print("Error:", error)


main()

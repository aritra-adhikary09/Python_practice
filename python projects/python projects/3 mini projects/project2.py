# Calcultor with history
History_File = "hsitory.txt"

def show_history():
    try:
        with open(History_File,"r") as f:
            lines = f.readlines()
            for line in reversed(lines):
                print(line)
    except FileNotFoundError:
        print("No history found!")
        return

def clear_history():
    open (History_File,"w").close()
    print("History cleared.")

def save_to_history(equation,result):
    with open (History_File,"a") as f:
        f.write(equation + "=" + str(result) + "\n")

def calculate(user):
    parts = user.split()    
    if len(parts) != 3:
        raise ValueError("Invalid input. Use format: Number operator number (e.g 8+8)")
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            raise ValueError("You can't divide by zero")
        else:
            result = num1/num2
    
    else:
        print("Invalid operator.use only + - * / ")
        return
    
    if int(result) == result:
        result = int(result)
    print("Rsult:",result)
    save_to_history(user,result)

def main():
    print("----SIMPLE CALCULATOR (type history, clear or exit)")
    while True:
        user = input("Enter calculation(+ - * /) or command (history, clear or exit)")
        if user == "exit":
            print("Goodbye")
            break
        elif user == "history":
            show_history()
        elif user == "clear":
            clear_history()  
        else:
            calculate(user)

main()
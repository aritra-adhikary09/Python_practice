'''Let’s create a Simple Calculator that performs arithmetic operations. Create
a function calculator(a, b, operation) that performs addition, subtraction,
multiplication, or division based on the operation parameter.  


[ operation parameter can have values ‘+’ , ‘-’ , '*’ & ‘/’ .'''

a = int(input("Enter the number:"))

b = int(input("Enter the number: "))

operation = input("Enter the operator: ")

def calculator(a,b, operation):
    if operation =='+':
        return a+b
    elif operation =='-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '/':
        if b == 0 :
            return "Error: Division by zero is not allowed."
        return a/b
    else:
        return "Invalid Operation."
    
print(calculator(a,b,'*'))


'''Q2. Create a program that:

Opens a file named log.txt in append mode

Adds a new log entry (for example: "Program run successfully")

Opens the same file in read mode and prints all log entries'''
# answer:

with open("log.txt","a") as f :
    data = f.write("program run successfully\n")

with open ("log.txt","r") as f:
    data = f.read()
    print(data)
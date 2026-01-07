'''creat a program that:
1. Opens a file "names.txt" in write mode,
2. Write 5 names (one per line) entered by the user,
3.then opens the same file in read mode and prints all names'''
# answer:

'''with open ("names.txt","w") as f:
    for i in range(5):
        name = input("Enter the name: ")
        f.write(name+ "\n")

with open ("names.txt","r") as f:
    print(f.read())'''

# if want to write names more than 5 times then use while loop

with open ("names.txt","w") as file :
    while True:
        f = input("Enter a name(To stop write'stop'): ")
        if f == "stop":
            break
        file.write(f + "\n")

with open("names.txt","r")as f:
    print("Names stored in the file:")
    print(f.read())
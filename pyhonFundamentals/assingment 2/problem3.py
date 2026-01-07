# def functions(n):
#     n=str(n)
#     for nums in n:
#         print(nums)

# n = int(input("Enter the number: "))
# functions(n)



def print_digits(n):
    while n > 0:
        digit = n % 10
        print(digit)
        n = n // 10

num = int(input("Enter the number: "))
print_digits(num)
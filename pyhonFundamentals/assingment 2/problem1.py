salary = float(input("Enter the salary amount: "))

if salary<30000:
    tax_rate = .05*100
elif 30000<=salary<=70000:
    tax_rate = .15*100
else :
    tax_rate = .25*100

print(f"Your final tax rate is: {tax_rate}% ")

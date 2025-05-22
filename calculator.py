def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "error"
    return x / y

print("select operation:")

ch = input("enter choice(+/-/*//): ")
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if ch == '+':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif ch == '-':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif ch == '*':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif ch == '/':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("invalid input")
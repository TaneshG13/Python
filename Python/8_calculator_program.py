operator = input("Enter an Operator (+ - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter first number: "))

if operator == "+":
    print(f"Answer is {num1 + num2}")
elif operator == "-":
    print(f"Answer is {num1 - num2}")
elif operator == "*":
    print(f"Answer is {num1 * num2}")
elif operator == "/":
    print(f"Answer is {num1 / num2}")
else:
    print("Enter Valid Operator :(")
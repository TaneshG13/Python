t = float(input("Enter temprature: "))
unit = input("Select Unit (F or C): ")

if unit == "F":
    print(f"your weight in celsius is {(t - 32) * (5/9)}")
elif unit == "C":
    print(f"your weight in Fahrenheit is {(t * (9/5)) + 32}")
else:
    print("Select Valid Unit :(")
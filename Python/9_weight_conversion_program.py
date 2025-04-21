w = float(input("Enter Your Weigh: "))
unit = input("Select Unit (lbs or Kg): ")

if unit == "lbs":
    print(f"your weight in kg is {w * 0.45359237}")
elif unit == "Kg":
    print(f"your weight in lbs is {w * 2.2}")
else:
    print("Select Valid Unit :(")
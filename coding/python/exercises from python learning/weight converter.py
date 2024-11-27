# python weight converter

weight = float(input("enter your weight: "))
unit = input("is it in kilograms or pounds? (K OR L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"your weight is {round(weight,1)} {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "kilogarms"
    print(f"your weight is {round(weight,1)} {unit}")

else:
    print("sorry you didnt inserted a unit from the list")

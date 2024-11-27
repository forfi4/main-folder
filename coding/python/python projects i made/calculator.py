# python calculator
import math 

while True:
    operator = input("Enter an operator ( +, -, *, /, **, square root, pi, odd or even): ")

    if operator == "+":
        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))
        result = num1 + num2
        print(f"The value is EQU {round(result, 3)} ")

    elif operator == "-":
        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))
        result = num1 - num2
        print(f"The value is EQU {round(result, 3)} ")

    elif operator == "*":
        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))
        result = num1 * num2
        print(f"The value is EQU {round(result, 3)} ")

    elif operator == "/":
        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))
        result = num1 / num2
        print(f"The value is EQU {round(result, 3)} ")         

    elif operator == "**":
        num = float(input("Enter the number: "))
        power_of = int(input("Enter the power number: "))
        result = pow(num, power_of)    
        print(f"The value is EQU {round(result, 3)}")

    elif operator == "square root":  
        num = float(input("Enter the number: "))
        result = math.sqrt(num)
        print(f"The value is EQU {round(result, 3)}")    

    elif operator == "pi":  
        result = math.pi  
        qu = input("Do you want it shortened? (Y/N): ")
        if qu == "Y" or qu == "y":  
            qu1 = int(input("How many numbers after the decimal point? (1,2,3,4): "))  
            if qu1 in [1, 2, 3, 4]:  
                print(round(result, qu1))
            else:
                print("Sorry, you either chose a number not in the list or didn't write anything.")
        elif qu == "N" or qu == "n":  
            print(f"Okay then, that's the full number: {result}")
        else:
            print("Sorry, what you entered is not valid.")

    elif operator == "odd or even":
        e = int(input("Enter the number you want to check (only whole numbers): "))
        if e % 2 == 1:
            print(f"{e} is odd")
        elif e % 2 == 0:
            print(f"{e} is even")
        else:
            print("Sorry, you either chose not a whole number or typed nothing.")
    else:
        print("Sorry, you didn't choose any operator.")

    hi = input("Do you want to continue? (Y/N): ")
    if hi == "Y" or hi == "y":  
        continue
    elif hi == "N" or hi == "n":  
        break
    else:
        print(f"{hi} is not valid.")
        break

# python compound intrest calcalator

princple = 0
time = 0 
rate = 0

while True:
    princple = float(input("enter the princple amount:"))
    if princple < 0:
        print("princple cant be less then zero: ")
    else:
        break

while True:
    rate = float(input("enter the intrest rate :"))
    if rate < 0:
        print("intrest rate cant be less then  zero: ")
    else:
        break

while True:
    time = int(input("enter the time in year/s:"))
    if time < 0:
        print("time cant be less then zero: ")
    else:
        break

total = princple * pow((1 + rate / 100), time)
print(f"balance after {time} year/s: $ {total:.2f}")


manu = {"pizza":12.90,
        "soda":2.70,
        "hotdog":3.22,
        "water":1.23,
        "pretzel":3.2,
        "popcorn":2.90}

cart =[]

total = 0

print("------------MANU-----------")
for key,value in manu.items():
    print(f"{key:10} : ${value:.2f}")
print("---------------------------")
while True:
    food = input("what would you like to order (q to quit): ").lower()    
    if food =="q":
        break
    elif manu.get(food) is not None:
        cart.append(food)

print("---------YOUR CART----------")             
for food in cart:
    total += manu.get(food)
    print(food,end=" ")

print()
print(f"your total is ${total:.2f}")
    
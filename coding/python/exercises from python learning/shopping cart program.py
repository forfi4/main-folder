# an exrecise from python learning

foods = []
prices = []
total = 0 

while True:
    food = input("enter the food you would like to buy (q to quit): ")

    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----your cart-----")        
for food in foods:
    print(food, end=" ")

for price in prices:
    total=price+total
print()    
print("----your total is----")
print(f"your total is {total}$")

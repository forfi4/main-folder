
rows = int(input("enter the number of rows: "))
coulumns = int(input("ennter the number of coulmns: "))
symbol = input("enter the symbol to use: ")

for x in range(rows):
    for y in range(coulumns):
        print(symbol,end="")
    print()    

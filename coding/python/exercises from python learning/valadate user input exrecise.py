#exrecise from python learning

username = input("enter your username: ")

length = len(username)

result ="your username must have under 12 characters:" if length > 12 else ""
print(result)

space = username.count (" ")
space = "your username must not countain any spaces" if space > 0 else ""
print(space)

digit0 = username.count("0")
digit1 = username.count("1")
digit2 = username.count("2")
digit3 = username.count("3")
digit4 = username.count("4")
digit5 = username.count("5")
digit6 = username.count("6")
digit7 = username.count("7")
digit8 = username.count("8")
digit9 = username.count("9")

if digit0 > 0 or digit1 > 0 or digit2 > 0 or digit3 > 0 or digit4 > 0 or digit5 > 0 or digit6 > 0 or digit7 > 0 or digit8 > 0 or digit9 > 0:
    print("your username must not include any numbers")

else:
    print(f"your username {username} is okay!")





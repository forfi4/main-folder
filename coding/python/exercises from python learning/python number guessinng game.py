# python number guessing game
import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
is_running = True
guesss = 0

print("PYTHON NUMBER GUESSING GAME")
print(f"select a number between {lowest_num} and {highest_num} ")

countu = 0
while is_running:
    guess = input("enter your guess:")

    if guess.isdigit():
       guess=int(guess)
       guesss+=1 
       if guess < lowest_num or guess > highest_num:
            print("that number is out of range")
            print()
            print(f"please select a number between {lowest_num} and {highest_num} ")
            countu+=1
            if countu == 3:
                print()
                print()
                print("if you wont stop writing valid things i will find you and i will touch you understood?")
                countu = 0
       elif guess < answer:
           print("too low try agian:")
       elif guess > answer:
           print("too high try again:")
       else:
           print(f"correct the answer was {answer}")
           print(f"number of guesses: {guesss}")
           again = input("do you wanna do another round? (Y/N): ").upper()
           if again =="Y":
               continue
           else:
               print("BA BYEE")
               is_running = False
               


    else:
        print("valid guess")
        print(f"please select a number between {lowest_num} and {highest_num} ")
        countu+=1
        if countu == 3:
            print()
            print()
            print("if you wont stop writing valid things i will find you and i will touch you understood?")
            countu = 0





        
  
      
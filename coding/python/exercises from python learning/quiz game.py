# a quiz game
while True:
    questions = ("how many elements are in the periodic table?",
                "which animal lays the largest eggs?",
                "what is the most abundant gas in earth's atmosphare?",
                "how many bones are in the human body",
                "which planet in the solar system is the hottest?")

    options = (("A.116", "B.117 ", "C.118 ","D.119 "),
            ("A.whale ", "B.crocodile ", "C.elphent ","D.ostrich "),
            ("A.nitrogen ", "B.oxygen ", "C.carbon -dioxide ","D.hydrogen "),
            ("A.206 ", "B.207 ", "C.208 ","D.209 "),
            ("A.mercury ", "B.venus ", "C.earth ","D.mars "))

    answers = ("C","D","A","A","B")

    guesses = []

    score = 0

    qu_num = 0

    for qu in questions:
        print("-------------------")
        print(qu)
        for option in options[qu_num]:
            print(option)

        guess = input("enter (A,B,C,D):").upper()
        guesses.append(guess)
        if guess == answers[qu_num]:
            score+=1
            print("CORRECT")
            
        else:
            print("INCORRECT")
            print(f"{answers[qu_num]} is the correct option")


        qu_num += 1    

    print("------------------")
    print("      RESULT      ")    
    print("------------------")

    print("answers:", end="")

    for answer in answers:
        print(answer,end=" ")
    print()
        
    print("guesses:",end="")    
    for guess in guesses:
        print(guess,end=" ")
    print()    

    score = int(score / len(questions) *100)
    print(f"your score is {score}%")

    print()
    i = input("do you want to start over again (Y/N):").upper()

    if i == "Y":
        continue
    else:
        print("bye bye")
        break
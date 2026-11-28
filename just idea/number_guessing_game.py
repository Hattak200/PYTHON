import random 
print("welcome to the game : ")
print(''' in this game we have laws :
                                      if you choose easy level , you should guess between 1 and 50 
                                                    medium level , you should guess between 1 and 100 
                                                    hard levet , you should guess between 1 and 500
                                      finally you have 10 attemps''')
level = input("choose your level (easy , medium , hard): ").lower()
c = 0
win = False
if level == "easy" :
    guess_computer = random.randint(1 , 50)
    while c < 10 :
        c += 1
        guess_human = int(input("enter your guess : "))
        if guess_human < guess_computer :
            print("too low !")
        elif guess_human > guess_computer :
            print("too high !")
        elif guess_human == guess_computer : 
            print(f" correct ! , you won in {c} attempts")
            win = True
            break
if win == False:
    print("you lose , your attempts is  10")

if level == "medium" :
    guess_computer = random.randint(1 , 100)
    while c < 10 :
        c += 1
        guess_human = int(input("enter your guess : "))
        if guess_human < guess_computer :
            print("too low !")
        elif guess_human > guess_computer :
            print("too high !")
        elif guess_human == guess_computer : 
            print(f" correct ! , you won in {c} attempts")
            win = True
            break
if win == False :
    print("you lose , your attempts is  10")


if level == "hard" :
    guess_computer = random.randint(1 , 500)
    while c < 10 :
        c += 1
        guess_human = int(input("enter your guess : "))
        if guess_human < guess_computer :
            print("too low !")
        elif guess_human > guess_computer :
            print("too high !")
        elif guess_human == guess_computer : 
            print(f" correct ! , you won in {c} attempts")
            win = True
            break
if win == False :
    print("you lose , your attempts is  10")



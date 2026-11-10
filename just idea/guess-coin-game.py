print("welcome to the Guess Coin Game!")
print(''' choose a methode to toss the coin :
1.random.random()
2.random.randint(1,2) ''')
methode = int(input("Enter your choice (1 or 2): "))
guess = str(input('Guess the coin toss! Enter "heads" or "tails": ')).lower()
if methode == 1 :
    import random
    toss = random.random()
    if toss < 0.5 :
        result = "heads"
    else :
        result = "tails"
        if guess.upper() == result :
            print("congratulation ! , You guessed it right! The coin landed on", result)
        else :
            print("Sorry, you guessed it wrong. The coin landed on", result ,". Better luck next time!")
elif methode == 2 :
    import random
    toss = random.randint(1, 2)
    if toss == 1 :
        result = "heads"
    else :
        result = "tails"
        if guess.upper() == result :
            print("congratulation ! , You guessed it right! The coin landed on", result)
        else :
            print("Sorry, you guessed it wrong. The coin landed on", result ,". Better luck next time!")
pin = int(input("Enter your four-digit pin: "))
if pin < 1000 or pin > 9999:
    print("Invalid pin. Please enter a four-digit number.")
else:
    print("Pin accepted.")
    import random
    genpin = random.randint(1000, 9999)
    if pin == genpin :
        print("Congratulations! You guessed the correct pin.")
    else:
        print("Sorry, the correct pin was:", genpin)



a = int(input("entrer un nombre : \n"))
b = int(input("entrer un autre nombre : \n"))
if a / b == 0:
    print("le pgcd est : ", b)
elif a / b != 0 :
    while a % b != 0:
        r = a % b
        a = b
        b = r
    print("le pgcd est : ", b)

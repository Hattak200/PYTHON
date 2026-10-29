print("bonjour \n ici on resoudre dans C une equation de deuxiéme degrée : az² + bz + c = 0  ")
a = int(input("entrer le nombre a : "))
b = int(input("entrer le nombre b : "))
c = int(input("entrer le nombre c : "))
delta = b*b - 4 * a * c
if delta > 0 :
    X1 = (-b - (delta**0.5) )/ 2*a
    X2 = (-b + (delta**0.5) )/ 2*a
    print("les solutions de l'equation est : ", X1 , X2)
elif delta == 0 :
    X = -b / (2*a)
    print("les solutions de l'equation est : ", X)
elif delta < 0 :
    print(f"les solutions de l'equation est : X1 = {-b / (2*a)} + i{(delta**0.5) / 2*a} ")
    print(f"X2 = {-b / (2*a)} - i{(delta**0.5) / 2*a}")
    



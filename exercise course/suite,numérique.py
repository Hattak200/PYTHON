print("on a la suite numérique : Un+1 = Un/2 + 3 et U0 = 1")
print("trouver le petit valeur n qui verifier : |Un - 6| < 0.001 ")
U0 = 1
n = int(input("entrer un nombre n :  "))
for i in range(1,n+1):
    Un = U0/2 + 3
    U0 = Un
    if abs(Un - 6) < 0.001 :
      print(i)
      break
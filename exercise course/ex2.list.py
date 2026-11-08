print(" U0 = 2 et Un+1 = 3Un + 1 ")
U0 = 2
U = [2]
n = int(input("Entrez le nombre de termes à calculer : "))
for i in range(1 , n):
    Un = 3 * U0 + 1
    U.append(Un)
    U0 = Un
print(f"Les {n} premiers termes de la suite sont : {U}")
print(" le terme maximal est : " , max(U))
print(" le terme minimal est : " , min(U))
print(" la somme des termes est : " , sum(U))

print("on a la suite numérique suivante : U1 = 1 , U2 = 1 , Un = Un-1 + Un-2 pour n >= 2")
n = int(input("entrer un nombre : \n"))
U1 = 1
U2 = 1
s = 2
for i in range(3,n+1):
    Un = U1 + U2
    s = s + Un
    U2 = U1
    U1 = Un
print("la somme des termes de rang", n, "est :", s)

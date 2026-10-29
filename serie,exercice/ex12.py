n = int(input(print("entrer un nombre : \n")))
s = 0
p = 1
for i in range(1,n+1):
        s = s + i
        p = p * s

print("le produit :", p)
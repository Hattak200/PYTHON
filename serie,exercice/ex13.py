n = int(input(print("entrer un nombre : \n")))
s = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        s = s+(i*j)

print("la somme :", s)
n = int(input("entrer un nombre : \n"))
c = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j) % 2 == 0 and i < j and j<= n:
            c = c + 1
print(f"le compteur = {c}")
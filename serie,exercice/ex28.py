n = int(input("entrer un nombre : \n"))
p = 1
for i in range(1,n+1):
    if i % 2 == 0 :
        for j in range(1,i+1) :
            p = p * j
    else :
        p = p * i
print("le produit est : ", p)


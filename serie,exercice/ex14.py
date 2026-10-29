n = int(input(print("entrer un nombre : \n")))
s = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2 == 0 :
            s = s + j
       

print("la somme :", s)
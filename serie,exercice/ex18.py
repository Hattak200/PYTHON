n = int(input("entrer un nombre : \n"))
m = -1
# donne le plus grande valeur qui est premier de 1 jusqu'a n et aprés le mettre au carré
for i in range(1,n+1):
    cmpt = 0
    for j in range(1,n+1):
        if i % j == 0 :
            cmpt = cmpt + 1 
    if cmpt == 2 :
     pr = i 
     if pr > m :
        m = pr 
print(' M = ' , m * m)

            

        


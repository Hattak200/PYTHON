n = int(input(print("entrer un nombre : \n")))
c = 0
for i in range(1,n+1):
    if i%3==0:
        c = c + 1
print("la compteur :", c)
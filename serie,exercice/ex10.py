n = int(input(print("entrer un nombre : \n")))
s = 0
if n <= 50 :
    for i in range(1,n+1):
        s = s + i
elif n> 50 :
    for i in range(1,51):
        s = s + i
print("la somme :", s)
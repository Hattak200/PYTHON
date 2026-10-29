n = int(input("entrer un nombre : \n"))
s = 0
for i in range(1,n+1):
    if i % 2 == 0:
        r = 2
    elif i % 2 != 0:
        r = 3
    s = s + r**i
print("la somme :", s)
n = int(input(print("entrer un nombre : \n")))
s = 0
for i in range(1,n+1):
    if i%2!=0:
        s = s + 1/(i*i)
    elif i%2 == 0 :
        s = s + 1/i
print("la somme :", s)
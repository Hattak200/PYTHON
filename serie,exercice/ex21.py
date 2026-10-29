n = int(input(print("entrer un nombre : \n")))
s = 0
for i in range(1,n+1):
    if i%2==0 and i%3==0:
        s = s + (i*i)
    elif i%2 == 0 or i%3==0 :
        s = s + i
print("la somme :", s)
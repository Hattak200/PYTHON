n = int(input(print("entrer un nombre : \n")))
s = 0
for i in range(1,n+1):
    s = s +( (-1)**(i+1) * i)
print("la somme :", s)
def Somme(n):
    somme = 0
    for i in range(1,n+1):
        somme = somme + i
    return somme
n = int(input("entrer un nombre n : \n"))
print(f'{Somme(n)}')
     
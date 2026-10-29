def puissance(x) :
    for i in range(1,21):
        resultat = x**i
        print(resultat)
    return resultat

x = int(input("entrer un nombre x : \n"))
print(f'{puissance(x)}')


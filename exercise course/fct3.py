def Pair(n):
    for i in range(1,n+1):
        if i % 2 == 0 :
            pair = i
            print(i) 
    return pair
n = int(input("entrer un nombre n : \n"))
print(f'{Pair(n)}')
     
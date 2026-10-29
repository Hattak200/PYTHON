n = int(input(print("entrer un nombre : \n")))

for i in range(0,n+1):
        if i%2 != 0 :
               pr = i
               if pr >= n-1 :
                  m = pr
                  print(m*m)
        else:
            print("-infini")
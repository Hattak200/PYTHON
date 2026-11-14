def perfect_num(s,n) :
    for i in range( 1 , n) :
        if n % i == 0 :
            s = s + i
    return s
n = int(input("enter a number : "))
s = 0
result = perfect_num(s,n)
if n == result :
    print(f"{result} is a perfect number")
else :
    print(f"{n} is not a perfect number")
def pgcd(a,b):
    if a % b == 0 :
        return b
    else :
        return pgcd(b, a % b)
a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
print(f" pgcd({a};{b}) is {pgcd(a,b)}")
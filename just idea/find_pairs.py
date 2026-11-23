def find_pairs(numbers , target ):
    pairs = []
    for i in range(0,len(numbers)):
        for j in range(i+1 , len(numbers)):
            if i + j == target :
                pairs.append(f"({i},{j})")
    return pairs
numbers = set()
pairs = []
n = int(input("enter the number of the list : "))
for d in range(0,n):
    num = int(input("enter a number  : "))
    numbers.add(num)
target = int(input("enter the target : "))
print(f" the pairs of the target {target}  :  {find_pairs(numbers , target)}")


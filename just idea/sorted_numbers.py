def sorte(list):
    for i in range(0,len(list)):
        for j in range(i+1 , len(list)):
            if list[i] > list[j] :
                change = list[i]
                list[i] = list[j]
                list[j] = change
            else :
                continue
    return list
n = int(input("enter number of the list : "))
list = []
for i in range(0,n):
    i = int(input("enter a random number to create a list not sorted : "))
    list.append(i)
print(f"your list : {sorte(list)}")





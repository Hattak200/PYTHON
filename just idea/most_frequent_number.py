n = int(input(' how much numbers do you want enter in the list :  '))
list = []
for i in range(0,n):
    i = int(input(f'enter the number {i+1} : '))
    list.append(i)
maximum = 0
for j in list :
    c = 0
    for k in list :
        if j == k :
            c += 1
    if c > maximum :
        maximum = c
        freq = j
print(f''' the most frequent number is {freq} 
            occurrences : {c} ''')


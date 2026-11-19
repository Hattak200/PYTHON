lignes = int(input("enter number of lignes : "))
collone = int(input("enter number of the column : "))
matrix = []
for i in range(0 , lignes) :
    list = []
    for j in range(0 , collone):
        num = int(input("enter a number : " ))
        list.append(num)
    matrix.append(list)
print("your matrix : " , matrix)
new_matrix = []
for j in range(0 , collone):
    new_list = []
    for i in range(0 , lignes):
        new_list.append(matrix[i][j])
    new_matrix.append(new_list)
print("the new matrix :" ,new_matrix)



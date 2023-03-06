import numpy as np

array = [[-9,-9,-9,1,1,1],[0,-9,0,4,3,2],[-9,-9,-9,1,2,3],[0 ,0 ,8,6,6,0],[0,0,0,-2,0,0],[0,0,1,2,4,0]]

matrix = np.matrix(array)


print(matrix)
array1 = []
array2 = []
array3 = []
array4 = []
array5 = []
array6 = []


for coluna in range(3):
    for linha in range(3):
        array1.append(matrix[coluna,linha])

for coluna in range(3):
    for linha in range(3,6):
        array2.append(matrix[coluna,linha])
        
for coluna in range(3):
    for linha in range(3,6):
        array3.append(matrix[linha,coluna])
        
for coluna in range(3,6):
    for linha in range(3,6):
        array4.append(matrix[linha,coluna])


array1[3]=0
array1[5]=0
array2[3]=0
array2[5]=0
array3[1]=0
array3[7]=0
array4[1]=0
array4[7]=0



array1 = sum(array1)
array2 = sum(array2)
array3 = sum(array3)
array4 = sum(array4)

print(array1)
print(array2)
print(array3)


arra1
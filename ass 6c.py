import numpy as np
r1=int(input("Enter the rows of matrix 1: "))
c1=int(input("Enter the cols of matrix 1: "))
r2=int(input("Enter the rows of matrix 2: "))
c2=int(input("Enter the cols of matrix 2: "))
mat1 = np.zeros([r1,c1],dtype='int')
mat2 = np.zeros([r2,c2],dtype='int')

for i in range(0,r1):
    print("Enter integer for {}-ROW:".format(i))
for j in range(0,c1):
    mat1[i][j] = int(input())
for i in range(0,r2):
    print("Enter integer for {}-ROW:".format(i))
for j in range(0,c2):
    mat2[i][j] = int(input())
res = np.matmul(mat1,mat2) #mat1 @ mat2
print(res)


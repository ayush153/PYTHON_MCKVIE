# 1D LIST

l1 = []
n = int(input("Enter the range of list-"))
for i in range(n):
    a = int(input("Enter numbers: "))
    l1.append(a)

print("The list is-", l1)

max1 = max(l1)
print("The max no is-", max1)

min1 = min(l1)
print("The min no is-", min1)

# 2D LIST

r = int(input("Enter the row size-"))
c = int(input("Enter the coulmn size-"))
matrix = [0]*r
for i in range(0,r):
    rw = [0]*c
    print('Enter  integer for {}-row:'.format(i))
    for j in range(0,c):
        rw[j] = int(input())
    matrix[i] = rw
max1 = list()
for i in matrix:
    print(i)
    max1 = max1 + [max(i)]
print(max(max1))

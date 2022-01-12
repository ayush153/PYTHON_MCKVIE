l1 = []
n = int(input("Enter the range of list-"))
for i in range(n):
    a = int(input("Enter the element: "))
    l1.append(a)
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)

print("After removing duplicates-", l2)

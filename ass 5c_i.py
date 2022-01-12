n = 5
for i in range(1,(n//2)+2):
    for j in range((n//2)-i+1):
        print(" ",end=" ")
    for j in range((i*2)-1):
        print("*",end=" ")
    print()

for i in range(n//2,0,-1):
    for j in range(n//2-i+1):
        print(" ", end=" ")
    for j in range((i * 2) - 1):
         print("*", end=" ")
    print()









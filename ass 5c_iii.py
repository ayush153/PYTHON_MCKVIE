n=5
for i in range (n,0,-1):
    for j in range(i):
        print(chr(65+j),end="")
    print(" "*(n-i),end="")
    print(" "*(n-i), end="")
    print("\b",end="")
    for j in range(i-1, -1, -1):
        print(chr(65 + j), end="")
    print("")





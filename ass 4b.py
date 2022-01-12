s = int(input("Enter lower range: "))
e = int(input("Enter upper range: "))

print("The prime numbers are :")
for num in range(s, e + 1):
    if num > 1:
        for i in range(2, int(num ** .5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")




a = eval(input("Enter 1st number :"))
b = eval(input("Enter 2nd number :"))
c = eval(input("Enter 3rd number :"))
if a <= b:
    if b > c:
        print("{} is greatest among three numbers".format(b))
    else:
        print("{} is greatest among three numbers".format(c))
else:
    if a > c:
        print("{} is greatest among three numbers".format(a))
    else:
        print("{} is greatest among three numbers".format(c))


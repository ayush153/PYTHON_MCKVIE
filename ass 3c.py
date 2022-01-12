a = eval(input("Enter the 1st number: "))
b = eval(input("Enter the 2nd number: "))
c = eval(input("Enter the 3rd number: "))
d = b*b - 4*a*c
if a == 0:
    print("Not a quadratic equation")
elif d > 0:
    r1 = float(-b+d**0.5)/(2*a)
    r2 = float(-b-d**0.5)/(2*a)
    print("The roots are real and unequal and are {} and {}" .format(r1,r2))
elif d == 0:
    r = -b/(2*a)
    print("The roots are real and equal and that is {}" .format(r))
else:
    d = -1*d
    real = -b/(2 * a)
    imag = ((d**0.5)/(2*a))
    R1 = complex(real,imag)
    R2 = R1.conjugate()
    print("{} and {} are the imaginary roots." .format(R1, R2))


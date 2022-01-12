basic = eval(input("Enter the basic pay drawn by the Employee :"))
agp = basic * 0.5
merged = agp + basic
da = 0.5 * merged
hra = 0.15 * merged
total = merged + da + hra
print("Total salary drawn by the employee = ",'%0.2f'%total)

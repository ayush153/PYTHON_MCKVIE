unit=int(input("Enter the unit consume:"))
if(unit<=200):
    bill = unit*0.50
if unit>200 and unit<=400:
    bill = unit*0.65+100
if unit>400 and unit<=600:
    bill = unit*0.80+200
if unit>600:
    bill = unit*1.00+300
print("BILL is",bill)
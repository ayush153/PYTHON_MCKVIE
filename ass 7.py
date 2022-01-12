'''7A
s1 = "Hello world! "
up = 0
lw = 0
for i in s1:
    if(65 <= ord(i) <= 90):
        up+=1
    if(97 <= ord(i) < 122):
            lw+=1
print(up,lw)'''

'''7B
s1 = "Hello World. I am AYUSH."
s2 = "Hello , I am KUMAR."
l1 = s1.split()
l2 = s2.split()
t1 = set(l1)
t2 = set(l2)
t3 = t1.intersection(t2)
print(t3)'''

'''7C
s = input("Enter a word separated by comma:")
l1 = s.split(',')
l2 = sorted(l1)
for x in l2:
    print(x,end=",")
print()'''

'''7D
a= input("Enter the EMAIL ID.")
b = a.index('@')
c = a.index('.')
i = a[b+1:c]
print(i)'''



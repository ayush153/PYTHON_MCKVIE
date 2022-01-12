import math as m
for i in range(100,1000):
  sum = 0
  j = i

  while(j > 0):
    r = j % 10
    f = m.factorial(r)
    sum = sum + f
    j = j // 10
  if(sum == i):
      print("Special numbers are:-",i)





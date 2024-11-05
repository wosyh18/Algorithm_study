import random

values = []

for _ in range (9) :
   value = int(input())
   values.append(value)
   

   randlist = []
   
while True :
   randlist = random.sample(values,7)
   k = sum(randlist)
   if (k == 100):
      break
   
randlist.sort()

for num in randlist:
   print(num)
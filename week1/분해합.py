num = int(input())
k = 1

while True:
   s = 0  

   for i in str(k):
      s += int(i)  

   if s == num:
      print(k)  
      break
   elif s > num:
      print(0)
      break  

   k += 1  
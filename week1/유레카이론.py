triangle= []
for i in range (1,46) :
   triangle.append(i*(i+1)//2)

n = int(input())
found = False
for a in triangle :
   for b in triangle :
      for c in triangle :
            if a + b + c == n :
               found = True
               break
      if found :
            break
   if found : 
      break

if found :
   print(1)
else :
   print(0)
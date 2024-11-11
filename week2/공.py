m = int(input())

cups = [1,2,3]

for _ in range(m) :
   a,b = map(int,input().split())
   temp = cups [a-1]
   cups[a-1] = cups[b-1]
   cups[b-1] = temp

for i in cups :
   if i == 1 :
      print (cups.index(i)+1)
      break
   
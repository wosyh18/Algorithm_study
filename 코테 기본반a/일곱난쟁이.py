import random


nanjang = [int(input().strip()) for _ in range (9)]
result_nanjang = [0]*9

while sum(result_nanjang) != 100 :
   nanjang_minus = random.sample(nanjang,2)

   result_nanjang = [element for element in nanjang if element not in nanjang_minus]

result_nanjang.sort()
for i in result_nanjang:
   print(i)
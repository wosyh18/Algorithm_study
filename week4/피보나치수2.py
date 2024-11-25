# 피보나치 함수
def fibo(k):
   fibo_list = [0] * (k+1)
   fibo_list[0] = 0
   fibo_list[1] = 1
   for i in range(2,k+1):
      fibo_list[i] = fibo_list[i-1]+fibo_list[i-2]
   
   print(fibo_list[k])

n = int(input())
fibo(n)




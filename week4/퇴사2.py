N = int(input())
T = [0]*N
P = [0]*N
for i in range (N) :
   T[i], P[i] = map(int,input().split)
   
dp = [0] * [N+1] #+1은 초기값
for n in range ( N-1, -1 ,-1) : #뒤에서 앞으로 (완료 기준)
   if n+T[n] <= N : #기간 내 상담 O
      dp[n]=max(dp[n+1], dp[n+T[n]+P[n]])
   else :
      dp[n] = dp[n+1]
      
print (dp[0])

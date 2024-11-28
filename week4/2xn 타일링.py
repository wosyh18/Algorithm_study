blocks = list(input())
n = input(int())
dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
   for j in range(i + 1, n):
      if (blocks[i] == 'B' and blocks[j] == 'O') or \
         (blocks[i] == 'O' and blocks[j] == 'J') or \
         (blocks[i] == 'J' and blocks[j] == 'B'):
            dp[j] = min(dp[j], dp[i] + (j - i) ** 2)


result = dp[-1]
if result == float('inf'):
   print(-1)
else:
   print(result)
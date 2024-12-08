#입력받기
n = int(input())
dungchi = [tuple(map(int,input().split())) for _ in range(n)]

ranks = []
for i in range(n):
   rank = 1
   for j in range(n):
      if i != j and dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
         rank += 1
   5
55 185
58 183
88 186
60 175
46 155ranks.append(rank)

print(*ranks)
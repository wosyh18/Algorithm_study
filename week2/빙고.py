a = [list(map(int, input().split())) for _ in range(5)]  # 빙고판을 숫자로 저장
b = [[False] * 5 for _ in range(5)]  # 불린 숫자 상태 체크
num = [list(map(int, input().split())) for _ in range(5)]  # 사회자가 부르는 숫자
bingocnt = 0  # 빙고 개수

# 사회자가 부른 숫자 리스트를 1차원 리스트로 변환
num_list = sum(num, [])

for count, n in enumerate(num_list, start=1):
   # 빙고판에서 숫자 위치를 찾아 True로 표시
   for row in range(5):
      for col in range(5):
            if a[row][col] == n:
               b[row][col] = True
               break

   # 빙고 개수 초기화
   bingocnt = 0

   # 가로 줄 체크
   for row in b:
      if all(row):
            bingocnt += 1

   # 세로 줄 체크
   for col in range(5):
      if all(b[row][col] for row in range(5)):
            bingocnt += 1

   # 대각선 체크
   if all(b[i][i] for i in range(5)):
      bingocnt += 1
   if all(b[i][4 - i] for i in range(5)):
      bingocnt += 1

   # 빙고가 3개 이상일 때
   if bingocnt >= 3:
      print(count)
      break

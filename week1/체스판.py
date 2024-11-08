N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

change = [[0] * (M - 7) for _ in range(N - 7)]

for i in range(N - 7):
   for j in range(M - 7):
      changes_W = 0  
      changes_B = 0  
      
      # 8x8 보드 탐색
      for x in range(8):
            for y in range(8):
               if (x + y) % 2 == 0:
                  if board[i + x][j + y] != 'W':  # [짝][짝] or [홀][홀]이 W여야 함
                        changes_W += 1
                  if board[i + x][j + y] != 'B':  # [짝][짝] or [홀][홀]이 B여야 함
                        changes_B += 1
               else:  # 홀수 위치
                  if board[i + x][j + y] != 'B':  # [짝][홀] or [홀][짝]이 B여야 함
                        changes_W += 1
                  if board[i + x][j + y] != 'W':  # [짝][홀] or [홀][짝]이 W여야 함
                        changes_B += 1

      change[i][j] = min(changes_W, changes_B)

min_changes = min(min(row) for row in change)
print(min_changes)

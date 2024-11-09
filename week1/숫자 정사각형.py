n, m = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

max_length = 1

for i in range(n):
   for j in range(m):
      for k in range(1, min(n, m)):
            if i + k < n and j + k < m:
               if (matrix[i][j] == matrix[i][j + k] and
                  matrix[i][j] == matrix[i + k][j] and
                  matrix[i][j] == matrix[i + k][j + k]):
            
                  max_length = max(max_length, k + 1)


print(max_length * max_length)
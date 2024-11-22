dirR = [1,-1,0,0] #상하
dirC = [0,0,1,-1] #좌우

#dfs 1.방문 표시 바꾸고 -> 2.연결노드 방문 표시 없으면 -> 3. 연결 노드 방문하기
def dfs(y,x):
   global visited
   #1
   visited[y][x] = 1
   #2
   for(n) in range(4):
      newY = y + dirR[n]
      newX = x + dirC[n]
      if graph[newY][newX] and not visited[newY][newX]:
         dfs(newY,newX)
   
# 0. 입력 받기, 초기화 
T = int(input())
M , N , K = map(int,input().split())
for _ in range (T) :

   graph = [0 for _ in range (N+1) for _ in range(M+1) ]
   visited = [0 for _ in range (N+1) for _ in range(M+1) ]

   #1. 그래프 입력 받기
   for _ in range (K) :
      x,y = map(int, input().split())
      graph[y+1][x+1] = 1
      '가로(x) 세로(y) ->  list[y][x]'
      'x+1 , y+1 로 설정 -> (1,1)부터 시작하게끔 해서 겉 테두리가 생기니까 범위를 벗어나는지 확인하지 않아도 배추가 존재하는지만 확인하면 됨 => dfs,bfs 사용시 쓰면 편함'

      #2. graph 순회하며 dfs 돌기
      answer = 0
      for i in range (1,N+1) :
         for j in range (1,M+1) :
            if graph[i][j] and not visited[i][j] :
               dfs(i,j)
               answer +=1
      print (answer)






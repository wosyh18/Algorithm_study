#dfs
def dfs(c) :
   ans_dfs.append(c) # 방문 노드 추가
   v[c] = 1 # 방문 표시

   for n in adj[c] :
      if not v[n] :
         dfs(n)

#bfs
def bfs (s) :
   q = [] # 방문 예정 노드 리스트
   q.append(s) # 시작 노드를 q에 넣어두고 시작
   ans_bfs.append(s)
   v[s] =1

   while q :
      c = q.pop(0)
      for n in adj[c] : # q에 든 수(c) 꺼내서 q와 연결된 인접 노드 차례대로 보기 
         if not v[n] : # c와 연결된 수 중 방문 안 한 수는 방문 예정 리스트에 넣기
            q.append(n)
            ans_bfs.append(n)
            v[n] =1

#N = 정점 개수 M = 간선 개수 V = 시작 번호
N , M , V = map(int, input().split())

adj = [[]for _ in range (N+1)] #인접 리스트 생성

#인접 리스트에 주어진 값 넣기
for _ in range (M) :
   s, e = map(int, input().split())
   adj[s].append(e)
   adj[e].append(s)

#오름차순 정렬
for i in range (N+1) :
   adj[i].sort()

v = [0]* (N+1) #방문 여부 리스트
ans_dfs = [] 
dfs(V)
print(*ans_dfs)

v = [0]* (N+1) #방문 여부 리스트
ans_bfs = []
bfs(V)
print(*ans_bfs)

'''
# deque 이용해서 bfs 구현
form collections import deque

def BFS(adj,start,v) :
   queue = deque([start]) #시작값을 넣은 큐를 만들기
   v[start] =1 #시작값 방문 O

   while queue : #큐에 값이 있는 동안
      c = queue.popleft() #큐에서 수를 빼서 
      for i in adj[c]:#큐에서 뺀 수와 인접한 값을 방문 안 했다면 
         if not v[c]:
            queue.append(c)#방문 안 한 값을 큐에 넣고 
            v[c] = 1 #방문 추가
'''
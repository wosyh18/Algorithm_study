import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 증가

def dfs(c):
   v[c] = 1  # 방문 표시
   for n in adj[c]:
      if not v[n]:
            dfs(n)

# N = 정점 개수, M = 간선 개수
N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]  # 인접 리스트 생성

# 인접 리스트에 주어진 값 넣기
for _ in range(M):
   s, e = map(int, input().split())
   adj[s].append(e)
   adj[e].append(s)

v = [0] * (N+1)  # 방문 여부 리스트
count = 0  # 연결 요소의 개수

# 모든 노드에 대해 DFS 실행
for i in range(1, N+1):
   if not v[i]:  # 아직 방문하지 않은 노드라면
      dfs(i)  # DFS 실행
      count += 1  # 연결 요소 개수 증가

print(count)  # 연결 요소의 개수 출력
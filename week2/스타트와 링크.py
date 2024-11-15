from itertools import combinations

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def calculate_team(team):
   return sum(board[i][j] for i in team for j in team if i != j)

min_diff = float('inf')
all_players = set(range(N))

for start_team in combinations(range(N), N//2):
   start_team = set(start_team)
   link_team = all_players - start_team
   
   start_stat = calculate_team(start_team)
   link_stat = calculate_team(link_team)
   
   diff = abs(start_stat - link_stat)
   min_diff = min(min_diff, diff)

print(min_diff)
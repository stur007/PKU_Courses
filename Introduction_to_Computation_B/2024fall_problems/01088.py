import sys
from functools import lru_cache

sys.setrecursionlimit(1<<30)

r, c = map(int, input().split())
maze = []
for _ in range(r):
    s = list(map(int, input().split()))
    maze.append(s)

visited = [[0]*c for _ in range(r)]

def scope(x, y):
    return 0<= x <r and 0<= y <c

@lru_cache(maxsize=None)
def dfs(x, y):
    temp = 0
    for dx, dy in [(0, 1), (0 ,-1), (1, 0), (-1, 0)]:
        nx, ny = x+dx, y+dy
        if scope(nx, ny) and maze[nx][ny] > maze[x][y]:
            temp = max(dfs(nx, ny)+1, temp)
    return temp

ans = 0
for i in range(r):
    for j in range(c):
        ans = max(ans, dfs(i, j))
print(ans+1)
from collections import deque
import sys
sys.setrecursionlimit(1<<30)

n = int(input())
maze = []
for _ in range(n):
    s = input()
    m = len(s)
    maze.append(s)

visited1 = [[False]*m for _ in range(n)]

def scope(x, y):
    return 0<=x<n and 0<=y<m

def dfs(x, y, visited):
    visited[x][y] = True ### 这个顺序可以保证初始点被直接打上标记
    for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if scope(nx, ny) and not visited[nx][ny] and maze[nx][ny] == '1':
            dfs(nx, ny, visited)

def bfs(x, y, step):
    q = deque([(x, y, step)])
    inqueue = {(x, y)}

    while q:
            x, y, step = q.popleft()
            for dx, dy in [(0 ,1), (0, -1), (-1, 0), (1, 0)]:
                nx = x + dx
                ny = y + dy
                if scope(nx, ny) and maze[nx][ny] == '1' and not visited1[nx][ny]:
                    return step
                if scope(nx, ny) and (nx, ny) not in inqueue:
                    if maze[nx][ny] == '1':
                        q.appendleft((nx, ny, step))
                    elif maze[nx][ny] == '0':
                        q.append((nx, ny, step+1))
                    inqueue.add((nx, ny))


def find_1():
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '1':
                dfs(i ,j, visited1)
                return bfs(i, j, 0)
print(find_1())
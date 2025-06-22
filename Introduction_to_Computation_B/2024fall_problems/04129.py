from collections import deque

def scope(x, y):
    return  0<=x<r and 0<=y<c


def bfs(a, b):
    q = deque([(0, a, b)])
    inqueue = {0, a, b}
    while q:
            step, x, y = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if scope(nx, ny):
                    if maze[nx][ny] == 'E':
                        return step + 1
                    if ((step+1)%k, nx, ny) not in inqueue:
                        if maze[nx][ny] != '#' or (step + 1) % k == 0:
                            q.append((step+1, nx, ny))
                            inqueue.add(((step+1)%k, nx, ny))
    return 'Oop!'

t = int(input())
for _ in range(t):
    r, c, k = map(int, input().split())
    maze = []
    for _ in range(r):
        maze.append(input())
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'S':
                print(bfs(i, j))
                break

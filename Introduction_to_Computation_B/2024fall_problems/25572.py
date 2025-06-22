from collections import deque

n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]

def scope(x, y):
    return 0<=x <n and 0<=y <n and maze[x][y] != 1

def bfs(a1, b1, a2, b2):
    temp = deque([(a1, b1, a2, b2)])
    inq = {(a1, b1, a2, b2)}
    while temp:
        x1, y1, x2, y2 = temp.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx1, ny1, nx2, ny2 = x1+dx, y1+dy, x2+dx, y2+dy
            if scope(nx1, ny1) and scope(nx2, ny2):
                if maze[nx1][ny1] == 9 or maze[nx2][ny2] == 9:
                    return 'yes'
                else:
                    if (nx1, ny1, nx2, ny2) not in inq:
                        inq.add((nx1, ny1, nx2, ny2))
                        temp.append((nx1, ny1, nx2, ny2))
    return 'no'

for i in range(n):
    for j in range(n):
        if maze[i][j] == 5:
            x, y = i, j
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx = x+dx
                ny = y+dy
                if scope(nx, ny) and maze[nx][ny] == 5:
                    print(bfs(x, y, nx, ny))
                    exit()


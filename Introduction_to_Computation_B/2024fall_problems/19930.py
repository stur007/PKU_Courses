from collections import deque

def scope(x, y):
    if 0 <= x <m and 0<= y < n:
        return True
    else:
        return False

def bfs():
    queue = deque([(0, 0)])
    inQueue = [[False] * n for _ in range(m)]
    inQueue[0][0] = True
    step = 0
    if s[0][0] == 1:
        return step
    while queue:
        l = len(queue)
        for _ in range(l):
            (x, y) = queue.popleft()
            for dx, dy in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                nx = x+dx
                ny = y+dy
                if scope(nx, ny) and not inQueue[nx][ny]:
                    if s[nx][ny] == 1:
                        return step+1
                    elif s[nx][ny] == 0:
                        queue.append((nx, ny))
                        inQueue[nx][ny] = True
        step += 1
    return 'NO'

m, n = map(int, input().split())
s = []
for _ in range(m):
    s.append(list(map(int, input().split())))
print(bfs())
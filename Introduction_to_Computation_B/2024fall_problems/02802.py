from collections import deque

o = 0
while True:
    o += 1
    w, h = map(int, input().split())
    if w == h == 0:
        break
    s = [list(input()) for _ in range(h)]
    maze = [[0]*(w+2) for _ in range(h+2)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'X':
                maze[i+1][j+1] = 1

    def scope(i, j):
        return 0<=i<=h+1 and 0<=j<=w+1

    def bfs(a, b, c, d, step):
        visited = [[False]*(w+2) for _ in range(h+2)]
        q = deque([(a, b)])
        if a == c and b == d:
            return step
        while q:
            length = len(q)
            for _ in range(length):
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    for g in range(1, max(w, h)):
                        nx = x+g*dx
                        ny = y+g*dy
                        if nx == c and ny == d:
                            return step+1
                        if not scope(nx, ny):
                            break
                        if maze[nx][ny] == 1:
                            break
                        if scope(nx, ny) and maze[nx][ny] == 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

            step += 1

    print(f'Board #{o}:')
    t = 0
    while True:
        t += 1
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == y1 == x2 == y2 == 0:
            print()
            break
        ans = bfs(y1, x1, y2, x2, 0)
        if ans != None:
            print(f'Pair {t}: {ans} segments.')
        else:
            print(f'Pair {t}: impossible.')
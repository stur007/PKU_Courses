t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = []
    for _ in range(n):
        str = input()
        temp = []
        for i in range(m):
            temp.append(str[i])
        s.append(temp[:])

    ans = 0
    def scope(x, y):
        if 0<= x <n and 0 <= y < m:
            return True
        else:
            return False

    def dfs(x, y):
        global d
        d += 1
        s [x][y] = '.'
        for dx, dy in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
            nx = x+dx
            ny = y+dy

            if scope(nx, ny):
                if s[nx][ny] == 'W':
                    dfs(nx, ny)
    for i in range(n):
        for j in range(m):
            if s[i][j] == 'W':
                d = 0
                dfs(i, j)
                ans = max(ans, d)

    print(ans)


t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    def scope(i, j):
        return 0<= i < n and 0<= j <m

    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    cnt = 0
    def dfs(i, j,step):
        global cnt
        if step == n*m:
            cnt += 1
        for di, dj in [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            ni = i+di
            nj = j +dj
            if scope(ni, nj):
                if not visited[ni][nj]:
                    visited[ni][nj] = True
                    dfs(ni, nj,step+1)
                    visited[ni][nj] = False

    dfs(x, y, 1)
    print(cnt)
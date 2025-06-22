t = int(input())
def dfs(least, most, idx, n):
    global cnt
    if idx == n and least <= most:
        cnt += 1
        return
    for i in range(least, most+1):
        dfs(i, most-i, idx+1, n)
for _ in range(t):
    m ,n = map(int, input().split())
    cnt = 0
    dfs(0, m, 1, n)
    print(cnt)
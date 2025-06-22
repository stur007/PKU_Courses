import sys
input = sys.stdin.read

def f():
    data = input().split()
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    idx = 3
    dp = [[0]*m for _ in range(n+1)]
    for _ in range(k):
        x, y = int(data[idx]), int(data[idx+1])
        idx += 2
        for b in range(n, x-1, -1):
            for c in range(m-1, y-1, -1):
                dp[b][c] = max(dp[b][c], dp[b-x][c-y]+1)
    ans = dp[-1][-1]
    i = dp[-1].index(ans)
    return f"{ans} {m-i}"

print(f())
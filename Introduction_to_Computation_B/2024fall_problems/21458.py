T, n = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]

dp = [0]+[-float('inf')]*T

for i in range(1, n+1):
    for j in range(T, s[i-1][0]-1, -1):
            dp[j] = max(dp[j], dp[j- s[i-1][0]]+s[i-1][1])

if dp[-1] == -float('inf'):
    print(-1)
else:
    print(dp[-1])
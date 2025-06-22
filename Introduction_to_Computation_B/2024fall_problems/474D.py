t, k = map(int, input().split())
n = 10**5
m = 10**9+7
dp = [1] *(n+1)
pre = [0]*(n+1)
for i in range(n+1):
    if i-k >= 0:
        dp[i] = (dp[i-1]+dp[i-k])%m
    pre[i] = (pre[i-1]+dp[i])%m
for _ in range(t):
    a, b = map(int ,input().split())
    ans = pre[b]-pre[a-1]
    if ans < 0:
        ans += m
    print(ans)

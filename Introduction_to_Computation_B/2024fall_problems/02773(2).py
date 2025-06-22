t, m = map(int,input().split())
dp = [[0]*(t+1) for _ in range(m+1)]
for i in range(1, m+1):
    t_i, m_i = map(int,input().split())
    for j in range(1, t+1):
        if t_i <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-t_i]+m_i)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
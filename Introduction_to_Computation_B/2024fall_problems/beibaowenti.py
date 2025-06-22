n, V = map(int,input().split())
w = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
dp = [[0]*(V+1) for _ in range(n+1)]
for i in range(1,n+1):
    for v in range(1,V+1):
        if w[i-1] <= v:
            dp[i][v] = max(dp[i-1][v], dp[i-1][v-w[i-1]]+c[i-1])
        else:
            dp[i][v] = dp[i-1][v]
print(dp[-1][-1])


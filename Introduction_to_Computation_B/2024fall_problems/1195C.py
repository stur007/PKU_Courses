n = int(input())
dp = [[0]*4 for _ in range(n+1)]
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
for i in range(1,n+1):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = max(dp[i-1][0], dp[i-1][2])+s1[i-1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1])+s2[i-1]
    dp[i][3] = max(dp[i][0], dp[i][1], dp[i][2], dp[i-1][3])
print(dp[-1][-1])

n = int(input())
s = list(map(int, input().split()))
dp = [[0]*3]+[[200]*3 for _ in range(n)]
for i in range(n):
    if s[i] == 0:
        dp[i+1][0] = min(dp[i])+1
    elif s[i] == 1:
        dp[i+1][0] = min(dp[i])+1
        dp[i+1][1] = min(dp[i][0], dp[i][2])
    elif s[i] == 2:
        dp[i+1][0] = min(dp[i])+1
        dp[i+1][2] = min(dp[i][0], dp[i][1])
    else:
        dp[i+1][0] = min(dp[i])+1
        dp[i+1][1] = min(dp[i][0], dp[i][2])
        dp[i+1][2] = min(dp[i][0], dp[i][1])
print(min(dp[-1]))

### 注意到把自己难住的地方就是dp的思路起点！
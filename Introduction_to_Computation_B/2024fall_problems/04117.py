dp = [[0] * 51 for _ in range(51)]
for i in range(1, 51):
    for j in range(1, 51):
        if j > i:
            dp[i][j] = dp[i][i]
        elif i == j:
            dp[i][j] += sum(dp[i - x][x] for x in range(1, j))
            dp[i][j] += 1
        else:
            dp[i][j] += sum(dp[i - x][x] for x in range(1, j + 1))
while True:
    try:
        n = int(input())
        print(dp[n][n])
    except:
        break

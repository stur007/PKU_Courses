t,m = [int(x) for x in input().split()]
data = []
for _ in range(m):
    data.append([int(y) for y in input().split()])

dp = [0]*(t + 1)
for i in range(m):
    for j in range(t, data[i][0] - 1, -1):
        if j >= data[i][0]:
            dp[j] = max(dp[j], dp[j-data[i][0]] + data[i][1])
print(dp[-1])

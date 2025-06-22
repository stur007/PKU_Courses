n = int(input())
dp = [0]*(n+1)
if n == 1:
    print(1)
else:
    dp[1] = 1
    dp[2] = 2
    tot = 1
    for i in range(3, n+1):
        tot +=dp[i-1]
        dp[i] = tot+1
    print(dp[-1])
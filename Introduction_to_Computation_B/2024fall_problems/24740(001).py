n = int(input())
for _ in range(n):
    a, b = map(int,input().split())
    if b-a <= 2:
        print(1)
    else:
        dp = [0] *(b-a+2)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,b-a+2):
            dp[i] = dp[i-1]+dp[i-2]
        print(dp[-1])
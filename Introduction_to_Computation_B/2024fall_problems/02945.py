k = int(input())
s = list(map(int, input().split()))
dp = [1]*k ### 注意初值的设定
for i in range(k):
    for j in range(i):
        if s[j] >= s[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

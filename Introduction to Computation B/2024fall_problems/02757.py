n = int(input())
nums = [int(x) for x in input().split()]
dp = [1]*n

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[j]+1,dp[i])

print(max(dp))
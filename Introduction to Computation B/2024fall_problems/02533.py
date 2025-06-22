n = int(input())
s = list(map(int ,input().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if s[j] < s[i]:
            dp[i] =max(dp[i], dp[j] +1)
print(max(dp))
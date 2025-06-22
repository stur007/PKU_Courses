n, m = map(int, input().split())
dp = [0]+[float('inf')]*m
s = list(map(int, input().split()))
for i in range(n):
        for j in range(s[i-1], m+1):
                dp[j] = min(dp[j], dp[j-s[i-1]]+1)
if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])
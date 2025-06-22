n, a, b, c = map(int, (input().split()))
s = [a,b,c]
s.sort()
a = s[0]
b = s[1]
c = s[2]
dp = [0] *(n+1)
try:
    dp[a] = 1
    for i in range(a + 1, b + 1):
        dp[i] = dp[i - a] + (1 if dp[i - a] != 0 else 0)
    dp[b] = max(dp[b], 1)
    for i in range(b + 1, c + 1):
        dp[i] = max(dp[i - a] + (1 if dp[i - a] != 0 else 0), dp[i - b] + (1 if dp[i - b] != 0 else 0))
    dp[c] = max(dp[c], 1)
    for i in range(c + 1, n + 1):
        dp[i] = max(dp[i - a] + (1 if dp[i - a] != 0 else 0), dp[i - b] + (1 if dp[i - b] != 0 else 0),
                    dp[i - c] + (1 if dp[i - c] != 0 else 0))
    print(dp[-1])
except IndexError:
    print(dp[-1])

### 这道题目过于讨厌了，不停的考虑奇怪的情形
### 但是，参考一下解答，是不是复杂是自己的原因呢，其实，中间那些不可能的情形都可以赋值为负无穷！
"""
n, a, b, c = map(int, input().split())
dp = [0]+[float('-inf')]*n

for i in range(1, n+1):
    for j in (a, b, c):
        if i >= j:
            dp[i] = max(dp[i-j] + 1, dp[i])

print(dp[n])
"""

import heapq
n = int(input())
s = list(map(int, input().split()))
dp = [0] *(n+1)
ans = 0
q = []
for i in range(1,n+1):
    heapq.heappush(q, s[i-1])
    dp[i] = dp[i - 1] + s[i - 1]
    if dp[i]>=0:
        ans += 1
    else:
        worst_potion = heapq.heappop(q)
        dp[i] -= worst_potion
print(ans)
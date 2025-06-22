t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    m = [float('-inf')]+list(map(int, input().split()))
    p = [0]+list(map(int, input().split()))
    dp = [0]*(n+1)
    for i in range(1, n+1):
        for j in range(0, i):
            if m[i]-m[j]>k:
                dp[i] = max(dp[i-1], dp[j] +p[i])

    print(dp[-1])
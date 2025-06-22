from bisect import bisect_left
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    pairs = []
    for i in range(n):
        pairs.append((s[2*i], s[2*i+1]))
    pairs.sort(reverse = True)
    dp = [pairs[0][1]]
    for p in pairs:
        idx = bisect_left(dp, p[1])
        if idx == len(dp):
            dp.append(p[1])
        else:
            dp[idx] = p[1]
    print(len(dp))
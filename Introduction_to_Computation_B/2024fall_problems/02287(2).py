while True:
    n = int(input())
    if n == 0:
        break

    t = list(map(int, input().split()))
    k = list(map(int, input().split()))
    t.sort()
    k.sort()

    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if t[i-1] > k[j-1]:
                s = 400
            elif t[i-1] == k[j-1]:
                s = 200
            else:
                s = 0
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+s)

    print(dp[-1][-1]-200*n)
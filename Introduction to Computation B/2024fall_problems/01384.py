t = int(input())
for _ in range(t):
    e, f =map(int, input().split())
    w = f-e
    n = int(input())
    s = []
    for _ in range(n):
        s.append(list(map(int, input().split())))
    dp = [0]+[float('inf')]*w
    for i in range(n):
        for j in range(s[i][1], w+1):
            dp[j] = min(dp[j], dp[j-s[i][1]]+s[i][0])
    if dp[-1] == float('inf'):
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {dp[-1]}.')
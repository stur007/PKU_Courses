n, m = map(int, input().split())
s = list(map(int, input().split()))
s.reverse()
dp = [1]
temp = {s[0]}
for i in range(1,n):
    if not s[i] in temp:
        temp.add(s[i])
        dp.append(dp[-1]+1)
    else:
        dp.append(dp[-1])
dp.reverse()
for _ in range(m):
    l = int(input())
    print(dp[l-1])
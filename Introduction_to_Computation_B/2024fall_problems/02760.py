n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
dp = [0, s[0][0], 0]
for i in range(1,n):
    temp = [0] * (i+3)
    for j in range(1, i+2):
        temp[j] = max(dp[j-1]+s[i][j-1], dp[j]+s[i][j-1])
    dp = temp[:]
print(max(dp))
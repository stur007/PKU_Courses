s = list(map(int, input().split(',')))
n = len(s)
dp1 = [-float('inf')]*(n+1)
dp2 = [-float('inf')]*(n+1)
for i in range(1,n+1):
    dp1[i] = max(dp1[i-1]+s[i-1], s[i-1])
    dp2[i] = max(dp1[i-1], dp2[i-1]+s[i-1], dp1[i])
print(max(dp2))
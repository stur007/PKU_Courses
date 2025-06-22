from functools import cmp_to_key
def cmp_max(a, b):
    if a+b > b+a:
        return -1
    elif a+b < b+a:
        return 1
    else:
        return 0
m = int(input())
n = int(input())
a = list(input().split())
a.sort(key = cmp_to_key(cmp_max))
s = []
for i in range(len(a)):
    s.append(int(a[i]))
#print(s)
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if i>=len(str(s[j-1])):
            dp[i][j] = max(dp[i][j-1], int(str(dp[i-len(str(s[j-1]))][j-1])+str(s[j-1])))
        else:
            dp[i][j] = dp[i][j-1]
print(dp[-1][-1])

### 只能说不是很好想到怎么处理，dp部分比较简单，但是greedy部分还是不好想，需要琢磨一下
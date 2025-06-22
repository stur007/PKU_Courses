n = int(input())
m = int(input())
s = list(map(int, input().split()))
for _ in range(m):
    for i in range(n-2, -1,-1):
        if s[i]<s[i+1]:
            minv = s[i]
            break
    for j in range(n-1,i, -1):
        if s[j] >minv:
            maxv = s[j]
            break
    s[j],s[i] = minv, maxv
    buffer = s[i+1:]
    buffer.reverse()
    s = s[:i+1]+buffer
print(*s)

### 这个贪心策略还是比较容易想到的
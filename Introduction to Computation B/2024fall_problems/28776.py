n = int(input())
a, b = map(int, input().split())
s = []
for _ in range(n):
    x, y = (map(int, input().split()))
    s.append((x*y, x, y))
s.sort()
pre = a
maxv = 0
for i in range(n):
    maxv = max(maxv, pre//s[i][2])
    pre *= s[i][1]
print(maxv)
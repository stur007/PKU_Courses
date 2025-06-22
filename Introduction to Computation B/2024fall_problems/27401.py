from bisect import bisect_left
from copy import deepcopy

n, t = map(int, input().split())
p = list(map(int, input().split()))
r = set()
r.add(0)
for i in range(n):
    temp = deepcopy(r)
    for k in r:
        temp.add(k+p[i])
    r = deepcopy(temp)
s = list(r)
s.sort()
i = bisect_left(s, t)
if i == len(s):
    print(0)
else:
    print(s[i])
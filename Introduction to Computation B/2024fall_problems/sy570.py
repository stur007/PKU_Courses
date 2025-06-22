from collections import defaultdict
data = defaultdict(set)
n, q =map(int, input().split())
flag = 0
for _ in range(q):
    x, y = map(int,input().split())
    data[x].add(y)
    for k in range(1,n+1):
        if (k in data[y]) and (x in data[k]):
            flag = 1
            break
if flag:
    print('Yes')
else:
    print('No')

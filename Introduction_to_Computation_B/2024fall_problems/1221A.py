q = int(input())
for _ in range(q):
    n = int(input())
    s = list(map(int, input().split()))
    collect = []
    for i in s:
        if i <= 2048:
            collect.append(i)
    if sum(collect) >= 2048:
        print('yes')
    else:
        print('no')
# 感觉思路不是很好想，发现只要加起来就行
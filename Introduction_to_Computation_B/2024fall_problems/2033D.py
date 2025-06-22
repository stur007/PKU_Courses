t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prefix = {0}
    temp = 0
    cnt = 0
    for i in range(n):
        temp += a[i]
        if temp in prefix:
            cnt += 1
            temp = 0
            prefix = {0}
        else:
            prefix.add(temp)
    ans.append(cnt)
print(*ans, sep='\n')
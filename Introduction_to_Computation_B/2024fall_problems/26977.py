n = int(input())
s = list(map(int, input().split()))
i = 0
temp = []
ans = 0
while True:
    if s[0] == 0:
        s.pop(0)
    else:
        n = len(s)
        break
while True:
    if i >= n:
        break
    temp.append(s[i])
    if len(temp) > 2 and temp[-2] >= temp[-1] and temp[-2] >= temp[-3]:
        temp.pop()
        height = min(temp[0], temp[-1])
        temp.pop(0)
        temp.pop()
        for k in temp:
            ans += height-k
        temp = [s[i-1], s[i]]
        i += 1
    elif i == n-1 and len(temp) > 2:
        height = min(temp[0], temp[-1])
        temp.pop(0)
        temp.pop()
        for k in temp:
            ans += height - k
        temp = [s[i - 1], s[i]]
        i += 1
    else:
        i += 1
print(ans)
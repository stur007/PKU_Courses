n, m = map(int, input().split())
s= []
for _ in range(n):
    s.append(list(map(int, input().split())))
s.sort()
s.append((m, 0))
cnt = 0
temp = 0
i = 0
while i < n:
    if max(temp+s[i][1], s[i][0]+1) <= s[i+1][0]:
        temp = max(temp+s[i][1], s[i][0]+1)
        cnt += 1
        i += 1
    else:
        if max(temp+s[i][1], s[i][0]+1) < max(temp+s[i+1][1], s[i+1][0]+1):
            temp = max(temp+s[i][1], s[i][0]+1)
            cnt += 1
            i += 2
        else:
            temp = max(temp+s[i+1][1], s[i+1][0]+1)
            cnt += 1
            i += 2
print(cnt)
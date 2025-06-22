k = int(input())
for _ in range(k):
    n = int(input())
    s = []
    for _ in range(n):
        s.append(tuple(map(int, input().split())))
    s.sort()
    cnt = 1
    time = [s[0][0], s[0][1]]
    for i in range(n):
        if time[0] <= s[i][1] and time[1] >= s[i][0]:
            time = [max(time[0],s[i][0]), min(time[1], s[i][1])]
        else:
            time = [s[i][0], s[i][1]]
            cnt += 1
    print(cnt)

### 代码简单，但是第一次没想到怎么设置贪心的方案。
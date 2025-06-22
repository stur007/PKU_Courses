while True:
    r, n = map(int, input().split())
    if r == -1 and n == -1:
        break
    s = list(map(int, input().split()))
    s.sort()
    cnt = 1
    x = [s[0],s[0]]
    for i in range(1,n):
        if s[i] - x[0] <= r:
            if s[i] - x[1] <= r:
                x[0] = s[i]
        else:
            cnt += 1
            x = [s[i],s[i]]
    print(cnt)
### 两周之前做这道题目还是非常困难的，现在就非常清楚了！
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int ,input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append((a[i],b[i]))
    c.sort(reverse = True)
    time = 0
    i = 0
    while True:
        if c[i][0] > c[i][1] + time:
            time += c[i][1]
            i += 1
        else:
            print(max(time,c[i][0]))
            break
        if i ==n:
            print(time)
            break
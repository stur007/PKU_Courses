m = int(input())
for _ in range(m):
    n, k =map(int, input().split())
    s = list(map(int, input().split()))
    for _ in range(k):
        if s == [i for i in range(n,0,-1)]:
            s = [i for i in range(1,n+1)]
            continue
        for i in range(n - 2, -1, -1):
            if s[i] < s[i + 1]:
                minv = s[i]
                break ###之前第一次做的时候丢失了break，然后半天没有想出来是为啥错
        for j in range(n - 1, i, -1):
            if s[j] > minv:
                maxv = s[j]
                break
        s[j], s[i] = minv, maxv
        buffer = s[i + 1:]
        buffer.reverse()
        s = s[:i + 1] + buffer
    print(*s)
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    s = [int(i)%x for i in input().split()]
    if sum(s) % x != 0:
        print(n)
    else:
        i = 0
        pre = 0
        j = n - 1
        suf = 0
        while True:
            pre += s[i]
            suf += s[j]
            pre = pre%x
            suf = suf%x
            i += 1
            j -= 1
            if pre != 0:
                print(n-i)
                break
            if suf != 0:
                print(j+1)
                break
            if i==n or j == -1:
                print(-1)
                break
# False = 0, True = 1 注意含义的使用
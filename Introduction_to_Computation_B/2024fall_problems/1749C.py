t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    flag = 1
    for k in range(1, n+2):
        test = a[:n-k+1]
        i = k
        while i > 1:
            if len(test) == 0:
                flag = 0
                break
            if test[0] <= i:
                test.pop(0)
                i -= 1
            else:
                test.pop(0)
        if len(test) == 0:
            flag = 0
        if len(test) > 0 and min(test) > 1:
            flag = 0
        if not flag:
            break
    print(k-1)
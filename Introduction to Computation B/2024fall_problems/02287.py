while True:
    n = int(input())
    if n == 0:
        break
    t = list(map(int, input().split()))
    k = list(map(int, input().split()))

    t.sort()
    k.sort()
    cnt = 0
    i = 0
    j = 0
    m = n-1
    l = n-1

    while True:
        if i > m or j > l:
            break
        if t[i] > k[j]:
            i += 1
            j += 1
            cnt += 1
        elif t[m] > k[l]:
            m -= 1
            l -= 1
            cnt += 1
        else:
            if t[i] < k[l]: ###排除平局的情况
                cnt -= 1

            i += 1
            l -= 1

    print(cnt*200)
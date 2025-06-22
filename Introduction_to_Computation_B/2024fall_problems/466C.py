n = int(input())
s = list(map(int, input().split()))
tot = sum(s)
if tot%3 != 0:
    print(0)
else:
    lst_pre = []
    lst_suf = []
    part = tot//3
    pre = 0
    suf = 0
    i = 0
    j = n-1
    cnt_pre = 0
    cnt_suf = 0
    while i < n:
        pre += s[i]
        if pre == part:
            cnt_pre = 1
        else:
            cnt_pre = 0
        lst_pre.append(cnt_pre)
        i += 1
    while j >= 0:
        suf += s[j]
        if suf == part:
            cnt_suf += 1
        lst_suf.append(cnt_suf)
        j -= 1
    ans = 0
    lst_suf.reverse()
    for k in range(n-2):
        if lst_pre[k] != 0:
            ans += lst_pre[k]*lst_suf[k+2]
    print(ans)
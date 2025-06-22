'''
while True:
    n = int(input())
    if n == 0:
        break
    key = list(map(int,input().split()))
    while True:
        s = input()
        if s == '0':
            break
        num = ''
        i = 0
        while i < len(s):
            if s[i] != ' ':
                num += s[i]
                i += 1
            else:
                break
        message = s[i+1:]
        k = int(num)
        ans_p = [' ']*n
        ans = [' ']*n
        for j in range(len(message)):
            ans_p[key[j]-1] = message[j]
        k -= 1

        while k > 0:
            k -= 1
            for a in range(len(ans_p)):
                if ans_p[a] != ' ':
                    ans[key[a]-1] = ans_p[a]
            ans_p = ans[:]
            ans = [' ']*n
        ans = ans_p
        print(*ans, sep = '')
'''

###这样做确实是正确的，但是会出现超时的情形
###下面是优化之后的结果：
'''while True:
    n = int(input())
    if n == 0:
        break
    key = list(map(int,input().split()))
    test_0 = [i for i in range(n)]
    test = [key[i]-1 for i in range(n)]
    test_c = 1
    while test != test_0:
        test = [key[test[i]]-1 for i in range(n)]
        test_c += 1
    while True:
        s = input()
        if s == '0':
            break
        num = ''
        i = 0
        while i < len(s):
            if s[i] != ' ':
                num += s[i]
                i += 1
            else:
                break
        message = list(s[i+1:])
        k = int(num)%test_c
        formal = [i for i in range(n)]
        while k > 0:
            formal = [key[formal[i]] - 1 for i in range(n)]
            k -= 1
        ans = [' ']*n
        for i in range(len(message)):
            ans[formal[i]] = message[i]
        print(*ans,sep = '')'''
### 这样写仍然是超时的，研究答案以后发现需要对每个点计算循环，而计算整体的循环节仍然会接近总长度的量级
while True:
    n = int(input())
    if n == 0:
        break
    key = list(map(int, input().split()))
    ref = [i for i in range(n)] ### 没有必要创建列表，直接枚举即可
    for i in range(n):
        ref[i] = key[ref[i]]-1
        cnt = 1
        while ref[i] != i:
            cnt += 1
            ref[i] = key[ref[i]]-1
        ref[i] = cnt
    while True:
        s = input()
        if s == '0':
            break
        num, message = s.split(' ',1)
        num = int(num)
        ans = [' ']*n
        for j in range(len(message)):
            num_j = num%ref[j]
            k = j
            for _ in range(num_j):
                k = key[k]-1
            ans[k] = message[j]
        print(*ans, sep = '')
    print()
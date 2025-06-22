n, k = map(int,input().split())
ref = ['A', 'B', 'C', 'D', 'E', 'F']
ans = []
if n == 0:
    print(0)
else:
    while n > 0:
        n, s = divmod(n, k)
        if s >= 10:
            s = ref[s-10]
        ans.append(s)
    ans.reverse()
    print(*ans, sep = '')
    ### 小心n==0 的情形！！
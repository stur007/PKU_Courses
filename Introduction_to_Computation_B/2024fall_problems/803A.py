n, k = map(int, input().split())
if k > n**2:
    print(-1)
else:
    ans = [[0]*n for _ in range(n)]
    for i in range(n):
        if k >= 2*(n-i)-1:
            k -=2*(n-i)-1
            for j in range(i,n):
                ans[i][j] = 1
                ans[j][i] = 1
        elif k > 0:
            for j in range(i,(k-1)//2+i+1):
                ans[i][j] = 1
                ans[j][i] = 1
            k -= 1+2*((k-1)//2)
            if k:
                ans[i+1][i+1] =1
                k -= 1
        else:
            break
    for i in ans:
        print(*i)

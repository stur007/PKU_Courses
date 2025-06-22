t = int(input())
for _ in range(t):
    n = int(input())
    jails = [0]*n
    for i in range(1,n+1):
        for j in range(n):
           if (j+1) % i == 0:
               if jails[j] == 0:
                   jails[j] = 1
               else:
                   jails[j] = 0
    print(sum(jails))

    ###代码简化：s[i] ^= 1 直接实现元素在0和1之间的转化
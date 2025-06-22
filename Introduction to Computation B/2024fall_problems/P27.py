t = int(input())
for i in range(t):
    n,k=[int(x) for x in input().split()]
    a=[int(y) for y in input().split()]
    c=[]
    for j in range(n):
        c.append((a[j],j))
    c.sort()
    b=[int(z) for z in input().split()]
    b.sort()
    d=[0]*n
    for k in range(n):
        d[c[k][1]]=b[k]
    print(*d,sep=' ')


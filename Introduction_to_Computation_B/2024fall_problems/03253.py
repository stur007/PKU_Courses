while True:
    n,p,m=[int(x) for x in input().split()]
    if n == 0 and p == 0 and m == 0:
        break
    children = [i for i in range(1,n+1)]
    ans = []
    for a in range(p-1):
        children.append(children.pop(0))
    while len(children) > 1:
        for b in range(m-1):
            children.append(children.pop(0))
        ans.append(children.pop(0))
    ans.append(children.pop(0))
    print(*ans,sep=',')
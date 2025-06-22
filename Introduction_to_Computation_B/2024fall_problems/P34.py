m = int(input())
test = []
for _ in range(m):
    a,b,c,d = [int(x) for x in input().split()]
    mark = False
    for i in [a,-a]:
        for j in [b,-b]:
            for k in [c, -c]:
                for l in [d,-d]:
                    if i + j + k + l == 24:
                        mark = True
    print('YES' if mark else 'NO')
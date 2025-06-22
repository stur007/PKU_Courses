m, n, p, q = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(m)]
cor = [list(map(int, input().split())) for _ in range(p)]
ans = []
for i in range(m+1-p):
    line = []
    for j in range(n+1-q):
        element = 0
        for k in range(p):
            element_line = 0
            for l in range(q):
                element_line += cor[k][l]*mat[k+i][l+j]
            element += element_line
        line.append(element)
    ans.append(line)

for _ in range(m+1-p):
    print(*ans[_])
m, n = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]
maxv = 0
for i in range(m):
    for j in range(n):
        if s[i][j] == 0:
            maxn = n
            for k in range(i, m):
                for l in range(j, maxn):
                    if s[k][l] == 0:
                        maxv = max(maxv, (k-i+1)*(l-j+1))
                    else:
                        maxn = l
                        break
print(maxv)

### 关注行号和列号！
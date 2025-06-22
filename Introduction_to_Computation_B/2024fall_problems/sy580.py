n, m = map(int, input().split())
ans = 0
matrix = [list(input().split()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        abcd = int(matrix[0][j]+matrix[i][m-1]+matrix[n-1][j]+matrix[i][0])
        ans = max(int(matrix[i][j]) * abcd, ans)
print(ans)
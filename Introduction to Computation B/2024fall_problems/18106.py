n = int(input())
matrix = [[0]*n for _ in range(n)]
temp = 0
i, j = 0, -1
step = [(0, 1), (1, 0), (0, -1), (-1, 0)]

flag = 0

while True:
    temp += 1
    ref = [j + 1 <= n - 1 and matrix[i][j + 1] == 0, i + 1 <= n - 1 and matrix[i + 1][j] == 0,
           j - 1 >= 0 and matrix[i][j - 1] == 0, i - 1 >= 0 and matrix[i - 1][j] == 0]

    if ref[flag]:
        di, dj = step[flag]
        i = i+di
        j = j+dj
        matrix[i][j] = temp

    else:
        for k in range(4):
            if ref[k]:
                di, dj = step[k]
                i = i + di
                j = j + dj
                matrix[i][j] = temp
                flag = k

        ### 可以简化，已经想到按照顺序判断了，可以直接+= 1 然后计算

    if temp == n**2:
        break

for i in range(n):
    print(*matrix[i])
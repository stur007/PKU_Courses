n, m, k = [int(x) for x in input().split()]
matrix = [[0] * m for _ in range(n)]
ans = 0
mark = 0

for _ in range(k):
    i, j = [int(y) - 1 for y in input().split()]  # 将输入转换为0索引
    if matrix[i][j] == 0:  # 如果这个位置还没有被涂黑
        ans += 1
        matrix[i][j] = 1

        # 检查是否形成了2x2的黑色方块
        try:
            if (i > 0 and j > 0 and matrix[i - 1][j] == 1 and matrix[i][j - 1] == 1 and matrix[i - 1][j - 1] == 1 or
                    i < n - 1 and j > 0 and matrix[i + 1][j] == 1 and matrix[i][j - 1] == 1 and matrix[i + 1][j - 1] == 1 or
                    i > 0 and j < m - 1 and matrix[i - 1][j] == 1 and matrix[i][j + 1] == 1 and matrix[i - 1][j + 1] == 1 or
                    i < n - 1 and j < m - 1 and matrix[i + 1][j] == 1 and matrix[i][j + 1] == 1 and matrix[i + 1][j + 1] == 1):
                mark = 1
                print(ans)
                break
        except IndexError:
            pass
    else:
        ans+=1

if mark == 0:
    print(0)
n, m = map(int, input().split())

# 构建带边框的岛屿矩阵
island = [[0] * (m + 2)]  # 上边框
for _ in range(n):
    s = [0] + [int(x) for x in input().split()] + [0]  # 在每行的开头和结尾插入0
    island.append(s)
island.append([0] * (m + 2))  # 下边框

circle = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if island[i][j] == 1:
            circle += 4
            if island[i+1][j] ==1:
                circle -= 1
            if island[i-1][j] == 1:
                circle -= 1
            if island[i][j-1] == 1:
                circle -= 1
            if island[i][j+1] == 1:
                circle -= 1
print(circle)
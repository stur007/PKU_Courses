L,M=[int(x) for x in input().split()]
line=[1]*(L+1)
for _ in range(M):
    a,b=[int(x) for x in input().split()]
    line[a:b+1]=[0]*(b-a+1)
print(sum(line))


def count_remaining_trees(L, M, regions):
    # 创建一个长度为 L+1 的数组来标记树的状态
    trees = [False] * (L + 1)

    # 遍历每个区域
    for start, end in regions:
        # 确保 start <= end
        if start > end:
            start, end = end, start
        # 标记区域内的树
        for i in range(start, end + 1):
            trees[i] = True

    # 计算剩余的树的数量
    remaining_trees = sum(not removed for removed in trees)

    return remaining_trees


# 从输入中读取数据
import sys

input = sys.stdin.read
data = input().split()
L = int(data[0])
M = int(data[1])
regions = []

# 读取 M 个区域
index = 2
for _ in range(M):
    start = int(data[index])
    end = int(data[index + 1])
    regions.append((start, end))
    index += 2

# 计算剩余的树并输出结果
result = count_remaining_trees(L, M, regions)
print(result)

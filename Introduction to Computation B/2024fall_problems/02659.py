a, b, k = map(int, input().split())
data = []
for _ in range(k):
    r, s, p, t = map(int, input().split())
    data.append((r-1, s-1, (p-1)//2, t))

possible = [[1] * b for _ in range(a)]

for r, s, p, t in data:
    if t == 1:
        for i in range(a):
            for j in range(b):
                if i < r - p or i > r + p or j < s - p or j > s + p:
                    possible[i][j] = 0
    else:
        for i in range(max(0, r - p), min(a, r + p + 1)):
            for j in range(max(0, s - p), min(b, s + p + 1)):
                possible[i][j] = 0

ans = sum(sum(row) for row in possible)
print(ans)

# wrong answer 也有可能是数组越界的问题，比如数据集中仅仅出现了-1, -2 之类的代码
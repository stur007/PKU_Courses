n, W = map(int, input().split())
candies = []

# 收集糖果
for _ in range(n):
    v, w = map(int, input().split())
    candies.extend([v / w] * w)  # 记录糖果的单位价值

# 初始化dp数组
dp = [[0] * (W + 1) for _ in range(len(candies) + 1)]

# 填充dp数组
for i in range(1, len(candies) + 1):
    for w in range(1, W + 1):
        dp[i][w] = max(dp[i - 1][w], dp[i][w - 1] + float(candies[i - 1]))

# 输出结果
print(f"{dp[-1][-1]:.1f}")

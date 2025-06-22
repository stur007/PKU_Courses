from collections import Counter

int(input())
s = list(map(int, input().split()))
count = Counter(s)
num = sorted(count.keys())
n = len(num)
dp = [[0, 0] for _ in range(n)]
dp[0] = [0, num[0]*count[num[0]]]
for i in range(1, n):
    if num[i] - num[i-1] > 1:
        dp[i][0] = max(dp[i-1])
        dp[i][1] = max(dp[i-1])+count[num[i]]*num[i]
    else:
        dp[i][0] = max(dp[i-1])
        dp[i][1] = dp[i-1][0]+count[num[i]]*num[i]

print(max(dp[-1]))

### gpt,但是优化不大
"""
from collections import Counter

# 输入数据
int(input())  # 不需要存储该值
s = list(map(int, input().split()))

# 统计每个数字出现的次数并排序
count = Counter(s)
num = sorted(count.keys())

# 初始化动态规划变量
prev_not_take, prev_take = 0, count[num[0]] * num[0]

# 动态规划过程
for i in range(1, len(num)):
    if num[i] - num[i - 1] == 1:
        # 相邻情况下：当前数选，依赖于前一个不选的状态
        curr_take = prev_not_take + count[num[i]] * num[i]
    else:
        # 不相邻情况下：当前数选，依赖于前一个的最大状态
        curr_take = max(prev_not_take, prev_take) + count[num[i]] * num[i]
    
    # 当前数不选，取前一个的最大值
    curr_not_take = max(prev_not_take, prev_take)

    # 更新状态
    prev_not_take, prev_take = curr_not_take, curr_take

# 输出结果
print(max(prev_not_take, prev_take))

"""
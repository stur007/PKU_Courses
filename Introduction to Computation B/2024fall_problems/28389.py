from bisect import bisect_right
n = int(input())
s = list(map(int, input().split()))
dp = []
for i in s:
    idx = bisect_right(dp, i)
    if idx == 0:
        dp = [i] + dp
    else:
        dp[idx-1] = i
print(len(dp))

### 非常棒！学会了使用二分查找维护动态规划的问题，很有进步！

"""
原来的解法：
n = int(input())
s = list(map(int, input().split()))
dp = [0]
for i in s:
    flag = 0
    for j in range(len(dp)):
        if dp[j] <= i:
            dp[j] = i
            flag = 1
            break
    if flag == 0:
        dp.append(i)
print(len(dp))
用时2381ms
"""
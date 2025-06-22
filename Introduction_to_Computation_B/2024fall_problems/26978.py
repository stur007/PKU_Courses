import heapq
n, k = map(int, input().split())
nums= list(map(int, input().split()))
temp = []
ans = []
for i in range(k):
    heapq.heappush(temp, (-nums[i], i))
ans.append(-temp[0][0])
for i in range(1, n-k+1):
    while temp[0][1] < i:
        heapq.heappop(temp)
    heapq.heappush(temp, (-nums[i+k-1], i+k-1))
    ans.append(-temp[0][0])
print(*ans, sep = ' ')

# 发现会用heapq以后就是快！
# 答案用了单调队列，感觉和我的做法差别不大，也许更好的模拟了heap的功能？
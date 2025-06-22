"""n = int(input())
s = list(map(int, input().split()))
s.sort(reverse=True)
l = sum(s)
ans = 0
for i in range(n-1):
    ans += l
    l -= s[i]
print(ans)"""
# 其实基本思路正确，但是注意剪绳子要时刻判断最优解

from heapq import heappush, heappop

n = int(input())
s = list(map(int, input().split()))
ref = []
for i in s:
    heappush(ref, i)

ans = 0
while len(ref) > 1:
    a = heappop(ref)
    b = heappop(ref)
    temp = a+b
    ans += temp
    heappush(ref, temp)

print(ans)

#这一算法好像有一个名字叫Huffman树
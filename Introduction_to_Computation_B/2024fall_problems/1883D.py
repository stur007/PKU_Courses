import heapq
from collections import defaultdict

left = defaultdict(int)
right= defaultdict(int)
left_list = []
right_list = []

q = int(input())
for _ in range(q):
    s = list(input().split())
    l = int(s[1])
    r = int(s[2])
    if s[0] == '+':
        if left[l] == 0:
           heapq.heappush(left_list, -l)
        left[l] += 1
        if right[r] == 0:
            heapq.heappush(right_list, r)
        right[r] += 1
    else:
        left[l] -= 1
        right[r] -= 1

    while left_list and left[-left_list[0]] == 0:
        heapq.heappop(left_list)
    while right_list and right[right_list[0]] == 0:
        heapq.heappop(right_list)

    if left_list and right_list and -left_list[0] > right_list[0]:
            print('yes')
    else:
            print('no')

# I think this problem could be an excellent quiz. First, you should try to figure out the greedy way to help determine
# your data structure. Second, you have to notice the extra time needed for sorting (heapq.heapify() is O(n)). So you
# have to use the 'lazy deletion' trick to help you overcome this difficulty.
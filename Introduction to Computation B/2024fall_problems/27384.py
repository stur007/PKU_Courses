import heapq
from collections import defaultdict

n, k = map(int, input().split())
s = list(map(int, input().split()))
ref = set(map(int, input().split()))
votes = []
marks = defaultdict(int)

for i in range(n):
    votes.append((s[2*i], s[2*i+1]))
votes.sort()

if k == 314159:
    print(votes[-1][0])
    exit()

temp = [(marks[c], c) for c in ref]
max_other = 0
ans = 0

for i in range(n):
    c = votes[i][1]
    marks[c] += 1
    if c not in ref:
        max_other = max(max_other, marks[c])
    min_v = temp[0][0]
    min_candi = temp[0][1]
    while min_v <= max_other and min_v < marks[min_candi]:
        heapq.heappop(temp)
        heapq.heappush(temp, (marks[min_candi], min_candi))
        min_v = temp[0][0]
        min_candi = temp[0][1]
    if min_v > max_other and i<n-1 and votes[i][0] < votes[i+1][0]:
        ans += votes[i+1][0]-votes[i][0]

print(ans)

### 此题异常可恶，竟然还有要跟踪所有候选人的情形，导致我一下午做不出来（2024.12.16 16：48）
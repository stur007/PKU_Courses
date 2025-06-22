n = int(input())
a = list(map(int, input().split()))
inters = []
for i in range(n):
    inters.append((i-a[i], i+a[i]))
inters.sort()
visited_idx = 0
start = 0
end = 0
cnt = 0

while True:
    temp = 0
    for i in range(visited_idx, n):
        if inters[i][0] <= start:
            end = max(end, inters[i][1]+1)
            temp += 1
        else:
            break
    visited_idx += temp
    start = end
    cnt += 1
    if end >= n:
        break

print(cnt)

### 区间问题，注意优化
n, m = map(int, input().split())
s = list(tuple(map(int, input().split())) for _ in range(n))
intervals = []

for i in range(n):
    xi = s[i][0]
    yi = s[i][1]
    for x in range(max(xi-yi+1, 0), min(xi+1, m-yi+1)):
        intervals.append((x, x+yi))

cnt = 0
intervals.sort(key = lambda x:x[1])
temp = -1
for i in range(len(intervals)):
    if intervals[i][0] >= temp:
        cnt += 1
        temp = intervals[i][1]

print(cnt)

# In fact, it is not an difficult problem, what you need to do is try to figure out all the possible choices
# to help you get it over. (brute force)
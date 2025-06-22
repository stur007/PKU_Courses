n, c = map(int, input().split())
x = []
for _ in range(n):
    x.append(int(input()))
x.sort()

def ok(a):
    cnt = 1
    i = 0
    temp = x[0]
    while i < n:
        if x[i] - temp >= a:
            cnt += 1
            temp = x[i]
        i += 1
    return cnt >= c

def bisect(left, right):
    if right == left:
        return left
    if right - left == 1:
        if ok(right):
            return right
        else:
            return left
    mid = (left + right) // 2
    if ok(mid):
        return bisect(mid, right)
    else:
        return bisect(left, mid)

minv = 1
maxv = x[-1] - x[0]
ans = bisect(minv, maxv)
print(ans)

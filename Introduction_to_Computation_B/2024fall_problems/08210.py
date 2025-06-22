l, n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(int(input()))

def test(a):
    start = 0
    cnt = 0
    for i in range(n):
        if s[i]-start>=a:
            start = s[i]
        else:
            cnt += 1
    if l-start < a:
        cnt += 1
    return cnt <= m

def find():
    left = 1
    right = l//(n-m+1)
    while True:
        if right == left:
            return left
        if right - left == 1:
            if test(right):
                return right
            else:
                return left
        mid = (left + right) // 2
        if test(mid):
            left = mid
        else:
            right = mid
print(find())

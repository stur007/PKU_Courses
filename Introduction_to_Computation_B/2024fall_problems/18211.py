p = int(input())
s = list(map(int, input().split()))
s.sort()

my = 0
other = 0

while my >= other and s:
    if p >= s[0]:
        p -= s[0]
        my += 1
        s.pop(0)
    elif len(s) > 1 and my - other >= 1:  ###注意取等条件！！！不要在边界条件上出错
        p = p + s[-1] - s[0]
        other += 1
        my += 1
        s.pop(0)
        s.pop(-1)
    else:
        break

print(my - other)

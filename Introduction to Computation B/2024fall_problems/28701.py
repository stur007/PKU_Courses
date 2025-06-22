n, k = map(int,(input().split()))
s = list(map(int, input().split()))
s.sort()
total = sum(s)
max_time = sum(s)/k
if s[-1]>max_time:
    for i in range(n-1, -1, -1):
        if s[i] <= max_time:
            break
        k -= 1
        total -= s[i]
        max_time = total/k
print('%.3f' % max_time)
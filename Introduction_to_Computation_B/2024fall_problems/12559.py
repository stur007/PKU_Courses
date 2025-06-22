from functools import cmp_to_key
def cmp_max(a, b):
    if a+b > b+a:
        return -1
    elif a+b < b+a:
        return 1
    else:
        return 0
n = int(input())
s = list(input().split())
s.sort(key = cmp_to_key(cmp_max))
max_v = ''.join(s)
s.reverse()
min_v = ''.join(s)
print(max_v, min_v)
from functools import cmp_to_key

n, d = map(int, input().split())
s = [int(input()) for _ in range(n)]

def compare(a, b):
    if a < b:
        return -1  # a 小于 b，按升序排列
    elif a > b and a - b <= d:
        return 0   # a 和 b 的差小于等于 d，视为等价
    else:
        return 1   # 其他情况保持原顺序

s.sort(key=cmp_to_key(compare))
print(*s, sep='\n')
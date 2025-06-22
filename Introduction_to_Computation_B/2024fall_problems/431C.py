from functools import lru_cache
import sys
sys.setrecursionlimit(1<<30)

n, k, d = map(int, input().split())
m = 10**9+7

@lru_cache(maxsize=None)
def f(n, flag):
    if n == flag == 0:
        return 1
    if flag == 0:
        return sum(f(n-i, 0) for i in range(1, min(d-1, n)+1))%m
    else:
        return sum(f(n-i ,1) for i in range(1, min(d-1, n)+1))%m+sum(f(n-i, 0)+f(n-i, 1) for i in range(d, min(n, k)+1))%m
print(f(n, 1)%m)
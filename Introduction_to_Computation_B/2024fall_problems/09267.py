import sys
from functools import lru_cache
sys.setrecursionlimit(1<<30)

n, m = map(int, input().split())

@lru_cache(maxsize=None)
def f(n ,s):
    if n-s <= 1:
        return 1
    return sum(f(n-s-1, i) for i in range(min(n-s, m)))
print(sum(f(n, i) for i in range(min(n+1, m))))
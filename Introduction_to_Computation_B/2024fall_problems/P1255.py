import sys
from functools import lru_cache
sys.setrecursionlimit(1<<30)
n = int(input())
@lru_cache(maxsize=None)
def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return f(n-1)+f(n-2)
print(f(n))
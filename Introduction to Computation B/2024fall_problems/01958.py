import sys
from functools import lru_cache

sys.setrecursionlimit(1<<30)
@lru_cache(maxsize = None)
def f(n):
    if n == 0:
        return 0
    else:
        return min(f(n-k)+ 2**k -1 +f(n-k) for k in range(1, n+1))

for n in range(1, 13):
    print(f(n))

"""print('1\n3\n5\n9\n13\n17\n25\n33\n41\n49\n65\n81')"""
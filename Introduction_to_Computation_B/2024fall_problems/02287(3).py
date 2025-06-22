from functools import lru_cache
import sys
sys.setrecursionlimit(1<<30)
@lru_cache(maxsize=4096)
def dfs(i, j):
    if i == 0 or j == 0:
        return 0

    if t[i-1] > k[j-1]:
        s = 400
    elif t[i-1] == k[j-1]:
        s = 200
    else:
        s = 0
    return max(dfs(i-1, j), dfs(i, j-1), dfs(i-1, j-1)+s)
while True:
    n = int(input())
    if n == 0:
        break
    t = list(map(int, input().split()))
    k = list(map(int, input().split()))
    print(dfs(n, n)-200*n)
def dfs(a, b, step):
    if a//b >= 2 or a == b:
        return step
    else:
        return dfs(b, a-b, (step+1)%2)

while True:
    x, y = map(int, input().split())
    if x == y == 0:
        break
    a = max(x, y)
    b = min(x, y)
    ans = dfs(a, b, 0)
    if ans == 0:
        print('win')
    else:
        print('lose')
n = int(input())
cnt = 0
ans = []
def f(n, x, y, z):
    global cnt
    if n == 1:
        ans.append(f'{x}->{z}')
        cnt += 1
    else:
        f(n-1, x, z, y)
        ans.append(f'{x}->{z}')
        cnt += 1
        f(n-1, y, x, z)

f(n, 'A', 'B', 'C')
print(cnt)
print(*ans, sep = '\n')
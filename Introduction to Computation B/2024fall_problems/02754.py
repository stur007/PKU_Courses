def f(buffer, idx, ans):
    if idx == 8:
        ans.append(buffer[:])
        return
    for i in range(1,9):
          if all(buffer[k] != i and abs(idx-k) != abs(i-buffer[k]) for k in range(len(buffer))):
              buffer.append(i)
              f(buffer, idx+1, ans)
              buffer.pop()
ans = []
idx = 0
buffer = []
f(buffer, idx, ans)
n = int(input())
for _ in range(n):
    s = int(input())
    print(*ans[s-1], sep = '')
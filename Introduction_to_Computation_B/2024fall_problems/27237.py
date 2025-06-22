from collections import deque

def bfs(n, m, ans):
    q = deque([(0, n, '')])
    in_queue = {n}
    max_step = float('inf')
    while q:
        step, x, path = q.popleft()
        if step+1 <= max_step:
            if 3*x == m:
                max_step = step+1
                ans.append(path+'H')
                break
            if x//2 == m:
                max_step = step+1
                ans.append(path+'O')
                break
            if 3*x not in in_queue:
                in_queue.add(3*x)
                q.append((step+1, 3*x, path+'H'))
            if x//2 not in in_queue:
                in_queue.add(x//2)
                q.append((step+1, x//2, path+'O'))
        else:
            break
    print(len(ans[0]))
    print(*ans)

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    bfs(n, m, [])
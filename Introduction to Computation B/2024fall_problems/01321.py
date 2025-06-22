def dfs(idx, temp, n, k, maze):
    global cnt

    if idx == n:
        if len(temp) == k:
            cnt += 1
        return

    dfs(idx+1, temp, n, k, maze)

    for i in range(n):
        if maze[idx][i] == '#' and i not in temp:
            temp.append(i)
            dfs(idx+1, temp, n, k, maze)
            temp.pop()

while True:
    n, k = map(int, input().split())
    if n == k == -1:
        break
    maze = []
    for _ in range(n):
        maze.append(input())
    cnt = 0

    dfs(0, [], n, k, maze)
    print(cnt)
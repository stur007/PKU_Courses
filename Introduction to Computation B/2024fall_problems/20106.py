import heapq

def scope(x, y):
    return 0<=x<m and 0<=y<n

def dijkstra():
    while q:
        od, x, y = heapq.heappop(q)
        for dx, dy in [(0,1), (0, -1), (1,0), (-1,0)]:
            nx = x+dx
            ny = y+dy
            if scope(nx, ny) and maze[nx][ny] != '#':
                d = abs(int(maze[x][y])-int(maze[nx][ny]))
                if distance[nx][ny] > od+d:
                    distance[nx][ny] = od+d
                    heapq.heappush(q, (od+d, nx, ny))

m, n, p = map(int, input().split())
maze = []
for _ in range(m):
    maze.append(list(input().split()))
for _ in range(p):
    a, b, c, d = map(int, input().split())
    if maze[a][b] == '#' or maze[c][d] == '#':
        print('NO')
    else:
        distance = [[float('inf')] * n for _ in range(m)]
        distance[a][b] = 0
        q = [(0, a, b)]
        dijkstra()
        if distance[c][d] == float('inf'):
            print('NO')
        else:
            print(distance[c][d])
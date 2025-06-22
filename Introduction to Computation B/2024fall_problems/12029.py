from collections import deque
import sys
sys.setrecursionlimit(1<<30)
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    k = int(data[idx])
    idx += 1
    results = []
    for _ in range(k):
        m, n = map(int, data[idx:idx+2])
        idx += 2
        s = []
        for _ in range(m):
            s.append(list(map(int, data[idx:idx+n])))
            idx += n

        i, j = map(int, data[idx:idx+2])
        idx += 2
        i, j = i-1, j-1

        p = int(data[idx])
        idx += 1
        inQueue = [[False]*n for _ in range(m)]
        q = deque([])
        for _ in range(p):
            x, y = map(int, data[idx:idx+2])
            idx += 2
            x -= 1
            y -= 1
            inQueue[x][y] = True
            q.append((x, y))

        def scope(a, b):
            return  0<=a<m and 0<=b<n

        while q:
            l = len(q)
            for _ in range(l):
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nx = x+dx
                    ny = y+dy
                    if scope(nx, ny):
                        if s[nx][ny] < s[x][y]:
                            q.append((nx, ny))
                            s[nx][ny] = s[x][y]
                            inQueue[nx][ny] = True

        results.append('Yes' if inQueue[i][j] else 'No')
    sys.stdout.write('\n'.join(results)+'\n')
if __name__ == '__main__':
    main()
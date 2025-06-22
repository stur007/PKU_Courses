import sys
from copy import deepcopy

sys.setrecursionlimit(1<<30)

s = [list(map(int, input().split())) for _ in range(5)]

temp = []
ans = []

def dfs(idx):
    global ans, temp
    if idx == 6:
        ans.append(temp[:])
        return

    for i in [0, 1]:
        temp.append(i)
        dfs(idx+1)
        temp.pop()
dfs(0)

def scope(x, y):
    return 0<=x<5 and 0<=y<6

for actions in ans:
    test = deepcopy(s)
    for i in range(len(actions)):
        if actions[i] == 1:
            for dx, dy in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = dx, i+dy
                if scope(nx, ny):
                    test[nx][ny] = (test[nx][ny]+1)%2

    follow_actions = []
    for i in range(1, 5):
        temp = []
        for j in range(6):
            if test[i-1][j] == 1:
                temp.append(1)
                for dx, dy in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = i+dx, j+dy
                    if scope(nx, ny):
                        test[nx][ny] = (test[nx][ny] + 1) % 2
            else:
                temp.append(0)
        follow_actions.append(temp[:])

    if sum(test[-1]) == 0:
        print(*actions, sep = ' ')
        for i in range(4):
            print(*follow_actions[i], sep = ' ')
        break
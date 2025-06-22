from collections import defaultdict
m, n = map(int, input().split())
s = []
for _ in range(m):
    s.append(list(map(int, input().split())))

score = {}
marks = defaultdict(int)
for i in range(m*n):
    a = input()
    if not a:
        score[i] = (None, None, None)
        marks[0] += 1
    else:
        score[i] = tuple(map(int, a.split()))
        marks[sum(score[i])] += 1

def scope(x, y):
    return 0<=x <m and 0<=y<n

same = 0
for x in range(m):
    for y in range(n):
        temp = score[s[x][y]]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x+dx
            ny = y+dy
            if scope(nx, ny):
                if temp == score[s[nx][ny]]:
                    same += 1
                    break

answers = list(marks.keys())
answers.sort(reverse = True)
excellent = 0
for i in range(len(answers)):
    if excellent+marks[answers[i]] <= 0.4*m*n:
        excellent += marks[answers[i]]
    else:
        break

print(same, excellent)

### 题目不难。就是代码麻烦
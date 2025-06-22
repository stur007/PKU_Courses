"""import math

test = 1
while True:
    s = input()
    if len(s.strip()) == 0:
        test += 1
        continue
    n, d = map(int, s.split())
    if (n,d) == (0,0):
        break
    data = []
    for _ in range(n):
        data.append(tuple(map(int, input().split())))
    data.sort()
    cnt = 1
    try:
        current = math.sqrt(d**2-data[0][1]**2)+data[0][0]
    except ValueError:
        cnt = -1
        continue
    for i in range(n-1):
        if data[i][1] > d:
            cnt = -1
            break
        else:
            if math.sqrt((data[i][0]-current)**2+data[i][1]**2) > d:
                cnt += 1
                current = math.sqrt(d**2-data[i][1]**2)+data[i][0]
    print(f'Case {test}: {cnt}')"""

### 这是一开始的想法，后来发现确实不对，不是一维空间的情形（不是简单从左到右排序处理一下就行），不能简单处理，需要精致计算一下

"""import math

test = 1
while True:
    s = input()
    if len(s.strip()) == 0:
        test += 1
        continue
    n, d = map(int, s.split())
    if (n,d) == (0,0):
        break
    data = []
    for _ in range(n):
        data.append(tuple(map(int, input().split())))
    data.sort()
    cnt = 1
    try:
        current = math.sqrt(d**2-data[0][1]**2)+data[0][0]
    except ValueError:
        cnt = -1
        continue
    for i in range(n-1):
        if data[i][1] > d:
            cnt = -1
            break
        else:
            if data[i][0]-current > d:
                cnt += 1
                current = math.sqrt(d**2-data[i][1]**2)+data[i][0]
            elif 0<data[i][0]-current:
                if ((data[i][0]-current)**2+data[i][1]**2)>d**2:
                    cnt += 1
                    current = math.sqrt(d**2-data[i][1]**2)+data[i][0]
            else:
                if ((data[i][0] - current) ** 2 + data[i][1] ** 2) > d ** 2:
                    current = math.sqrt(d ** 2 - data[i][1] ** 2) + data[i][0]
    print(f'Case {test}: {cnt}')"""

### 然后参考了解答以后才知道和进程检测是一样的
import math
test = 1
while True:
    s = input()
    if len(s.lstrip()) == 0:
        test += 1
        continue
    n,d = map(int, s.split())
    if (n,d) == (0,0):
        break
    data = []
    cnt = 0
    for _ in range(n):
        x,y = map(int, input().split())
        if d >= y:
            a = x - math.sqrt(d**2-y**2)
            b = x + math.sqrt(d**2-y**2)
            data.append((a,b))
    if len(data) == n:
        data.sort()
        cnt = 1
        temp = data[0][1]
        for i in range(n):
            if temp >= data[i][0]:
                temp = min(data[i][1],temp)
            else:
                temp = data[i][1]
                cnt += 1
    else:
            cnt = -1
    print(f'Case {test}: {cnt}')
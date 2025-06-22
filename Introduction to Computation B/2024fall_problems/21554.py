n = int(input())
s = list(map(int, input().split()))
clct = []
for i, t in enumerate(s):
    clct.append([i+1, t])
pre = 0
tot = 0
clct.sort(key=lambda x: x[1])
num = []
for i in range(n-1):
    pre += clct[i][1]
    tot += pre
    num.append(clct[i][0])
num.append(clct[-1][0])
aver = tot/n
print(*num)
print('%.2f' % aver)
d = int(input())
n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
x = 0
y = 0
maxv = 0
num = 1
minx = min(s[i][0] for i in range(n))
maxx = max(s[i][0] for i in range(n))
miny = min(s[i][1] for i in range(n))
maxy = max(s[i][1] for i in range(n))
for x in range(max(0,minx-d), min(1025,maxx+1+d)): ### 注意加范围限制
    for y in range(max(0,miny-d), min(maxy+1+d,1025)):
        cnt = 0
        for i in range(n):
            if abs(x-s[i][0])<= d and abs(y-s[i][1]) <= d:
                cnt += s[i][2]
        if cnt > maxv:
            maxv = cnt
            num = 1
        elif cnt == maxv:
            num += 1
        else:
            continue
print(num, maxv)
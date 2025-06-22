h = int(input())
m = int(input())
s = []
for _ in range(m):
    x, y = map(float, input().split())
    s.append((x*y, 5*y))
s.sort(reverse = True) ###太粗心了，竟然忘记了reverse
time = 2*h-0.5*m
score = 0
for i in range(m):
    if time > s[i][1]/s[i][0]:
        time -= s[i][1]/s[i][0]
        score += s[i][1]
    else:
        score += time*s[i][0]
        break
print('{:.1f}'.format(score))
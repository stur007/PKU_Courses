n = int(input())
s = list(map(int, input().split()))
if n == 1:
    print(1)
    exit(0)
cnt = 1
temp = s[1] - s[0]
pre = s[1]
for i in range(2, n):
    if temp*(s[i]-pre) < 0:
        temp = s[i] - pre
        pre = s[i]
        cnt += 1
    else:
        pre = s[i]

cnt += 1

if temp == 0:
    cnt -= 1
print(cnt)

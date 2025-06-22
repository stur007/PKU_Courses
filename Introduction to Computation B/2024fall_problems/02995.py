n = int(input())
s = list(map(int, input().split()))
dp_up = [1]*n
dp_down =[1]*n
for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            dp_up[i] = max(dp_up[i], dp_up[j]+1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i-1, -1):
        if s[i] > s[j]:
            dp_down[i] = max(dp_down[i], dp_down[j]+1)

dp_tot = []
for i in range(n):
    dp_tot.append(dp_up[i]+dp_down[i]-1)

print(max(dp_tot))
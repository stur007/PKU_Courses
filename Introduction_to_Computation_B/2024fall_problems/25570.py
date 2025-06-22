n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
ans = []
i = 0
j = n-1
while True:
    if i == j:
        ans.append(s[i][i])
        break
    elif j == i+1:
        ans.append(s[i][i]+s[i][j]+s[j][i]+s[j][j])
        break
    else:
        ans.append(sum(s[i][i:j+1])+sum(s[k][i] for k in range(i+1, j))+sum(s[j][i:j+1])+sum(s[k][j] for k in range(i+1, j)))
        i += 1
        j -= 1
print(max(ans))
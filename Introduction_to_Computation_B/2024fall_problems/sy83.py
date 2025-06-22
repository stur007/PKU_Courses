n = int(input())
s = []
for _ in range(n):
    s.append(input())
ans = ''
j = 0
while True:
    for i in range(n-1):
        char = s[i][j]
        if char == s[i+1][j]:
            continue
        else:
            print(ans)
            exit(0)
    ans+= (s[0][j])
    j += 1

    ### 下面是学习之后的代码，实测正常可用：
    '''
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    m = min(len(i) for i in s)
    ans = ''
    for j in range(m):
        char = s[0][j]
        if all(s[k][j] == char for k in range(n)):
            ans += char
        else:
            break
    print(ans)
    '''
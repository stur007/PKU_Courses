n = int(input())
s = list(input().split())
first = [0,'0',0]
for i in range(n):
    for j in range(len(s[i])):
        if not s[i][j] == '0':
            break
    if j > first[0]:
        first = [j, s[i], i]
    elif j == first[0]:
        if s[i] < first[1]:
            first = [j, s[i], i]
if first == [0,'0',0]:
    s.sort()
    ans = ''.join(s)
    print(int(ans))
else:
    s.pop(first[2])
    s.sort()
    ans = ''.join(s)
    ans = first[1] + ans
    print(int(ans))
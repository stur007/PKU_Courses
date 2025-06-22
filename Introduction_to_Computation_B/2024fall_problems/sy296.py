s = list(input().split())
for i in range(len(s)):
    if s[i] in '+-':
        s[i], s[i+1] = s[i+1], s[i]
print(*s, sep = ' ')
s = input()
ans = ''
for char in s:
    if char.isupper():
        ans += char.lower()
    else:
        ans += char.upper()
print(ans)
s = input().lower()
count = 1
ans = []
for i in range(len(s)-1):
    if s[i] == s[i+1] :
     count += 1
    else:
      ans.append((s[i],count))
      count = 1

ans.append((s[-1], count))
print(''.join(f'({char},{cnt})' for char, cnt in ans))
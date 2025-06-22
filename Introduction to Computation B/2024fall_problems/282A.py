t = int(input())
ans = 0
for _ in range(t):
    code=input()
    if '++' in code:
        ans+=1
    else:
        ans-=1
print(ans)
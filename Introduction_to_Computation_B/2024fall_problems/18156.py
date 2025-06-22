t = int(input())
s = list(map(int, input().split()))
s.sort()
i = 0
j = len(s)-1
ans = float('inf')
while True:
    if i == j:
        break
    temp = s[i]+s[j]
    if temp > t:
        j -= 1
    elif temp == t:
        ans = t
        break
    else:
        i += 1
    if abs(ans-t)>abs(temp-t):
        ans = temp
    else:
        if abs(ans-t) == abs(temp-t):
            if ans > temp:
                ans = temp
print(ans)

### 暂时还没有理解，完了再思考一下
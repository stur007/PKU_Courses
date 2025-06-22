n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
s.sort()
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    i = 1
    j = n-2
    cnt = 2
    temp_l = s[0][0]
    temp_r = s[n-1][0]
    while i <= j:
        if i == j:
            temp = max(s[i][0]-temp_l, temp_r -s[j][0])
            if temp > s[i][1]:
                cnt += 1
            break
        if s[i][0]-temp_l > s[i][1]:
            temp_l = s[i][0]
            cnt += 1
        elif s[i+1][0]-s[i][0] > s[i][1]:
            temp_l = s[i][0]+s[i][1]
            cnt += 1
        else:
            temp_l = s[i][0]
        i += 1
        if temp_r -s[j][0] >s[j][1]:
            temp_r = s[j][0]
            cnt += 1
        elif s[j][0]-s[j-1][0]>s[j][1]:
            temp_r = s[j][0]-s[j][1]
            cnt += 1
        else:
            temp_r = s[j][0]
        j -= 1
    print(cnt)

### 一道崭新的题目在没有提示的情形下完整的搞定了，非常有成就感！
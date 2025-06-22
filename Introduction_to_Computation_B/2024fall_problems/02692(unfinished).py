n = int(input())
for _ in range(n):
    data = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0}
    s = []
    for _ in range(3):
        s.append(list(input().split()))
    for i in data:
        data[i] = 1
        for j in range(3):
            sum_left = 0
            sum_right = 0
            for k in range(4):
                sum_left += data[s[j][0][k]]
                sum_right += data[s[j][1][k]]
            if s[j][2] == 'even':
                if sum_left == sum_right:
                    flag = 1
                else:
                    flag = 0
                    break
            elif s[j][2] == 'up':
                if sum_left < sum_right:
                    flag = 1
                else:
                    flag = 0
                    break
            else:
                if sum_left > sum_right:
                    flag = 1
                else:
                    flag = 0
                    break
        if flag:
            print(f'{i} is the counterfeit coin and it is light.')
            break
        else:
            data[i] = -1
            for j in range(3):
                sum_left = 0
                sum_right = 0
                for k in range(4):
                    sum_left += data[s[j][0][k]]
                    sum_right += data[s[j][1][k]]
                if s[j][2] == 'even':
                    if sum_left == sum_right:
                        flag = 1
                    else:
                        flag = 0
                        break
                elif s[j][2] == 'up':
                    if sum_left < sum_right:
                        flag = 1
                    else:
                        flag = 0
                        break
                else:
                    if sum_left > sum_right:
                        flag = 1
                    else:
                        flag = 0
                        break
            if flag:
                print(f'{i} is the counterfeit coin and it is heavy.')
                break
            else:
                data[i] = 0
                continue
### 代码长度过长，稍后优化一下
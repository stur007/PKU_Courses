data = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0}
ref = 'ABCDEFGHIJKL'
def heavy(idx, s):
    if idx >= 12:
        return None
    data[ref[idx]] = 1
    for j in range(3):
        sum_left = 0
        sum_right = 0
        for k in range(4):
            sum_left += data[s[j][0][k]]
            sum_right += data[s[j][1][k]]
        if sum_left == sum_right and s[j][2] == 'even' or sum_left > sum_right and s[j][2] == 'up' or sum_left < sum_right and s[j][2] == 'down':
            continue
        else:
            data[ref[idx]] = 0
            return heavy(idx+1, s)
    data[ref[idx]] = 0
    return f'{ref[idx]} is the counterfeit coin and it is heavy. '


def light(idx, s):
    if idx >= 12:
        return

    data[ref[idx]] = -1
    for j in range(3):
        sum_left = 0
        sum_right = 0
        for k in range(4):
            sum_left += data[s[j][0][k]]
            sum_right += data[s[j][1][k]]
        if sum_left == sum_right and s[j][2] == 'even' or sum_left > sum_right and s[j][
            2] == 'up' or sum_left < sum_right and s[j][2] == 'down':
            continue
        else:
            data[ref[idx]] = 0
            return light(idx + 1, s)
    data[ref[idx]] = 0
    return f'{ref[idx]} is the counterfeit coin and it is light. '

t = int(input())
for _ in range(t):
    s = []
    for _ in range(3):
        s.append(list(input().split()))
    if heavy(0, s) is None:
        print(light(0 ,s))
    else:
        print(heavy(0, s))
    # print(data)

while True:
    n = int(input())
    if n == 0:
        break
    h = int(input())
    num = h*12
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    t = list(map(int, input().split()))
    stay_time = []
    fish_num = []
    i = 0
    current_fish = 0
    current_time = 0
    while num > 0:
        if i < n-2:
            if data[i][0] >= data[i+1][0]/(1+t[i]):
                num -= 1
                current_time += 5
                current_fish += data[i][0]
                data[i][0] -= data[i][1]
            else:
                stay_time.append(current_time)
                fish_num.append(current_fish)
                current_fish = 0
                num -= t[i]
                i += 1
        else:
            num -= 1
            current_fish += data[i][0]
            data[i][0] -= data[i][1]
    print(*stay_time, sep = ', ')
    print('Number of fish expected: '+str(sum(fish_num)))
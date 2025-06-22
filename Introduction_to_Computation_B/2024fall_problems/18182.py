t = int(input())
for _ in range(t):
    n,m,b = map(int, input().split())
    skills = []
    for _ in range(n):
        skills.append([int(x) for x in input().split()])
    skills.sort(key = lambda x:(x[0], -x[1]))
    time = 0
    cnt = 0
    for i in range(n):
        damage_time = skills[i][0]
        damage_point = skills[i][1]
        if time == damage_time:
            if cnt < m:
                cnt += 1
                b -= damage_point
            else:
                continue
        else:
            cnt = 1      #注意这个初始条件，用了我很长时间排查
            time = damage_time
            b -= damage_point

        if b <= 0:
            print(time)
            break
    if b > 0:
        print('alive')
import math
while True:
    N = int(input())
    if N == 0:
        break
    arrival_times = []
    for _ in range(N):
        speed, time =[int(x) for x in input().split()]
        if time < 0:
            continue
        arrival_time = time + math.ceil(4.5 / speed * 3600)
        arrival_times.append(arrival_time)
    print(min(arrival_times))
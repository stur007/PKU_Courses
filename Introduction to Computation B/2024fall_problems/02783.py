while True:
    n = int(input())
    if n == 0:
        break
    hotels = []
    cnt = 0
    for _ in range(n):
        hotels.append([int(x) for x in input().split()])
    hotels.sort(key = lambda x:(x[0], x[-1]))
    cnt = 1
    most_cheap = hotels[0][1]
    for hotel in hotels:
        if hotel[1] < most_cheap:
            cnt += 1
            most_cheap = hotel[1]
    print(cnt)

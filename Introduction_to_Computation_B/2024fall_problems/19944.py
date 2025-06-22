n = int(input())
week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for _ in range(n):
    date = input()
    c = int(date[0:2])
    y = int(date[2:4])
    m = int(date[4:6])
    if m == 1:
        m = 13
        if y == 0:
            c -= 1
            y = 99
        else:
            y -= 1
    if m == 2:
        m = 14
        if y == 0:
            c -= 1
            y = 99
        else:
            y -= 1
    d = int(date[6:8])
    w = (y + int(y/4) + int(c/4) -2*c + int(26*(m +1)/10) + d - 1) % 7
    print(week[w])
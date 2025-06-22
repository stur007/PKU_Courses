while True:
    try:
        a, b = input().split()
    except:
        break
    for i in range(min(int(a), int(b)) + 1, 0, -1):
        if int(a) % i == 0 and int(b) % i == 0:
            print(i)
            break
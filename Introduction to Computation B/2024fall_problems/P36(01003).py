while True:
    n = float(input())
    if n == 0 :
        break
    cnt = 0
    length = 0
    while length < n :
        cnt += 1
        length += 1/(cnt+1)
    print(str(cnt)+' card(s)')
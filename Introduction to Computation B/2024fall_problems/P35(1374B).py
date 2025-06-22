t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(0)
    else:
        cnt_3 = 0
        cnt_2 = 0
        while n % 3 == 0 :
            cnt_3 += 1
            n = n / 3
        while n % 2 == 0 :
            cnt_2 += 1
            n = n / 2
        if n == 1:
            if cnt_3 < cnt_2 :
                print(-1)
            else:
                print(2 * cnt_3 - cnt_2)
        else:
            print(-1)
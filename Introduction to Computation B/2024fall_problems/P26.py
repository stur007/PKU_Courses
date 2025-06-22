numbers=list(input())
count_0=0
count_1=0
for number in numbers:
    if number=='1':
        count_0=0
        count_1+=1
        if count_1==7:
            print('YES')
            break
    else:
        count_1 = 0
        count_0 += 1
        if count_0 == 7:
            print('YES')
            break
if count_1<7 and count_0<7:
    print('NO')
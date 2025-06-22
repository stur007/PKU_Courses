t = int(input())
for _ in range(t):
    a = int(input())
    n=2/(1-a/180)#运算不准确，尽量少用
    n=round(n,2)
    if n%1==0:
        print('YES')
    else:
        print('NO')
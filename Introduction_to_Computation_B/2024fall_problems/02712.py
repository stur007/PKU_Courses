n= int(input())
for _ in range(n):
    ini_mon, ini_day, ini_num, fin_mon, fin_day =[int(x) for x in input().split()]
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if ini_mon == fin_mon:
        during = fin_day - ini_day
    else:
        during = days[ini_mon - 1] - ini_day + sum(days[ini_mon:fin_mon-1]) + fin_day
    print(ini_num*2**during)

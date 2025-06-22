import math

t = int(input())
for _ in range(t):
    n, m =[int(x) for x in input().split()]
    c = math.gcd(n ,m)
    k = round(math.log(m/c, 2), 3)
    i = round(math.log(n/c, 3), 3)
    if i >= k and i == int(i) and k == int(k) :
        print('YES')
    else:
        print('NO')
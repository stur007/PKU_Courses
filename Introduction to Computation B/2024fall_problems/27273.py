import math

t= int(input())
for _ in range(t):
    n = int(input())
    s = n*(n+1)/2
    m = int(math.log(n,2))
    s_2_n = 2*(1-2**(m+1))/(1-2)
    print(int(s - s_2_n))


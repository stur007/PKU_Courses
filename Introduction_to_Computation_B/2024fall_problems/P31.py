L, M = [int(x) for x in input().split()]
series = [1] * (L+1)
for _ in range(M):
    a,b = [int(y) for y in input().split()]
    series[a:b+1]=[0] *(b+1-a)
print(sum(series))
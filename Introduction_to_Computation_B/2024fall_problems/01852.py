t = int(input())
for _ in range(t):
    l, t = [int(x) for x in input().split()]
    n = [int(y) for y in input().split()]
    n_min = []
    n_max = []
    for i in n:
        j = min(i, l - i)
        k = max(i, l - i)
        n_min.append(j)
        n_max.append(k)
    t_min = max(n_min)
    t_max = max(n_max)
    print(t_min, t_max)
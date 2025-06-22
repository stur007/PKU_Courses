n = int(input())
p = [float(x) for x in input().split()]
cost_min = float('inf')
profit_max = 0
for i in range(n-1):
    if p[i] < cost_min:
        cost_min = p[i]
    if (p[i]-cost_min)/cost_min >= profit_max:
        profit_max = (p[i]-cost_min)/cost_min
ans = 100*profit_max +100
print(f'{ans:.2f}')
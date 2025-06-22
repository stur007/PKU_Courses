n = int(input())
t=[int(x) for x in input().split()]
t.sort()

count=0
cumulative_time = 0

for t_i in t:
    if cumulative_time <= t_i:
        count+=1
        cumulative_time+=t_i

print(count)
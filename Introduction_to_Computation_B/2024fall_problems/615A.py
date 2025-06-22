from os import remove

n,m =[int(a) for a in input().split()]
my = [0]*m
for _ in range(n):
    x = [int(b) for b in input().split()]
    x.pop(0)
    for b in x:
        my[b-1] = 1

if sum(my) == m:
    print('YES')
else:
    print('NO')
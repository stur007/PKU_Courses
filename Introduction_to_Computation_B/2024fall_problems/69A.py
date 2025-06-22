n = int(input())
x_s=[]
y_s=[]
z_s=[]
for _ in range(n):
    x,y,z=[int(x) for x in input().split()]
    x_s.append(x)
    y_s.append(y)
    z_s.append(z)
if sum(x_s)==0 and sum(y_s)==0 and sum(z_s)==0:
    print('YES')
else:
    print('NO')

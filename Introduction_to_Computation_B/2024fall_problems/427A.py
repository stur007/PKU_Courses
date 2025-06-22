n=int(input())
a_s=[]
b_s=[]
for _ in range(n):
    a,b=[int(x) for x in input().split()]
    a_s.append((a,_))
    b_s.append((b,_))

a_s.sort()
b_s.sort()

for i in range(n):
    if a_s[i][1] != b_s[i][1]:
        print('Happy Alex')
        break
else:
    print('Poor Alex')
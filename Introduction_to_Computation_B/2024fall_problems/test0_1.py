t=int(input())
for _ in range(t):
    n=int(input())
    rooms=[0]*n
    for i in range(n):
        for j in range(n):
            if (j+1)%(i+1)==0:
                if rooms[j]==1:
                    rooms[j]=0
                else:
                    rooms[j]=1
    print(sum(rooms))
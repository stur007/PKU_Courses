n,k=map(int,input().split())
scores=[int(x) for x in input().split()]
num=0
for i in range(n):
    if scores[i] >=scores[k-1] and scores[i]>0:
        num+=1

print(num)
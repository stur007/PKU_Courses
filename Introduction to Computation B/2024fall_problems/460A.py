n,m=[int(x) for x in input().split()]
cnt=0
while n-m>=0:
    n=n-m+1
    cnt+=m
cnt+=n
print(cnt)
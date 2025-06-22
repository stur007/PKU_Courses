m,n,a=map(int,input().split())
if m%a==0:
    num_m=m//a
else:
    num_m=m//a+1

if n%a==0:
    num_n=n//a
else:
    num_n=n//a+1

print(num_m*num_n)
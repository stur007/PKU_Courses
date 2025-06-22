n,k,l,c,d,p,nl,np=[int(x) for x in input().split()]
num_1=(k*l)//(n*nl)
num_2=(c*d)//n
num_3=p//(n*np)
print(min(num_2,num_3,num_1))

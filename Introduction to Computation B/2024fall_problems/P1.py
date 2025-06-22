a=int(input())
list=[]
for i in range(0,int(a/4)+1):
    j=(a-4*i)/2
    if j%1==0:
        list.append(i+j)
if list:
    print(int(list[-1]),int(list[0]))
else:
    print(0,0)



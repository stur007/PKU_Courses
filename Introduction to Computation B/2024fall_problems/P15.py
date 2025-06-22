t = int(input())
for i in range(t):
    n = list(input())
    count=0
    for j in range(len(n)):
       if int(n[j])!=0:
           count+=1
           n[j]=str(int(n[j])*10**(len(n)-j-1))
    print(count)
    n_new=[]
    for num in n:
        if num!='0':
            n_new.append(num)
    print(*n_new,sep=' ')


rr=0
while True:
    n,d=map(int,input().split())
    if n==d==0:
        break
    else:
        rr+=1
        empty=[]
        for i in range(n):
            x,y=map(int,input().split())
            if d>=y:
                #empty.append([x+(d**2-y**2)**0.5,x-(d**2-y**2)**0.5])
                empty.append([x-(d**2-y**2)**0.5,x+(d**2-y**2)**0.5])
        input()
        if len(empty)<n:
            print("Case {}: -1".format(rr))
        elif d<0:
            print("Case {}: -1".format(rr))
        else:
            empty.sort(reverse=True)
            #number=n
            number = len(empty)
            c = empty[0][0]
            for j in range(1,n):
                #if empty[j][0]>=empty[j-1][1]:
                if c > empty[j][1]:
                    c = empty[j][0]
                else:
                   number-=1

            print("Case {}: {} ".format(rr,number))
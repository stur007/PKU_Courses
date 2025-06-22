n=int(input())
a=[int(x) for x in input().split()]
m=int(input())
b=[int(y) for y in input().split()]
a.sort()
b.sort()
i,j=0,0 #使用双指针判断
cnt=0
while i<n and j<m:
    if abs(a[i]-b[j])<= 1 :
        cnt+=1
        i+=1
        j+=1
    elif a[i]<b[j]:
        i+=1
    elif a[i]>b[j]:
        j+=1

print(cnt)

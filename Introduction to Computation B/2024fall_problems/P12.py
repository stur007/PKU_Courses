n=int(input())
stones=list(input())
num=0
for i in range(1,len(stones)):
    if stones[i]==stones[i-1]:
        num+=1
print(num)
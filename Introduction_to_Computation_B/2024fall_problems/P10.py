name=list(input())
name.sort()

count=1
for i in range(1,len(name)):
    if name[i]!=name[i-1]:
        count=count+1

if count%2==1:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')
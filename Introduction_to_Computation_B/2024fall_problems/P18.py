n=int(input())
events=[int(x) for x in input().split()]
count=0
add=0
for i in range(n):
    add+=events[i]
    if add<0:
        count+=1
        add=0
print(count)
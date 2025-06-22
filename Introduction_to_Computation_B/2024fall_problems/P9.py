n=int(input())
count=0
for i in range(n):
    scores=input().split()
    tot=0
    for score in scores:
        score=int(score)
        tot+=score
    if tot>=2:
        count+=1
print(count)
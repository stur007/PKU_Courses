s=input()
m=int(input())
ans=[0]
count=0
answer=[]
for i in range(len(s)):
    if s[i-1] == s[i]:
        count+=1
        ans.append(count)
for _ in range(m):
    l,r=[int(x) for x in input().split()]
    answer.append(ans[r-1]-ans[l-1])
print(*answer,sep='\n')
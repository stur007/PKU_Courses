s=input()
ref=['1','2','3']
nums=[]

for char in s:
    if char in ref:
        nums.append(char)

nums.sort()
print(*nums,sep='+')

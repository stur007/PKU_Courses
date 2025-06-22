n = int(input())
strs =[]
while n >= 8 :
    strs.append(n%8)
    n=n//8
strs.append(n)
strs.reverse()
print(*strs,sep='')
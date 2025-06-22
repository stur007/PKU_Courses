import math
s = input()
m = math.floor(math.log(len(s),2))
sequence = []
ans = []
for i in range(m+1):
    sequence.append(s[int(math.pow(2,i))-1])
while sequence:
    ans.append(sequence.pop(0))
    if sequence:
        ans.append(sequence.pop(-1))
print(*ans,sep = '')
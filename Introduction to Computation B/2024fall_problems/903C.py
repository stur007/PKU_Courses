from itertools import count

n = int(input())
a = [int(x) for x in input().split()]

a_org={}

for a_i in a:
    if a_i in a_org:
        a_org[a_i] += 1
    else:
        a_org[a_i] = 1
print(max(a_org.values()))

#another possible version
from collections import Counter

m = int(input())
b=[int(x) for x in input().split()]
count =  Counter(b)
print(max(count.values()))
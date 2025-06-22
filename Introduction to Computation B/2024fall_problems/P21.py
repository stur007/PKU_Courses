n=int(input())
numbers=[int(x) for x in input().split()]
features=[]
for number in numbers:
    features.append(number%2)
if sum(features)==1:
    print(features.index(1)+1)
else:
    print(features.index(0)+1)
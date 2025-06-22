n,l = [int(x) for x in input().split()]
a=[int(y) for y in input().split()]
a.sort()
distance=[a[0]-0,l-a[-1]]
for i in range(n-1):
    distance.append((a[i+1]-a[i])/2)
print(max(distance))
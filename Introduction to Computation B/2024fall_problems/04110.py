n, w_m = [int(x) for x in input().split()]
candies = []
for _ in range(n):
    v,w = [int(x) for x in input().split()]
    candies.append((v/w,v,w))
candies.sort(reverse = True)
capacity = 0
value = 0
for candy in candies:
    if w_m - capacity >= candy[2]:
        capacity += candy[2]
        value += candy[1]
    else:
        value += candy[0]*(w_m -capacity)
        break
print('{:.1f}'.format(value))

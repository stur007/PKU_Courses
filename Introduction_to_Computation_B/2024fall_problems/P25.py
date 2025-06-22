n = int(input())
coins=[int(x) for x in input().split()]
coins.sort(reverse=True)
tot=0
count=0
for coin in coins:
    tot+=coin
    count+=1
    if tot > sum(coins)/2:
        break
print(count)
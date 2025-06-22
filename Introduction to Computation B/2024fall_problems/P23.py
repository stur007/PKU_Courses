n,m = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()]
negative_prices=[]
for price in prices:
    if price <0:
        negative_prices.append(price)
negative_prices.sort()
if m>=len(negative_prices):
    print(-sum(negative_prices))
else:
    print(-sum(negative_prices[0:m]))
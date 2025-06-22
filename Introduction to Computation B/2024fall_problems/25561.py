n, m = map(int, input().split())
prices = [dict() for _ in range(n)]
for i in range(n):
    s = list(input().split())
    for j in range(len(s)):
        separate_idx = s[j].index(':')
        market = int(s[j][:separate_idx])-1
        price = int(s[j][separate_idx+1:])
        prices[i][market] = price


coupons = []
for k in range(m):
    t = input().split()
    temp = []
    for l in range(len(t)):
        separate_idx = t[l].index('-')
        q = int(t[l][:separate_idx])
        x = int(t[l][separate_idx+1:])
        temp.append((q, x))
    temp.sort()
    coupons.append(temp[:])

min_total_bill = float('inf')
shopping_list = [0 for _ in range(m)] #从m个店铺购买的商品总价
def dfs(kind):
    global min_total_bill
    if kind == n:
        total_bill = 0
        for i in range(m):
            money = shopping_list[i]
            real_cost = money
            for coupon in coupons[i]:
                if money >= coupon[0]:
                    real_cost = min(real_cost, money-coupon[1])
                else:
                    break
            total_bill += real_cost
        times = sum(shopping_list)//300
        total_bill -= times*50
        min_total_bill = min(total_bill, min_total_bill)
        return

    for market, price in prices[kind].items():
        shopping_list[market] += price
        dfs(kind+1)
        shopping_list[market] -= price
dfs(0)
print(min_total_bill)
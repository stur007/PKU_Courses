n = int(input())
num = list(map(int, input().split()))
prices = [1,2,5,10,20,50,100]

if n%50 != 0:
    print('Fail')
    exit()
n = n//50
dp = [float('inf')]*(n+1)
dp[0] = 0
for i in range(7):
    price = prices[i]
    max_count = num[i]

    k = 1
    while k <= max_count:
        for j in range(n, price*k-1, -1):
            dp[j] = min(dp[j], dp[j-price*k]+k)
        max_count -= k
        k *= 2
    if max_count > 0:
        for j in range(n, price*max_count-1, -1):
            dp[j] = min(dp[j], dp[j-price*max_count]+max_count)

if dp[-1] == float('inf'):
    print('Fail')
else:
    print(dp[-1])

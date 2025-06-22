dp = [-1]*1000001
dp[1] =1
dp[2] =2
for i in range(3,1000001):
    dp[i]= (2*dp[i-1]+dp[i-2])%32767
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
#如果使用函数递归调用会爆栈，导致runtime error
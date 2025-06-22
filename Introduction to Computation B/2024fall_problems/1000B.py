'''n, M = map(int ,input().split())
a = list(map(int, input().split()))
a.append(M)
period_l = [a[0]]
period_d = []
for i in range(n):
    if i %2 == 0:
        period_d.append(a[i+1]-a[i])
    else:
        period_l.append(a[i+1]-a[i])
if len(period_d)>=len(period_l):
    delta = [period_d[-1]-1]
    for i in range(len(period_l)-2,-1,-1):
        current = delta[-1] -period_l[i+1]+period_d[i]
        delta.append(current)
else:
    delta = [period_d[-1]-1-period_l[-1]]
    for i in range(len(period_d)-2,-1,-1):
        current = delta[-1] -period_l[i]+period_d[i]
        delta.append(current)
ans = sum(period_l)+max(max(delta),0)
print(ans)'''
### 不是不能行，只是解法有点复杂（如何减少思考量），而且忽略了间隔为1的情形，不能插入内容
n, M = map(int ,input().split())
a = [0]
a.extend(list(map(int, input().split())))
a.append(M)
pre = [0]
for i in range(n+1):
    if i%2 == 0:
        current = pre[-1]+a[i+1]-a[i]
        pre.append(current)
    else:
        current = pre[-1]
        pre.append(current)
maxv = pre[-1]
for i in range(n+1):
    if a[i+1]-a[i]>1:
        if i %2 == 0:
            current = pre[i+1]-1+(M-a[i+1])-(pre[-1]-pre[i+1])
        else:
            current = pre[i]+a[i+1]-a[i]-1 + (M-a[i+1])-(pre[-1]-pre[i+1])
        maxv = max(current, maxv)
print(maxv)

### 这段代码一下子就通过了，因为减少了大量加减1，判断奇数偶数的计算
### 在时空复杂度一定的情形下，越简单的代码越不容易出错
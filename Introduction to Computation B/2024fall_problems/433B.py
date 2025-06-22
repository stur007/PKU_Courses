n = int(input())
v = list(map(int,input().split()))
sum_v = [0]*(n+1)
for i in range(1,n+1):
    sum_v[i] = sum_v[i-1] +v[i-1]
sv = sorted(v)
sum_sv = [0]*(n+1)
for i in range(1,n+1):
    sum_sv[i] = sum_sv[i-1] +sv[i-1]
m = int(input())
for _ in range(m):
    t, l, r = map(int,input().split())
    if t == 1:
        print(sum_v[r]-sum_v[l-1])
    else:
        print(sum_sv[r]-sum_sv[l-1])

### 注意反复进行求和操作时的简化方法
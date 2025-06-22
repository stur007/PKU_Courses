t = int(input())
for _ in range(t):
    s = int(input())
    a = int(input())
    A = [int(x) for x in input().split()]
    b = int(input())
    B = [int(y) for y in input().split()]

    cnt = 0
    count_a ={}
    for i in A:
        if i in count_a:
            count_a[i] += 1
        else:
            count_a[i] = 1
    for j in B:
        if s - j in count_a:
            cnt += count_a[s - j]
    print(cnt)

### 减少重复工作，尽量减少反复排查的次数
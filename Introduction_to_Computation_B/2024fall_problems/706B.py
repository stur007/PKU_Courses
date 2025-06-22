n = int(input())
x = list(map(int, input().split()))
x.sort()
ans = []
i = 0
j = 0
while i <x[-1]:
    if i<x[j]:
        ans.append(j)
        i += 1
    else:
        if x[j] == x[-1]:
            ans += [j]*(x[-1]-len(ans))
            break
        else:
            j += 1
q = int(input())
for _ in range(q):
    m = int(input())
    if m < x[-1]:
        print(ans[m])
    else:
        print(n)


n = int(input())
a = [int(x) for x in input().split()]
count = 1
answer = []
for i in range(n - 1) :
    if a[i+1] >= a[i] :
        count += 1
    else:
        answer.append(count)
        count = 1
answer.append(count)
print(max(answer))
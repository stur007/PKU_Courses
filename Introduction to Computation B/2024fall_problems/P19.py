t=int(input())
for i in range(t):
    numbers=[int(x) for x in input().split()]
    max_number=max(numbers)
    if sum(numbers) ==2*max_number:
        print('YES')
    else:
        print('NO')
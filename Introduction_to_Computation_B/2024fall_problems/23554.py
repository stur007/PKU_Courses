n = int(input())
s = [int(x) for x in input().split()]

else_number = []
original_number = [i for i in range(1, n+1)]

for num in s:
    if num <= n:
        original_number.remove(num)
    else:
        else_number.append(num)
else_number.sort()
print(*original_number)
print(*else_number)
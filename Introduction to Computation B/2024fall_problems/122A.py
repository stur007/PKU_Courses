n = int(input())
lucky = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
list = []
for i in lucky:
    if n % i == 0:
        list.append(i)
        break
if list:
    print('YES')
else:
    print('NO')

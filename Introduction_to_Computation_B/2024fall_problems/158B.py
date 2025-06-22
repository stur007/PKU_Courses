'''
n = int(input())
students = [int(x) for x in input().split()]
num_of_cars = 0
num_of_students = {1:0,2:0,3:0,4:0}
for student in students:
    num_of_students[student] += 1
num_of_cars += num_of_students[4]
if num_of_students[2] % 2 == 0:
    num_of_cars += num_of_students[2] / 2
    num_left = 0
else:
    num_of_cars += num_of_students[2] // 2
    num_left = 1
if num_of_students[3] >= num_of_students[1]:
    num_of_cars += num_of_students[3]
    num_of_cars += num_left
else:
    num_of_cars += num_of_students[3]
    if (num_of_students[1] -num_of_students[3]) % 4 == 0:
        num_of_cars += (num_of_students[1] - num_of_students[3]) // 4 + num_left
    elif (num_of_students[1] -num_of_students[3]) % 4 == 1:
        num_of_cars += (num_of_students[1] - num_of_students[3]) // 4 + 1
    elif (num_of_students[1] -num_of_students[3]) % 4 == 2:
        num_of_cars += (num_of_students[1] - num_of_students[3]) // 4 + 1
    else:
        num_of_cars += (num_of_students[1] - num_of_students[3]) // 4 + num_left + 1
print(int(num_of_cars))
'''

### 下面化简一下上面的代码
from collections import defaultdict
import math
n = int(input())
s = list(map(int, input().split()))
ss = defaultdict(int)
for i in range(n):
    ss[s[i]] += 1
cars = ss[4]+ss[3]
if ss[2]%2 == 0:
    cars += int(ss[2]/2)
    if ss[1] >= ss[3]:
        a = math.ceil((ss[1]-ss[3])/4)
        cars += a
else:
    cars += int(ss[2]/2)+1
    if ss[1]-ss[3]-2 >= 0:
        cars += math.ceil((ss[1]-ss[3]-2)/4)
print(cars)

### 注意一下向上取整函数
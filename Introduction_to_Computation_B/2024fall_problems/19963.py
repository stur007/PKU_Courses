n = int(input())
pairs = [i[1:-1] for i in input().split()]
distances = [sum(map(int,i.split(','))) for i in pairs]
costs = [int(x) for x in input().split()]
data_d = {}
data_c = {}
data_r = {}
for index, distance in enumerate(distances):
    data_d[index] = distance
for index, cost in enumerate(costs):
    data_c[index] = cost
for index in range(n):
    data_r[index] = data_d[index]/data_c[index]
sorted_r = sorted(data_r.items(), key=lambda  item:item[1])
sorted_c = sorted(data_c.items(), key=lambda  item:item[1])
alter_r = []
alter_c = []
if n%2 == 1:
    medi_r = sorted_r[int((n-1)/2)][1]
    medi_c = sorted_c[int((n-1)/2)][1]
else:
    medi_r = (sorted_r[int((n-2)/2)][1]+sorted_r[int(n/2)][1])/2
    medi_c = (sorted_c[int((n-2)/2)][1]+sorted_c[int(n/2)][1])/2

for i in range(n):
    if sorted_r[i][1] > medi_r:
        alter_r.append(sorted_r[i][0])
    if sorted_c[i][1] < medi_c:
        alter_c.append(sorted_c[i][0])
print(len(set(alter_c)&set(alter_r)))

###gpt简化后的结果
'''
n = int(input())
pairs = [map(int, i[1:-1].split(',')) for i in input().split()]                         ###注意split()的使用
distances = [sum(pair) for pair in pairs]
costs = list(map(int, input().split()))

data_r = [d/c for d, c in zip(distances, costs)]                                        ###注意zip()的使用
sorted_r = sorted(enumerate(data_r), key=lambda item: item[1])                          ###注意enumerate()的使用
sorted_c = sorted(enumerate(costs), key=lambda item: item[1])

median_r = (sorted_r[(n-1)//2][1] + sorted_r[n//2][1]) / 2 if n % 2 == 0 else sorted_r[(n-1)//2][1]   ###条件判断的简化方式
median_c = (sorted_c[(n-1)//2][1] + sorted_c[n//2][1]) / 2 if n % 2 == 0 else sorted_c[(n-1)//2][1]

alter_r = {index for index, value in sorted_r if value > median_r}                     ###既然最后要逐一判断，那么排队就丧失了意义
alter_c = {index for index, value in sorted_c if value < median_c}

print(len(alter_r & alter_c))
'''


###更简单的方式：直接使用statistics.median()进行处理
'''
import statistics
n = int(input())
distance = list(map(lambda x:sum(eval(x)),input().split()))
prize = list(map(int,input().split()))
average = list(distance[i]/prize[i] for i in range(n))
prize_median = statistics.median(prize)
average_median = statistics.median(average)
num = 0
for i in range(n):
    if average[i] > average_median and prize[i] < prize_median:
        num += 1
print(num)
'''
"""
用时将近一小时改写出来的代码
n = int(input())
s = []
name = set()
for _ in range(n):
    s.append(input().split('-'))
    name.add(s[-1][0])
name = list(name)
name.sort()
ans = [[] for _ in range(len(name))]
for i in range(n):
    ans[name.index(s[i][0])].append(s[i][1])
for j in range(len(name)):
    ans[j].sort(key=lambda x: (-ord(x[-1]), float(x[:-1])))
result = list(zip(name, ans))
for i in result:
    print(f'{i[0]}: {", ".join(i[1])}')
    """

###经过一番修改代码终于不会报错了，下面试图重构一下使得代码更加条理。
'''n = int(input())
pairs = {}
for _ in range(n):
    s = input().split('-')
    if s[0] in pairs:
        pairs[s[0]].append(s[1])
    else:
        pairs[s[0]] = [s[1]]
for key in pairs:
    pairs[key].sort(key=lambda x: (-ord(x[-1]), float(x[:-1])))
for key in sorted(pairs.keys()):
    print(f"{key}: {', '.join(pairs[key])}")'''
### 似乎并没有简化多少，但是逻辑上变得清晰了，试试看能否更加简化

from collections import defaultdict

n = int(input())
pairs = defaultdict(list)

for _ in range(n):
    s = input().split('-')
    pairs[s[0]].append(s[1])

for key in sorted(pairs):
    print(f"{key}: {', '.join(sorted(pairs[key], key=lambda x: (-ord(x[-1]), float(x[:-1]))))}")

### 实践证明，时间变化不大，主要是内存简化了
### 学会了使用defaultdict以及各种简化排列的方式
### 学会了字符串比大小的方式，优先进行字典序比较，然后进行长度比较，同时学会了逆序比较的方式
### 另外学会了多重比较的方式，例如：
'''
data = ["123aaa", "124aaa", "124abc", "120eeee"]

# 自定义排序键
sorted_data = sorted(data, key=lambda x: (x[3:], int(x[:3])), reverse=(False, True))

# 输出结果
print(sorted_data)
'''

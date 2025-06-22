# Assignment 2: 语法练习

2024 fall, Complied by ==任宇桐 物理学院==

## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A

思路：

创建二维列表存储数字的位置，然后根据索引直接计算。

##### 代码

```python
# Python
for i in range(5):
    line=input().split()
    if '1' in line:
        print(abs(i-2)+abs(line.index('1')-2))
        break

```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20240924141815686.png)

### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：

如果直接按照题目的表示方式进行计算应该会超时，发现其实这道题目可以直接通过数学计算解决，但是注意取余数要先计算。

##### 代码

```python
# Python
n=int(input())
for i in range(n):
    a,b=[int(x) for x in input().split()]
    if a%b!=0:
        print(b-a%b)
    else:
        print(0)
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20240924141853698.png)

### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A

耗时：15-20 min

思路：

第一次做题的时候没有理解"untreated"的具体要求，后来发现似乎之后增加的policeman不用管之前的case，之后就成功通过了。

##### 代码

```python
# Python
n=int(input())
events=[int(x) for x in input().split()]
count=0
add=0
for i in range(n):
    add+=events[i]
    if add<0:
        count+=1
        add=0
print(count)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20240924142039111.png)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：

第一次完成的时候在创建列表的时候遇到了障碍，后来求助学会了这种方式。

##### 代码

```python
# Python
L, M = [int(x) for x in input().split()]
series = [1] * (L+1)
for _ in range(M):
    a,b = [int(y) for y in input().split()]
    series[a:b+1]=[0] *(b+1-a)
print(sum(series))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20240924142227081.png)

### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：

直接枚举即可，注意答案输出的方式。

##### 代码

```python
#Python
a, b = map(int,input().split())
ans = []
for i in range(a, b+1):
    s = str(i)
    if i == int(s[0])** 3 +int(s[1]) ** 3 +int(s[2]) ** 3:
        ans.append(i)
if ans:
    print(*ans)
else:
    print('NO')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20240924142420400.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/

耗时：20+min

思路：

第一次完成这道题目花了很长时间，没有理解题目的数学要求，还以为要逐次计算，写了很长的代码都不能AC。之后参考了答案，发现可以直接计算能追上的最快对象即可，感觉还是挺有意思的。

##### 代码

```python
# Python
import math
while True:
    N = int(input())
    if N == 0:
        break
    arrival_times = []
    for _ in range(N):
        speed, time =[int(x) for x in input().split()]
        if time < 0:
            continue
        arrival_time = time + math.ceil(4.5 / speed * 3600)
        arrival_times.append(arrival_time)
    print(min(arrival_times))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20240924142513338.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

这些题目中出现了几个数学题目，感觉不是简单翻译题目就能做对的，感觉还是挺有意思的。基本上一直在跟进每日选做，发布的全部完成。
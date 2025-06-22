# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>任宇桐 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：

直接暴力计算出所有的满足位置的日期，然后按照大小筛选对应满足要求的位置即可。

代码：

```python
cnt = 0
while True:
    cnt += 1
    p, e, i, d =[int(x) for x in input().split()]
    if (p,e,i,d) == (-1,-1,-1,-1):
        break
    list_p = [p+j*23 for j in range(int(21252/23)+d+1)]
    list_e = [e+j*28 for j in range(int(21252/28)+d+1)]
    list_i = [i+j*33 for j in range(int(21252/33)+d+1)]
    answers = list(set(list_p)&set(list_e)&set(list_i))
    answers.sort()
    while answers[0] <= d:
        answers.pop(0)
    ans = answers[0]-d
    print('Case '+str(cnt)+': the next triple peak occurs in '+str(ans)+' days.')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241022130054908.png)

### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：

一开始没有看见tag，然后尝试的各种方式，没有找到规律，然后参考了two pointers的指示才开始往这个方向想。

代码：

```python
p = int(input())
s = list(map(int, input().split()))
s.sort()

my = 0  
other = 0  

while my >= other and s:
    if p >= s[0]:
        p -= s[0]
        my += 1
        s.pop(0)
    elif len(s) > 1 and my - other >= 1:  ###注意取等条件！！！不要在边界条件上出错
        p = p + s[-1] - s[0] 
        other += 1
        my += 1
        s.pop(0)  
        s.pop(-1)
    else:
        break

print(my - other)
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241022131011878.png)

### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：

排序的思路还是比较顺利的，主要是复习了一下小数的输出方法。

代码：

```python
n = int(input())
s = list(map(int, input().split()))
clct = []
for i, t in enumerate(s):
    clct.append([i+1, t])
pre = 0
tot = 0
clct.sort(key=lambda x: x[1])
num = []
for i in range(n-1):
    pre += clct[i][1]
    tot += pre
    num.append(clct[i][0])
num.append(clct[-1][0])
aver = tot/n
print(*num)
print('%.2f' % aver)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241022130227704.png)

### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：

整体还是比较顺利的，第一次尝试的时候忘记了print(n),然后不知道为什么错。

代码：

```python
n = int(input())
haab = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax',
        'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
tzolkin = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk',
           'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
print(n) 
for _ in range(n):
    s = input().split()
    haab_date = int(s[0][:-1])
    haab_month = haab.index(s[1])
    haab_year = int(s[2])
    days = haab_year *365 +haab_month *20 + haab_date
    tzolkin_year, reserve_days = divmod(days, 260)
    tzolkin_number = (reserve_days%13)+1
    tzolkin_letter = reserve_days%20
    print(tzolkin_number,tzolkin[tzolkin_letter], tzolkin_year)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241022130509217.png)

### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：

认真思考以后，发现其实思路还是比较明确的，从两边开始，树木向两侧倒，然后尝试向中间倒，倒不下就跳过。

代码：

```python
n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
s.sort()
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    i = 1
    j = n-2
    cnt = 2
    temp_l = s[0][0]
    temp_r = s[n-1][0]
    while i <= j:
        if i == j:
            temp = max(s[i][0]-temp_l, temp_r -s[j][0])
            if temp > s[i][1]:
                cnt += 1
            break
        if s[i][0]-temp_l > s[i][1]:
            temp_l = s[i][0]
            cnt += 1
        elif s[i+1][0]-s[i][0] > s[i][1]:
            temp_l = s[i][0]+s[i][1]
            cnt += 1
        else:
            temp_l = s[i][0]
        i += 1
        if temp_r -s[j][0] >s[j][1]:
            temp_r = s[j][0]
            cnt += 1
        elif s[j][0]-s[j-1][0]>s[j][1]:
            temp_r = s[j][0]-s[j][1]
            cnt += 1
        else:
            temp_r = s[j][0]
        j -= 1
    print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241022130630387.png)

### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：

一开始分类讨论了很久，然后发现和进程检测是一样的。

代码：

```python
import math
test = 1
while True:
    s = input()
    if len(s.lstrip()) == 0:
        test += 1
        continue
    n,d = map(int, s.split())
    if (n,d) == (0,0):
        break
    data = []
    cnt = 0
    for _ in range(n):
        x,y = map(int, input().split())
        if d >= y:
            a = x - math.sqrt(d**2-y**2)
            b = x + math.sqrt(d**2-y**2)
            data.append((a,b))
    if len(data) == n:
        data.sort()
        cnt = 1
        temp = data[0][1]
        for i in range(n):
            if temp >= data[i][0]:
                temp = min(data[i][1],temp)
            else:
                temp = data[i][1]
                cnt += 1
    else:
            cnt = -1
    print(f'Case {test}: {cnt}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241022130712990.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

随着难度的增加，发现需要用更多的时间完成练习，希望通过努力能够还跟得上每日选做。


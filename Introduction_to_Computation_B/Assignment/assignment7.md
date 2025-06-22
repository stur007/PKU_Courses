# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>任宇桐 物理学院</mark>



**说明：**

1）⽉考： AC5<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：

先按照年龄分类，然后按照对应的参数排序即可。

用时<10min

代码：

```python
n = int(input())
s = []
o = []
cnt = 0
for _ in range(n):
    x, y = input().split()
    y = int(y)
    if y >= 60:
        cnt += 1
        o.append((x, y, cnt))
    else:
        s.append((x, y))
o.sort(key = lambda x:(-x[1], x[2]))
ans = []
for i in o:
    ans.append(i[0])
for i in s:
    ans.append(i[0])
print(*ans, sep = '\n')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241107175158962.png)

### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：

一开始直接暴力计算，直接遍历乘积矩阵中的每一个矩阵元，然后成功超时，后来发现其实完全可以通过空间存储量的增加弥补时间的问题，如果进行2重循环就可以解决问题。

用时20min

代码：

```python
n, m1, m2 = map(int, input().split())
d1 = []
d2 = []
for _ in range(m1):
    d1.append(list(map(int, input().split())))
for _ in range(m2):
    d2.append(list(map(int, input().split())))
ans = [[0]*n for _ in range(n)]
for a1 in d1:
    i = a1[0]
    j = a1[1]
    k = a1[2]
    for a2 in d2:
        if a2[0] == j:
            p =a2[1]
            q = a2[2]
            ans[i][p] += k*q
for i in range(n):
    for j in range(n):
        if ans[i][j] != 0:
            print(i,j,ans[i][j])
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241107175508077.png)

### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：

这一题目思路感觉比较简单，可以直接按照时间和技能排序，很快就能搞定。

用时10min

代码：

```python
t = int(input())
for _ in range(t):
    n, m, b = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(list(map(int, input().split())))
    s.sort(key = lambda x:(x[0],-x[1]))
    temp = -1
    cnt = m
    for i in s:
        if temp == i[0]:
            if cnt == 0:
                continue
            cnt -= 1
        else:
            temp = i[0]
            cnt = m
            cnt -= 1

        b -= i[1]

        if b <= 0:
            print(temp)
            break
    if b> 0:
        print('alive')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241107175710093.png)

### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：

*考试的时候认为这道题目和小偷背包十分相似，但是初始条件的判定和中间的处理过程还是有一定的思维量的，而且好不容易想清楚以后还会超时，考试的时候就没能成功解决，对我而言难度超过了Tough的题目（？）*

上面是考完以后立即写的，但是下来求助了一下AI发现正常的思路就能通过，但是自己没有掌握dp的一般写法（**刚刚学了所以还没掌握？**）发现其实没有那么难

代码：

```python
# 可以AC的代码，用时15887ms
n, m = map(int, input().split())
dp = [0]+[float('inf')]*m
s = list(map(int, input().split()))
for i in range(n):
        for j in range(s[i-1], m+1):
                dp[j] = min(dp[j], dp[j-s[i-1]]+1)
if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])
    
#TLE的代码
n, m = map(int, input().split())
dp = [0]+[float('inf')]*m
s = list(map(int, input().split()))
for i in range(n):
        for j in range(1, m+1):
            if j>=s[i-1]:
                dp[j] = min(dp[j], dp[j-s[i-1]]+1)
            else:
                dp[j] = dp[j] #重点就在于这个地方，考试的时候不知道为什么写了一行奇怪的无效代码导致没能AC
if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241107183808108.png)

### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：

直觉上看起来还是不算太难的，但是想到出现thousand和million就直接截断还是不是那么容易的，虽然根据题目的提示可以看出hundred和其他两个量词的区别，但是根据这一点想要成功解决这一题目还是需要想很长时间的。

用时30min

代码：

```python
s1 = {'negative':-1}
s2= {'zero':0,'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90}
s3 = {'hundred':100}
s4 = {'thousand':1000, 'million':10**6}
n = list(input().split())
flag = 1
if n[0] in s1:
    flag = -1
    n.pop(0)
temp = 0

ans = 0
for i in range(len(n)):
    if n[i] in s2:
        temp += s2[n[i]]
    elif n[i] in s3:
        temp =temp*s3[n[i]]
    else:
        temp = temp*s4[n[i]]
    if i == len(n)-1 or n[i] in s4:
        ans += temp
        temp = 0
print(flag *ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241107180323300.png)

### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：

这道题目之前根据老师的讲义学习了区间问题的处理，发现这道题目还是很快就能AC的。

用时10min

代码：

```python
n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
s.sort(key=lambda x:x[1])
temp = s[0][1]
cnt = 1
for i in range(1,n):
    if s[i][0] > temp:
        cnt += 1
        temp = s[i][1]
print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241107180541787.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

这次月考题目对我而言其实还是有一定难度的，卡着时间刚刚AC5，可能是刚刚学习了许多算法还不是特别熟悉的缘故吧。发现做完题目以后**及时查看**题解之中的答案代码，尽量每道题目都用最正规简单的方式搞定，这样在面对复杂的问题是才能将潜在的问题风险降到最低。

同时，我还发现其实题目的难度确实是因人而异的，不一定非要按照从前到后的顺序把题目逐一解完。

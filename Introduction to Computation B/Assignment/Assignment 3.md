# Assign #3: Oct Mock Exam暨选做题目满百

2024 fall, Complied by 任宇桐 物理学院==（请改为同学的姓名、院系）==



**说明：**

1）Oct⽉考： AC5==（请改为同学的通过数）== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/

用时<10min

思路：

考试时候直接手动创建了字母表，然后发现k的值会超出字母表的范围，要对26取余数。

代码

```python
import string
k = int(input())%26
s = input()
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
ans = []
for i in range(len(s)):
    if s[i].islower():
        ans.append(lower[lower.index(s[i])-k])
    else:
        ans.append(upper[upper.index(s[i])-k])
print(*ans, sep = '')
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241010201742899.png)

### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/

用时<10min

思路：

直接计算

代码

```python
a, b = map(str, input().split())
c = int(a[0:2])
d = int(b[0:2])
print(c+d)
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241010172108252.png)

### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/

用时<10min

思路：

直接判断

代码

```python
n = int(input())
num = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
for _ in range(n):
    s = input()
    result = 0
    for i in range(17):
        result += num[i] * int(s[i])
    result = result%11
    ref = ['1','0','X','9','8','7','6','5','4','3','2']
    last = ref[result]
    if s[-1] == last:
        print('YES')
    else:
        print('NO')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241010172155092.png)

### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/

用时<10min

思路：

直接计算

代码

```python
n = int(input())
while n >1:
    if n %2 == 1:
        s = int(n*3)+1
        print(f'{n}*3+1={s}')
        n = s
    else:
        s = int(n/2)
        print(f'{n}/2={s}')
        n = s
print('End')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241010172405318.png)

### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/

用时60min

思路：

注意分类讨论，考试的时候不小心代码中字母V小写，导致用时过长。

##### 代码

```python
ref = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
num = [1,5,10,50,100,500,1000]
s = input()
if s.isalpha():
    ans = 0
    for i in range(len(s)-1):
        if ref.index(s[i]) < ref.index(s[i+1]):
            ans -= num[ref.index(s[i])]
        else:
            ans += num[ref.index(s[i])]
    ans += num[ref.index(s[-1])]
    print(ans)
else:
    ans = ''
    s = s[::-1]
    for i in range(len(s)):
        num = int(s[i])
        if num <= 3:
            ans = ref[2*i]*num +ans
        elif num == 4:
            ans = ref[2*i]+ref[2*i+1] +ans
        elif num <= 8:
            ans = ref[2*i+1] + ref[2*i] *(num -5) + ans
        elif num == 9:
            ans = ref[2*i] + ref[2*i+2]+ ans
    print(ans)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](https://raw.githubusercontent.com/stur007/img/main/img/image-20241010200418466.png)

### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/

暂时还搞不定www...

思路：



代码

```python


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

通过月考发现自己的基本语法还算熟练掌握，但是发现自己的代码还有不少可以优化的地方，同时要注意时刻检查代码书写的**准确性**，如相似字母的大小写等等，这种错误难以检查出来，需要**书写**代码的时候就保持谨慎，同时**优化**以后发现减少了书写错误的可能。


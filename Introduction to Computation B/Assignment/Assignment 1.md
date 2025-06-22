20240911，Complied by ==任宇桐，物理学院==

## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/

用时：0-5 min

思路：

使用if条件判断是否是闰年，之前开始时有尝试过分别计算a除以4，100，400，3200是否为整数，但是发现复杂程度接近。

##### 代码

```python
# Python
a=int(input())
if a%4 != 0:
    print('N')
else:
    if a%100 != 0:
        print('Y')
    else:
        if a%400 != 0:
            print('N')
        else:
            if a%3200 != 0:
                print('Y')
            else:
                print('N')
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240911190335448](https://raw.githubusercontent.com/stur007/img/main/img/202501121118697.png)

### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/

用时：0-5 min

思路：

从0开始逐个枚举。

##### 代码

```python
# Python
a=int(input())
list=[]
for i in range(0,int(a/4)+1):
    j=(a-4*i)/2
    if j%1==0:
        list.append(i+j)
if list:
    print(int(list[-1]),int(list[0]))
else:
    print(0,0)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240911190442295](https://raw.githubusercontent.com/stur007/img/main/img/202501121119515)

### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A

用时：5-10 min

思路：

如果直接铺设的话也并不复杂，但是发现空下的数目只能是0或1，所以直接整除。

##### 代码

```python
# Python
M,N=[int(x) for x in input().split()]
num=M*N//2
print(num)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240911190919758](https://raw.githubusercontent.com/stur007/img/main/img/202501121119350)

### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A

用时：5-10 min

思路：

直接铺设即可，注意整除与否的条件。

##### 代码

```python
# Python
m,n,a=map(int,input().split())
if m%a==0:
    num_m=m//a
else:
    num_m=m//a+1
 
if n%a==0:
    num_n=n//a
else:
    num_n=n//a+1
 
print(num_m*num_n)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240911190957070](https://raw.githubusercontent.com/stur007/img/main/img/202501121120324)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A

用时：10-15 min

思路：

原来计划直接比较，参考了题解之后发现原来字符串可以直接比较大小。

##### 代码

```python
# Python
string_1=input().lower()
string_2=input().lower()
if string_1==string_2:
    print('0')
elif string_1>string_2:
    print('1')
else:
    print('-1')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240911191150542](https://raw.githubusercontent.com/stur007/img/main/img/202501121121120.png)

### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A

用时：5-10 min

思路：

因为是0和1，所以可以直接用求和的办法判断是否可行。

##### 代码

```python
# Python
n=int(input())
count=0
for i in range(n):
    scores=input().split()
    tot=0
    for score in scores:
        score=int(score)
        tot+=score
    if tot>=2:
        count+=1
print(count)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240911191248219](https://raw.githubusercontent.com/stur007/img/main/img/202501121121779.png)



## 2. 学习总结和收获

从零基础开始，通过练习学会了基本的if结构，以及对应的输入输出的处理方案。
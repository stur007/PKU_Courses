m = int(input())
s = list(map(int, input().split()))

for num in s:
    found = False
    for j in range(1,int(num**0.5) + 1):
        for k in range(j, int(num**0.5) + 1):
            if j**2 + k**2 == num:
                found = True
                print(bin(num), oct(num), hex(num))
                break
        if found:
            break
###典型的错误解法：
'''
import math

m = int(input())
s = list(map(int, input().split()))

for num in s:
    found = False
    for j in range(int(math.sqrt(num)) + 1):
        k = math.sqrt(num - j ** 2)
        if k.is_integer(): ###这一步是否判断了k > 0 呢
            found = True
            print(bin(num), oct(num), hex(num))
            break
'''
# 写法1：直接实现
import math
a, b, c, d = map(int, input().split())
num = a*d+b*c
den = b*d
common = math.gcd(num, den)
top = num//common
bottom = den//common
print(f'{top}/{bottom}')

# 写法2
import math

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    def __add__(self, another):
        orig_num = self.num*another.den+another.num*self.den
        orig_den = self.den*another.den
        common = math.gcd(orig_num, orig_den)
        top = orig_num // common
        bottom = orig_den // common
        return f'{top}/{bottom}'

a, b, c, d = map(int, input().split())
first = Fraction(a, b)
second = Fraction(c, d)
print(first+second)
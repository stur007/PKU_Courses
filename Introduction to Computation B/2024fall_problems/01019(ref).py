import math

a = [0] * 34001
s = [0] * 34001

def init():
    a[1] = s[1] = 1
    for i in range(2, 34001):
        a[i] = a[i - 1] + int(math.log10(i)) + 1
        s[i] = s[i - 1] + a[i]

def print_digit(x, y):
    # 输出结果，例如123456789 我们还剩余5位 应该输出5 那么我们就把后面的4位去掉再求余
    x //= 10 ** y
    print(x % 10)

def main():
    init()
    t = int(input())
    while t > 0:
        n = int(input())
        i = 1
        while s[i] < n:
            i += 1
        pos = n - s[i - 1]
        i = 0
        while pos > a[i]:
            i += 1
        print_digit(i, a[i] - pos)
        t -= 1

if __name__ == "__main__":
    main()
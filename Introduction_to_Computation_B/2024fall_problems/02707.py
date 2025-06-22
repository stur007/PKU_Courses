import math

n = int(input())
for _ in range(n):
    a, b, c = [float(x) for x in input().split()]
    if b == 0:
        b = -b
    delta = b**2 - 4*a*c
    if delta == 0:
        ans =-b/(2*a)
        print(f'x1=x2={ans:.5f}')
    elif delta > 0:
        ans_1 = -b/(2*a)+math.sqrt(delta)/(2*a)
        ans_2 = -b/(2*a)-math.sqrt(delta)/(2*a)
        print(f'x1={ans_1:.5f};x2={ans_2:.5f}')
    else:
        real_part = -b/(2*a)
        imagine_part = math.sqrt(-delta)/(2*a)
        ans_1 = f'{real_part:.5f}+{imagine_part:.5f}i'
        ans_2 = f'{real_part:.5f}-{imagine_part:.5f}i'
        print(f'x1={ans_1};x2={ans_2}')
import math
def is_prime_number(n):
    flag = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            flag = 0
            break
    if flag == 1:
        return True

s = int(input())

for i in range(int(s/2)+1,1,-1):
    if is_prime_number(i) and is_prime_number(s-i):
        print(int(i*(s-i)))
        break